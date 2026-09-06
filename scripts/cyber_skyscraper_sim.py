#!/usr/bin/env python3
"""
================================================================================
CYBER-SKYSCRAPER PROJECT HEALTH & RISK SIMULATOR (CLI ENGINE)
Author: [PT:AC] Andy Kieckhefer
================================================================================
A terminal simulator that embodies software development and cyber risk
forecasting as an 828m skyscraper. Renders structural health zones, simulates
daily cyber/weather threats (DDoS storms, zero-days), and tracks project health.
"""

import os
import sys
import time
import math
import random
import argparse

# Enforce UTF-8 on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Terminal Styling
GREEN = "\033[92m"
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
RED = "\033[91m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

class CyberSkyscraperSimulator:
    def __init__(self, target_height=828.0, total_floors=163):
        self.target_height = target_height
        self.total_floors = total_floors
        self.current_height = 0.0
        self.current_floor = 0
        self.hp = 100.0
        self.waf_integrity = 100.0
        self.damper_active = False
        self.ddos_active = False
        self.exploit_active = False
        self.day = 1

    def render_ascii_spire(self):
        """Draws ASCII representation of current skyscraper state."""
        h_ratio = self.current_height / self.target_height
        fl_ratio = self.current_floor / self.total_floors

        fl_core_color = CYAN if not self.ddos_active else RED
        spire_status = f"{PURPLE}⚡ BROADCASTING{RESET}" if self.current_floor >= 150 else f"{DIM}STANDBY{RESET}"
        damper_status = f"{YELLOW}SWAYING (-42% SHOCK){RESET}" if self.current_floor >= 115 else f"{DIM}PENDING FL 88{RESET}"
        facade_status = f"{GREEN}100% SECURE{RESET}" if self.waf_integrity > 85 else f"{ORANGE}{self.waf_integrity:.0f}% STRAIN{RESET}"
        caisson_status = f"{GREEN}ANCHORED (ZERO-TRUST){RESET}"

        print(f"\n{BOLD}{CYAN}                 /\\                 {RESET} [ZONE 5: TELEMETRY SPIRE]  -> {spire_status}")
        print(f"{BOLD}{CYAN}                /  \\                {RESET} Production Observability & Sentinel AI (828m)")
        print(f"{BOLD}{CYAN}               /====\\               {RESET}")
        print(f"{BOLD}{CYAN}              /  {YELLOW}(●){CYAN}  \\              {RESET} [ZONE 4: TUNED MASS DAMPER] -> {damper_status}")
        print(f"{BOLD}{CYAN}             /        \\             {RESET} Level 88: 660-Ton Fallback & Circuit Breaker")
        print(f"{BOLD}{CYAN}            /==========\\            {RESET}")
        print(f"{BOLD}{CYAN}           /  {fl_core_color}||||||{CYAN}    \\           {RESET} [ZONE 3: WAF CURTAIN WALL]  -> {facade_status}")
        print(f"{BOLD}{CYAN}          /   {fl_core_color}||||||{CYAN}     \\          {RESET} Aerodynamic Vortex Shedding & DDoS Shield")
        print(f"{BOLD}{CYAN}         /==============\\           {RESET}")
        print(f"{BOLD}{CYAN}        /     {fl_core_color}[CORE]{CYAN}     \\          {RESET} [ZONE 2: DATA CORE SPINE]   -> {CYAN}CI/CD & gRPC Mesh{RESET}")
        print(f"{BOLD}{CYAN}       /==================\\         {RESET} High-Throughput Event Streaming Conduit")
        print(f"{BOLD}{GREEN}      [====================]        {RESET} [ZONE 1: BEDROCK CAISSONS]  -> {caisson_status}")
        print(f"{BOLD}{GREEN}        ||   ||    ||   ||          {RESET} 100ft Piles into Rock · HSM & IAM Root")
        print(f"{DIM}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}\n")

    def print_hud(self):
        hp_color = GREEN if self.hp > 75 else (YELLOW if self.hp > 45 else RED)
        hp_bars = int(self.hp // 5)
        hp_bar = f"{hp_color}{'█' * hp_bars}{DIM}{'░' * (20 - hp_bars)}{RESET}"

        waf_bars = int(self.waf_integrity // 5)
        waf_bar = f"{CYAN}{'█' * waf_bars}{DIM}{'░' * (20 - waf_bars)}{RESET}"

        print(f"{BOLD}{'='*80}{RESET}")
        print(f"  {BOLD}DAY: {self.day:03d} / 365{RESET}  |  {BOLD}HEIGHT:{RESET} {CYAN}{self.current_height:5.1f}m / {self.target_height}m{RESET}  |  {BOLD}FLOORS:{RESET} {self.current_floor:03d} / {self.total_floors}")
        print(f"  {BOLD}STRUCTURAL HEALTH:{RESET} [{hp_bar}] {hp_color}{self.hp:5.1f}%{RESET}  |  {BOLD}WAF INTEGRITY:{RESET} [{waf_bar}] {self.waf_integrity:5.1f}%")
        print(f"  {BOLD}CYBER DEFENSE GRID:{RESET} {GREEN}EU AI Act [✔] · NIST AI RMF [✔] · ISO 42001 [✔]{RESET}")
        print(f"  {BOLD}ATTACK STATUS:{RESET} {RED if self.ddos_active or self.exploit_active else GREEN}{'🚨 ACTIVE INGRESS ATTACK' if self.ddos_active or self.exploit_active else '🟢 DEFCON 5 // CALM'}{RESET}")
        print(f"{BOLD}{'='*80}{RESET}")

    def advance_build(self, days=10):
        self.day = min(365, self.day + days)
        ratio = self.day / 365.0
        self.current_height = ratio * self.target_height
        self.current_floor = int(ratio * self.total_floors)
        if self.current_floor >= 115:
            self.damper_active = True

        # Natural recovery if not under attack
        if not self.ddos_active and not self.exploit_active:
            self.hp = min(100.0, self.hp + 5.0)
            self.waf_integrity = min(100.0, self.waf_integrity + 10.0)

    def trigger_ddos_storm(self):
        self.ddos_active = True
        print(f"\n{RED}{BOLD}⚡ CYBER INCIDENT: 1.2 Tbps DDoS Gale Wind Ingress Surge!{RESET}")
        if self.damper_active:
            print(f"{YELLOW}★ LEVEL 88 TUNED MASS DAMPER ENGAGED! Counter-torque absorbed 42% kinetic drag!{RESET}")
            self.hp = max(75.0, self.hp - 10.0)
            self.waf_integrity = max(70.0, self.waf_integrity - 15.0)
        else:
            print(f"{RED}💥 Damper not yet reached! Structural vibration causing API latency! (-25 HP){RESET}")
            self.hp = max(40.0, self.hp - 25.0)
            self.waf_integrity = max(40.0, self.waf_integrity - 35.0)

    def trigger_zero_day(self):
        self.exploit_active = True
        print(f"\n{RED}{BOLD}⚡ ZERO-DAY VULNERABILITY: Upstream REST dependency breached!{RESET}")
        print(f"{ORANGE}↳ Ingress diverted to Dual-Ingestion Adapter Bridge!{RESET}")
        self.hp = max(50.0, self.hp - 20.0)

    def trigger_act_of_war_pentest(self):
        """Simulates an Act of War: Red-Team Penetration Testing Siege."""
        self.exploit_active = True
        print(f"\n{RED}{BOLD}⚔️  ACT OF WAR: RED-TEAM PENETRATION TEST SIEGE INITIATED!{RESET}")
        print(f"{ORANGE}↳ Adversary simulating state-sponsored kinetic cyber assault:{RESET}")
        print(f"   • High-velocity SQLi/RCE artillery bombardment against Floor 10–30 facade")
        print(f"   • Automated credential-stuffing battering ram on API gateway")
        print(f"   • Subterranean sappers attempting lateral movement across VPC subnets")
        if self.damper_active:
            print(f"{YELLOW}★ BLAST-RESISTANT CURTAIN WALL ENGAGED! ZTNA airlocks sealed! (-12% WAF strain){RESET}")
            self.hp = max(70.0, self.hp - 8.0)
            self.waf_integrity = max(65.0, self.waf_integrity - 12.0)
        else:
            print(f"{RED}💥 Perimeter breached! Penetration testers reached internal staging vault! (-30 HP){RESET}")
            self.hp = max(35.0, self.hp - 30.0)
            self.waf_integrity = max(30.0, self.waf_integrity - 40.0)

    def trigger_war_simulation_breach(self):
        """Simulates a War Simulation: Catastrophic Security Breach & Progressive Collapse Rehearsal."""
        self.ddos_active = True
        self.exploit_active = True
        print(f"\n{PURPLE}{BOLD}🛡️  WAR SIMULATION: FULL SECURITY BREACH & PROGRESSIVE COLLAPSE REHEARSAL!{RESET}")
        print(f"{CYAN}↳ Blast-Radius Scenario: Master signing key leaked + Subterranean caisson compromised!{RESET}")
        print(f"   • Evaluating GSA Progressive Collapse: Severing 2 adjacent structural columns")
        print(f"   • Micro-segmented blast bulkheads slam shut across VPC clusters within 380ms")
        print(f"   • Outer Space Photonic Switch engages out-of-band kill-switch link")
        print(f"{GREEN}✔ Progressive collapse averted: Steel transfer trusses absorb redistributed load!{RESET}")
        print(f"{GREEN}✔ Cargo Integrity 100% INTACT: Cryptographic HSM root held firm in bedrock!{RESET}")
        self.hp = max(60.0, self.hp - 15.0)

    def deploy_patch(self):
        self.ddos_active = False
        self.exploit_active = False
        self.waf_integrity = 100.0
        self.hp = min(100.0, self.hp + 20.0)
        print(f"\n{GREEN}{BOLD}✔ WAF SHIELD & SECURITY PATCH DEPLOYED! All systems green.{RESET}")

def run_cli_sim(mode="normal"):
    sim = CyberSkyscraperSimulator()
    print(f"\n{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║     CYBER-SKYSCRAPER PROJECT HEALTH & RISK SIMULATOR // CLI RUNTIME          ║{RESET}")
    print(f"{BOLD}{CYAN}║  A Visual High-Rise Metaphor for Enterprise Cloud & Cyber Security Dev       ║{RESET}")
    if mode == "war":
        print(f"{BOLD}{PURPLE}║  [MODE: FORTRESS WARFARE] Acts of War (Pen-Testing) & War Simulations (BAS)   ║{RESET}")
    else:
        print(f"{BOLD}{CYAN}║  [MODE: 365-DAY RUNWAY] Everyday Production Weather Volatility               ║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")

    if mode == "war":
        milestones = [
            (60, "Bedrock Caissons Set: Zero-Trust HSM Piles Grounded to Rock", None),
            (120, "Core Spine Erected: Initiating ACT OF WAR (Red-Team Pen-Test Siege)", "pentest"),
            (140, "Deploying Blast-Hardened WAF & ZTNA Biometric Airlocks", "patch"),
            (250, "Curtain Wall Sealed: Installing Level 88 Damper & Space Switch Uplink", None),
            (300, "Executing WAR SIMULATION (Catastrophic Breach & Progressive Collapse)", "breach"),
            (320, "Sealing Compartmentalized Bulkheads & Out-of-Band Key Rotation", "patch"),
            (365, "Apex Spire Complete (828m)! Full DoD UFC & EU AI Act War-Proof Certified!", None)
        ]
    else:
        # Build sequence simulation
        milestones = [
            (60, "Foundation & Zero-Trust HSM Piles Complete (+EU AI Act Art 9/10)", None),
            (120, "Concrete Core Erected; Triggering DDoS Storm", "ddos"),
            (130, "Deploying Cloudflare WAF Patch & Ingress Rate Limiters", "patch"),
            (250, "Aerodynamic Glass Facade Sealed; Level 88 Damper Installed", None),
            (280, "Triggering Zero-Day Upstream API Sunset during Nor'easter", "zeroday"),
            (290, "Activating Tuned Mass Damper & Dual-Ingestion Bypass", "patch"),
            (365, "Apex Spire Needle Erected (828m)! Final Occupancy Certificate Issued!", None)
        ]

    for target_day, desc, action in milestones:
        sim.advance_build(days=(target_day - sim.day))
        sim.render_ascii_spire()
        sim.print_hud()
        print(f">>> {BOLD}{desc}{RESET}")

        if action == "ddos":
            sim.trigger_ddos_storm()
        elif action == "zeroday":
            sim.trigger_zero_day()
        elif action == "pentest":
            sim.trigger_act_of_war_pentest()
        elif action == "breach":
            sim.trigger_war_simulation_breach()
        elif action == "patch":
            sim.deploy_patch()

        time.sleep(0.5)

    print(f"\n{GREEN}{BOLD}🏆 SKYSCRAPER VESSEL CADENCE COMPLETE!{RESET}")
    print(f"Final Height: {sim.current_height:.1f}m / 163 Floors | Hull Health: {sim.hp:.1f}%")
    print(f"Fortress Certification: GSA Progressive Collapse [✔] · EU AI Act [✔] · NIST AI RMF [✔]\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cyber-Skyscraper Simulator")
    parser.add_argument("--mode", choices=["normal", "war"], default="normal", help="Simulation mode")
    args = parser.parse_args()
    run_cli_sim(mode=args.mode)
