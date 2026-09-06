#!/usr/bin/env python3
"""
================================================================================
BMS // CYBER-BUILDING MANAGEMENT SYSTEM & META-RISK FINE-TUNER
Author: [PT:AC] Andy Kieckhefer
================================================================================
Models internal building dynamics:
1. HVAC & Thermal Regulation (Compute Throttling, Pool Circulation)
2. Dual Heatmaps (Human Workload/Burnout & Network Ingress/Saturation)
3. The Meta-Risk of the Risk Rollout itself (Iatrogenic Drag, False Positives)
4. Closed-Loop Fine-Tuning Calibration
================================================================================
"""

import os
import sys
import json
import math
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

class CyberBMSFineTuner:
    def __init__(self, sensitivity=0.75, hvac_speed=0.65, waf_strictness=0.80):
        # Fine-Tuning Knobs (0.0 to 1.0)
        self.sensitivity = sensitivity        # Alert sensitivity (higher = more warnings)
        self.hvac_speed = hvac_speed          # Cooling & cache recycling speed
        self.waf_strictness = waf_strictness  # Defense strictness (higher = blocks more, higher false positives)

    def evaluate_hvac_thermal(self):
        """Calculates internal compute thermal load and HVAC cooling efficiency."""
        base_compute_load = 68.0 # % capacity
        cooling_power = self.hvac_speed * 100.0
        net_temp_celsius = max(38.0, 95.0 - (cooling_power * 0.55))
        
        thermal_status = "OPTIMAL" if net_temp_celsius < 55 else ("WARM" if net_temp_celsius < 75 else "OVERHEATED")
        status_color = GREEN if thermal_status == "OPTIMAL" else (YELLOW if thermal_status == "WARM" else RED)

        return {
            "compute_load_pct": base_compute_load,
            "core_temp_c": round(net_temp_celsius, 1),
            "hvac_cooling_speed_pct": round(cooling_power, 1),
            "air_circulation_cfm": int(12000 * self.hvac_speed),
            "thermal_status": thermal_status,
            "status_color": status_color
        }

    def evaluate_heatmaps(self):
        """Generates floor-by-floor People and Network heat density."""
        floors = [
            {"zone": "Crown (L150-163)", "people_heat": 24, "network_heat": 42, "desc": "Observability & Sentinel AI"},
            {"zone": "TMD Penthouse (L88-149)", "people_heat": 35, "network_heat": 68, "desc": "Circuit Breakers & Proxy Bridges"},
            {"zone": "Mid-Rise Superstructure (L40-87)", "people_heat": 88, "network_heat": 92, "desc": "Core Product Epics (CRITICAL HOTSPOT)"},
            {"zone": "Podium & Core (L10-39)", "people_heat": 62, "network_heat": 78, "desc": "Data Pipelines & Ingress Mesh"},
            {"zone": "Bedrock Vaults (L01-09)", "people_heat": 15, "network_heat": 32, "desc": "Zero-Trust HSM & Cryptographic Key Store"}
        ]
        return floors

    def evaluate_meta_risk(self):
        """
        Calculates the 'Risk of the Risk Tool itself' (Iatrogenic Drag):
        - High sensitivity -> Alert Fatigue & False Positives
        - High WAF strictness -> Blocked legitimate users & Developer Friction
        - Frustrated developers -> Shadow IT ingress
        """
        # Alert fatigue index (0 to 100)
        alert_fatigue = round((self.sensitivity ** 1.8) * 85.0, 1)
        
        # False alarm rate
        false_positives = round((self.sensitivity * self.waf_strictness) * 45.0, 1)
        
        # Developer friction drag (slows sprint velocity)
        dev_friction = round(((self.waf_strictness * 0.6) + (self.sensitivity * 0.4)) * 38.0, 1)
        
        # Shadow IT risk probability (teams bypassing strict rules)
        shadow_it_prob = round(max(5.0, (dev_friction * 1.5) - (self.hvac_speed * 15.0)), 1)
        
        # Total Meta-Risk Score (Iatrogenic Damage)
        meta_risk_score = round((alert_fatigue * 0.3) + (false_positives * 0.25) + (dev_friction * 0.25) + (shadow_it_prob * 0.2), 1)

        meta_status = "HEALTHY BALANCE" if meta_risk_score < 35 else ("MODERATE FRICTION" if meta_risk_score < 60 else "IATROGENIC PARALYSIS")
        status_color = GREEN if meta_risk_score < 35 else (YELLOW if meta_risk_score < 60 else RED)

        return {
            "meta_risk_score": meta_risk_score,
            "meta_status": meta_status,
            "status_color": status_color,
            "alert_fatigue_index": alert_fatigue,
            "false_positive_pct": false_positives,
            "developer_friction_pct": dev_friction,
            "shadow_it_probability_pct": shadow_it_prob
        }

    def print_bms_dashboard(self):
        hvac = self.evaluate_hvac_thermal()
        meta = self.evaluate_meta_risk()
        heatmaps = self.evaluate_heatmaps()

        print(f"\n{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"{BOLD}{CYAN}║             CYBER-BMS // BUILDING MANAGEMENT & META-RISK DASHBOARD               ║{RESET}")
        print(f"{BOLD}{CYAN}║     HVAC Thermal Loops · Network/People Heatmaps · Iatrogenic Risk Tuning        ║{RESET}")
        print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════════════════════════╝{RESET}\n")

        # Section 1: HVAC Climate Control
        print(f"{BOLD}1. HVAC & THERMAL COMPUTING REGULATION:{RESET}")
        print(f"   Core Compute Temp   : {hvac['status_color']}{hvac['core_temp_c']}°C [{hvac['thermal_status']}]{RESET}")
        print(f"   Chilled Air Speed   : {CYAN}{hvac['hvac_cooling_speed_pct']}% capacity ({hvac['air_circulation_cfm']:,} CFM){RESET}")
        print(f"   Thermal Action      : Dynamic HPA pod scaling & memory cache circulating.\n")

        # Section 2: Heatmaps
        print(f"{BOLD}2. MULTI-LAYER DUAL HEATMAPS (FLOOR-BY-FLOOR):{RESET}")
        print(f"   {'ZONE / ELEVATION':<32} | {'👥 TEAM HEAT':<14} | {'🌐 NETWORK HEAT':<16} | {'STATUS'}")
        print(f"   {'-'*80}")
        for fl in heatmaps:
            p_color = GREEN if fl['people_heat'] < 40 else (YELLOW if fl['people_heat'] < 75 else RED)
            n_color = GREEN if fl['network_heat'] < 40 else (YELLOW if fl['network_heat'] < 75 else RED)
            print(f"   {fl['zone']:<32} | {p_color}{fl['people_heat']:3d}% density{RESET}   | {n_color}{fl['network_heat']:3d}% throughput{RESET} | {fl['desc']}")
        print()

        # Section 3: The Meta-Risk of the Risk Rollout Itself
        print(f"{BOLD}3. META-RISK // THE RISK OF ROLLING OUT THE RISK TOOL ITSELF:{RESET}")
        print(f"   Iatrogenic Harm Index : {meta['status_color']}{meta['meta_risk_score']}% [{meta['meta_status']}]{RESET}")
        print(f"   Alert Fatigue Rating  : {YELLOW}{meta['alert_fatigue_index']}% (Developer warning exhaustion){RESET}")
        print(f"   False Positive Noise  : {ORANGE}{meta['false_positive_pct']}% (Benign commits flagged){RESET}")
        print(f"   Dev Velocity Drag     : {ORANGE}{meta['developer_friction_pct']}% sprint speed reduction{RESET}")
        print(f"   Shadow IT Leak Risk   : {RED if meta['shadow_it_probability_pct'] > 30 else GREEN}{meta['shadow_it_probability_pct']}% (Engineers bypassing security controls){RESET}\n")

        # Section 4: Closed-Loop Fine-Tuning Calibration
        print(f"{BOLD}4. CLOSED-LOOP FINE-TUNING RECOMMENDATIONS:{RESET}")
        if meta['meta_risk_score'] > 50:
            print(f"   {YELLOW}⚠️ OVER-ENFORCEMENT DETECTED:{RESET} Lower alert sensitivity to 0.60 to avoid alert fatigue.")
            print(f"   {YELLOW}⚠️ FRICTION MITIGATION:{RESET} Smooth WAF strictness to 0.70 to eliminate Shadow IT bypasses.")
        else:
            print(f"   {GREEN}✔ OPTIMAL EQUILIBRIUM:{RESET} Security envelopes protect the vessel without suffocating team velocity.")
        print()

def main():
    parser = argparse.ArgumentParser(description="Cyber BMS & Meta-Risk Fine-Tuner")
    parser.add_argument("--sensitivity", type=float, default=0.75, help="Alert sensitivity (0.1 to 1.0)")
    parser.add_argument("--hvac", type=float, default=0.65, help="HVAC fan cooling speed (0.1 to 1.0)")
    parser.add_argument("--waf", type=float, default=0.80, help="WAF strictness (0.1 to 1.0)")
    parser.add_argument("--json-out", default="bms_telemetry.json", help="Output JSON path")
    args = parser.parse_args()

    tuner = CyberBMSFineTuner(
        sensitivity=args.sensitivity,
        hvac_speed=args.hvac,
        waf_strictness=args.waf
    )
    tuner.print_bms_dashboard()

    report = {
        "hvac": tuner.evaluate_hvac_thermal(),
        "heatmaps": tuner.evaluate_heatmaps(),
        "meta_risk": tuner.evaluate_meta_risk(),
        "knobs": {
            "sensitivity": args.sensitivity,
            "hvac_speed": args.hvac,
            "waf_strictness": args.waf
        }
    }
    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"  {GREEN}✔{RESET} BMS telemetry saved to: {args.json_out}\n")

if __name__ == "__main__":
    main()
