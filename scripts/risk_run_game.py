#!/usr/bin/env python3
"""
================================================================================
AИDY'S RISK RUNNER: 60-MONTH HIGHWAY TO COMMENCEMENT
A Retro-Arcade Project Risk & Compliance Simulator
Author: [PT:AC] Andy Kieckhefer
================================================================================
Pilot your enterprise engineering project from Initiation (Month 0) to 
Commencement (Month 60+). Dodge potholes, clear EU AI Act police checkpoints, 
sniff hazards with NIST radar, and deploy architectural detour bridges!
"""

import sys
import time
import random
import argparse

# Enforce UTF-8 on Windows console
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

CAR_ART = r"""
        .--------.
____.../  _      _ \...____
`--.._ `-(_)----(_)-' _..--'
      `-------------`
"""

ROAD_ART = r"""
       |       :       |
      /        :        \
     /         :         \
    /          :          \
   /           :           \
  /            :            \
 /             :             \
"""

class RiskRunnerGame:
    def __init__(self, autoplay=False):
        self.autoplay = autoplay
        self.month = 0
        self.max_months = 60
        self.hp = 100
        self.speed = 75
        self.budget_fuel = 100
        self.xp = 0
        self.compliance_shield = 100
        self.inventory = {
            "nist_radar": 3,
            "eu_ai_shield": 2,
            "detour_bridge": 1,
            "lockfile_wrench": 3
        }
        self.active_detour = False

    def banner(self):
        print(f"\n{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{CYAN}║             AИDY'S RISK RUNNER // 60-MONTH HIGHWAY SIMULATOR                 ║{RESET}")
        print(f"{BOLD}{CYAN}║       EU AI Act (2024/1689) · NIST AI RMF 1.0 · Zero-Trust Highway           ║{RESET}")
        print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")

    def render_hud(self):
        hp_color = GREEN if self.hp > 60 else (YELLOW if self.hp > 30 else RED)
        hp_bars = int(self.hp // 5)
        hp_bar = f"{hp_color}{'█' * hp_bars}{DIM}{'░' * (20 - hp_bars)}{RESET}"

        fuel_bars = int(self.budget_fuel // 5)
        fuel_bar = f"{CYAN}{'█' * fuel_bars}{DIM}{'░' * (20 - fuel_bars)}{RESET}"

        shield_status = f"{GREEN}ACTIVE (100%){RESET}" if self.compliance_shield > 50 else f"{RED}OFFLINE (VULNERABLE){RESET}"

        print(f"\n{BOLD}{'='*78}{RESET}")
        print(f"  {BOLD}MONTH: {self.month:02d} / {self.max_months}{RESET}  |  {BOLD}STAGE:{RESET} {self.get_stage_name()}  |  {BOLD}XP:{RESET} {YELLOW}{self.xp}{RESET}")
        print(f"  {BOLD}VEHICLE HP:{RESET} [{hp_bar}] {self.hp}%  |  {BOLD}BUDGET/FUEL:{RESET} [{fuel_bar}] {self.budget_fuel}%")
        print(f"  {BOLD}SPEED:{RESET} {CYAN}{self.speed} mph{RESET}  |  {BOLD}LEGAL SHIELD:{RESET} {shield_status}  |  {BOLD}DETOUR:{RESET} {PURPLE}{'ENGAGED' if self.active_detour else 'STANDBY'}{RESET}")
        print(f"  {BOLD}INVENTORY:{RESET} 📡 NIST Radar: {self.inventory['nist_radar']} | 🛡️ EU AI Shield: {self.inventory['eu_ai_shield']} | 🌉 Detour Bridge: {self.inventory['detour_bridge']} | 🔧 Wrench: {self.inventory['lockfile_wrench']}")
        print(f"{BOLD}{'='*78}{RESET}")

    def get_stage_name(self):
        if self.month <= 6:
            return f"{GREEN}STAGE 0: INITIATION & SCOPE{RESET}"
        elif self.month <= 18:
            return f"{YELLOW}STAGE 1: ARCHITECTURAL FOUNDATION{RESET}"
        elif self.month <= 36:
            return f"{ORANGE}STAGE 2: ENTERPRISE SCALE & DEEP BUILD{RESET}"
        else:
            return f"{PURPLE}STAGE 3: FULL COMMENCEMENT & DURABILITY{RESET}"

    def trigger_event(self):
        """Random or milestone scripted encounters."""
        events = []
        if self.month == 6:
            events.append(("milestone", "🎯 MILESTONE: Stage 0 Certified! Runway approved by leadership. (+100 XP)", 100))
        elif self.month == 10:
            events.append(("pothole", "🕳️ POTHOLE ALERT: Major runtime update breaks legacy container builds!", -15, "lockfile_wrench"))
        elif self.month == 18:
            events.append(("checkpoint", "🚔 REGULATORY CHECKPOINT: EU AI Act & NIST compliance auditors demand conformity file!", -25, "eu_ai_shield"))
        elif self.month == 28:
            events.append(("road_closed", "⛔ ROAD CLOSED CRITICAL BREAKING POINT: Primary external API sunsets REST v1!", -50, "detour_bridge"))
        elif self.month == 42:
            events.append(("pothole", "🕳️ STAFFING BUMP: Senior security lead departs; knowledge gap detected.", -15, "lockfile_wrench"))
        elif self.month == 50:
            events.append(("traffic", "🚦 TRAFFIC JAM: Multi-entity legal data retention review delays merge.", -20, "nist_radar"))
        else:
            if random.random() < 0.35:
                minor_types = [
                    ("pothole", "🕳️ MINOR POTHOLE: Linter version drift detected in microservice.", -10, "lockfile_wrench"),
                    ("traffic", "🚦 MODERATE TRAFFIC: Security review backlog slows PR merges by 2 weeks.", -15, "nist_radar"),
                    ("boost", "⚡ CLEAN RUNWAY: Refactored test suite completes in 42 seconds! (+50 XP, +5 HP)", 50)
                ]
                events.append(random.choice(minor_types))

        for ev in events:
            ev_type = ev[0]
            desc = ev[1]
            print(f"\n>>> {BOLD}{desc}{RESET}")
            
            if ev_type == "milestone":
                self.xp += ev[2]
                self.hp = min(100, self.hp + 10)
            elif ev_type == "boost":
                self.xp += ev[2]
                self.hp = min(100, self.hp + 5)
            elif ev_type in ["pothole", "traffic", "checkpoint", "road_closed"]:
                penalty = ev[2]
                item_req = ev[3]

                if self.inventory.get(item_req, 0) > 0:
                    item_names = {
                        "lockfile_wrench": "🔧 Lockfile Wrench",
                        "eu_ai_shield": "🛡️ EU AI Compliance Shield",
                        "detour_bridge": "🌉 Dual-Ingestion Detour Bridge",
                        "nist_radar": "📡 NIST Sniffer Radar"
                    }
                    print(f"    {GREEN}ITEM AVAILABLE:{RESET} Deploy {item_names[item_req]} to counter hazard?")
                    if self.autoplay:
                        use_item = True
                        print(f"    {CYAN}[AUTOPLAY]{RESET} Automatically deployed {item_names[item_req]}!")
                    else:
                        resp = input(f"    Use {item_names[item_req]}? [Y/n]: ").strip().lower()
                        use_item = resp != "n"

                    if use_item:
                        self.inventory[item_req] -= 1
                        self.xp += 150
                        if item_req == "detour_bridge":
                            self.active_detour = True
                            print(f"    {PURPLE}★ DETOUR ARTERY ACTIVATED! Zero-downtime proxy deployed around breaking point! (+150 XP){RESET}")
                        else:
                            print(f"    {GREEN}★ HAZARD NEUTRALIZED! Zero damage taken. (+150 XP){RESET}")
                        continue

                # Take damage if no item used
                print(f"    {RED}💥 Direct impact! Took {abs(penalty)} HP damage!{RESET}")
                self.hp += penalty
                self.speed = max(20, self.speed - 15)

    def play_turn(self):
        self.render_hud()
        if self.hp <= 0:
            print(f"\n{RED}{BOLD}💀 GAME OVER: The project experienced catastrophic architectural failure!{RESET}")
            print(f"Total XP: {self.xp} | Survived to Month {self.month}")
            return False

        if self.month >= self.max_months:
            print(f"\n{GREEN}{BOLD}🏆 VICTORY! COMMENCEMENT ACHIEVED!{RESET}")
            print(f"You successfully steered a multi-year enterprise project across 60 months without catastrophic derailment!")
            print(f"Final XP: {YELLOW}{self.xp}{RESET} | Vehicle Durability: {GREEN}{self.hp}%{RESET}")
            return False

        if self.autoplay:
            print(f"\n{CYAN}[AUTOPLAY] Cruising forward 6 months...{RESET}")
            time.sleep(0.5)
            action = "1"
        else:
            print("\nCOMMANDS:")
            print("  [1] 🚗 Cruise Forward (Advance 6 Months)")
            print("  [2] 📡 Fire NIST Sniffer Radar (Scan next 12 months for hazards)")
            print("  [3] 🛡️ Refresh EU AI Act Compliance Shield")
            print("  [4] 🔧 Service Lockfiles & Patch Potholes")
            print("  [5] ⚡ Nitro Sprint (+10 mph, costs 15 fuel)")
            print("  [Q] Quit Game")
            action = input("Enter choice [1-5]: ").strip()

        if action == "1":
            self.month += 6
            self.budget_fuel = max(10, self.budget_fuel - 8)
            self.xp += 50
            self.trigger_event()
        elif action == "2":
            if self.inventory["nist_radar"] > 0:
                self.inventory["nist_radar"] -= 1
                print(f"\n{CYAN}📡 NIST RADAR SCANNING NEXT 12 MONTHS...{RESET}")
                print(f"   ↳ Month {self.month + 6}: Level 2 Pothole (Dependency Drift)")
                print(f"   ↳ Month {self.month + 12}: Level 3 Traffic (Governance Checkpoint)")
                print(f"   {GREEN}★ Hazard forecast logged into HUD! (+25 XP){RESET}")
                self.xp += 25
            else:
                print(f"\n{RED}Out of NIST Radar charges!{RESET}")
        elif action == "3":
            print(f"\n{GREEN}🛡️ EU AI Act technical conformity dossier regenerated! Shield at 100%! (+30 XP){RESET}")
            self.compliance_shield = 100
            self.xp += 30
        elif action == "4":
            print(f"\n{YELLOW}🔧 Running container lockfile stabilization and vulnerability linting... (+15 HP){RESET}")
            self.hp = min(100, self.hp + 15)
            self.xp += 20
        elif action == "5":
            if self.budget_fuel >= 15:
                self.budget_fuel -= 15
                self.speed = min(120, self.speed + 15)
                print(f"\n{BOLD}{CYAN}⚡ NITRO SPRINT ENGAGED! Cruising at {self.speed} mph!{RESET}")
            else:
                print(f"\n{RED}Low budget/fuel! Cannot sprint.{RESET}")
        elif action.lower() == "q":
            print("\nExiting Risk Runner.")
            return False

        return True

    def run(self):
        self.banner()
        while self.play_turn():
            pass

def main():
    parser = argparse.ArgumentParser(description="AИDY'S RISK RUNNER // Terminal Arcade Simulator")
    parser.add_argument("--autoplay", action="store_true", help="Run automated 60-month simulation")
    args = parser.parse_args()

    game = RiskRunnerGame(autoplay=args.autoplay)
    game.run()

if __name__ == "__main__":
    main()
