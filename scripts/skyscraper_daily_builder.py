#!/usr/bin/env python3
"""
================================================================================
THE SYNOPTIC SPIRE // 365-DAY DAILY WEATHER & SKYSCRAPER BUILD ITERATOR
Author: [PT:AC] Andy Kieckhefer
Standards: EU AI Act (2024/1689) | NIST AI RMF 1.0 | Aerodynamic Resilience
================================================================================
Anticipates daily atmospheric weather conditions for 365 days, models project
volatility, and executes iterative construction of an 828m enterprise skyscraper
with Tuned Mass Damper volatility stabilization and legal compliance checkmarks.
"""

import os
import sys
import math
import time
import json
import random
import argparse
from datetime import datetime, timedelta

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
GOLD = "\033[38;5;220m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

# 365-Day Synoptic Weather Generator
SYNOPTIC_SEASONS = [
    # Winter (Days 1–90): Polar Vortex, Blizzards, Freeze cycles
    {"days": (1, 90), "temp_range": (15, 42), "wind_base": 24, "wind_var": 18, "precip_prob": 0.35, "hazard_type": "Ice & Freezing Rain (Governance Freezes)"},
    # Spring (Days 91–180): High Wind Shear, Frontogenesis, Thunderstorms
    {"days": (91, 180), "temp_range": (45, 68), "wind_base": 28, "wind_var": 22, "precip_prob": 0.45, "hazard_type": "Gale Shear & Lightning (API Latency & DDoS)"},
    # Summer (Days 181–270): Heat Domes, Thermal Expansion, Convection Squalls
    {"days": (181, 270), "temp_range": (72, 98), "wind_base": 16, "wind_var": 14, "precip_prob": 0.25, "hazard_type": "Heat Domes (Compute Saturation & Throttling)"},
    # Autumn (Days 271–365): Nor'easters, Microbursts, Crisp Clear Highs
    {"days": (271, 365), "temp_range": (38, 65), "wind_base": 22, "wind_var": 20, "precip_prob": 0.30, "hazard_type": "Coastal Squalls (Upstream Schema Sunsets)"}
]

def generate_daily_weather(day_num):
    """Generates realistic meteorological conditions for a given day in the year."""
    season = next(s for s in SYNOPTIC_SEASONS if s["days"][0] <= day_num <= s["days"][1])
    
    # Seasonal base temperature with sinewave annual cycle
    annual_angle = (day_num / 365.0) * 2 * math.pi
    seasonal_temp_offset = -math.cos(annual_angle) * 25.0
    base_temp = 55.0 + seasonal_temp_offset + random.uniform(-8.0, 8.0)
    
    # Wind velocity (knots)
    wind_kts = max(4.0, season["wind_base"] + random.gauss(0, season["wind_var"] * 0.45))
    
    # Atmospheric pressure (hPa)
    pressure = round(1013.25 + random.uniform(-25.0, 20.0), 1)
    
    # Precipitation & Lightning
    has_precip = random.random() < season["precip_prob"]
    has_lightning = has_precip and (base_temp > 58.0) and (random.random() < 0.28)
    
    # Synoptic Condition Description
    if wind_kts > 42:
        condition = "Gale-Force Crosswind Storm"
        synoptic_code = "GALE"
    elif has_lightning:
        condition = "Severe Electrical Thunderstorm"
        synoptic_code = "TSRA"
    elif has_precip and base_temp < 32:
        condition = "Freezing Blizzard & Ice Accumulation"
        synoptic_code = "SNOW"
    elif has_precip:
        condition = "Precipitation & Low-Ceiling Fog"
        synoptic_code = "RAIN"
    elif base_temp > 88:
        condition = "High-Pressure Solar Heat Dome"
        synoptic_code = "HEAT"
    else:
        condition = "Fair Skies & Favorable Thermal Updraft"
        synoptic_code = "FAIR"

    # Volatility Index (0.0 to 100.0%)
    volatility = min(100.0, (wind_kts * 1.4) + (25.0 if has_lightning else 0.0) + (15.0 if synoptic_code == "SNOW" else 0.0))
    
    return {
        "day": day_num,
        "condition": condition,
        "synoptic_code": synoptic_code,
        "temp_f": round(base_temp, 1),
        "wind_kts": round(wind_kts, 1),
        "pressure_hpa": pressure,
        "has_lightning": has_lightning,
        "volatility_index_pct": round(volatility, 1),
        "hazard_metaphor": season["hazard_type"]
    }

class SkyscraperBuilder:
    def __init__(self, target_height_meters=828.0):
        self.target_height = target_height_meters
        self.current_height = 0.0
        self.total_floors = 163
        self.built_floors = 0
        self.structural_health = 100.0
        self.damper_active = False
        self.damper_counter_torque_nm = 0
        self.daily_logs = []
        self.compliance_stamps = {
            "eu_ai_art_9_10": False,
            "nist_govern_map": False,
            "eu_ai_art_11_13": False,
            "nist_measure_manage": False,
            "final_occupancy_cert": False
        }

    def iterate_day(self, weather):
        day = weather["day"]
        volatility = weather["volatility_index_pct"]
        wind = weather["wind_kts"]

        # Phase Classification
        if day <= 60:
            phase = "Stage 0: Bedrock Caissons & Foundation Piles"
            if day == 60:
                self.compliance_stamps["eu_ai_art_9_10"] = True
        elif day <= 150:
            phase = "Stage 1: Reinforced Concrete Core & Lobby Podium"
            if day == 150:
                self.compliance_stamps["nist_govern_map"] = True
        elif day <= 250:
            phase = "Stage 2: Superstructure Floors & Glass Curtain Wall"
            if day == 250:
                self.compliance_stamps["eu_ai_art_11_13"] = True
        elif day <= 320:
            phase = "Stage 3: Tuned Mass Damper (Level 88) & Mechanical Penthouse"
            self.damper_active = True
            if day == 320:
                self.compliance_stamps["nist_measure_manage"] = True
        else:
            phase = "Stage 4: Aerodynamic Crown Spire & Final Commissioning"
            if day == 365:
                self.compliance_stamps["final_occupancy_cert"] = True

        # Volatility Damping Physics
        mitigation_action = "Standard Continuous Build Cadence"
        daily_rise = self.target_height / 365.0

        if volatility > 55.0:
            if self.damper_active:
                # Tuned Mass Damper absorbs 70% of volatility
                damped_volatility = volatility * 0.30
                self.damper_counter_torque_nm = round(wind * 14200.0, 1)
                mitigation_action = f"TMD Active: 660-Ton Damper countered {self.damper_counter_torque_nm:,.0f} N·m sway. Build safe."
                daily_rise *= 0.85
            else:
                # Early stage high volatility: Cranes lock down, work moves to subterranean/indoor core
                mitigation_action = "High Wind Lockout: Transitioned build to interior core & wind tunnel testing."
                daily_rise *= 0.50
                self.structural_health = max(90.0, self.structural_health - 0.2)
        else:
            self.damper_counter_torque_nm = 0
            daily_rise *= 1.10 # Clear weather bonus

        self.current_height = min(self.target_height, self.current_height + daily_rise)
        self.built_floors = min(self.total_floors, int((self.current_height / self.target_height) * self.total_floors))

        log_entry = {
            "day": day,
            "phase": phase,
            "weather": weather,
            "height_meters": round(self.current_height, 1),
            "built_floors": self.built_floors,
            "structural_health_pct": round(self.structural_health, 1),
            "damper_active": self.damper_active,
            "mitigation_action": mitigation_action,
            "stamps": dict(self.compliance_stamps)
        }
        self.daily_logs.append(log_entry)
        return log_entry

def run_365_simulation(output_file="daily_weather_forecast_365.json", animate=False):
    builder = SkyscraperBuilder()
    print(f"\n{BOLD}{GOLD}╔══════════════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{GOLD}║              THE SYNOPTIC SPIRE // 365-DAY VOLATILITY & RESILIENCE ENGINE            ║{RESET}")
    print(f"{BOLD}{GOLD}║       Target Height: 828m | Tuned Mass Damper: Active | Full Legal Compliance        ║{RESET}")
    print(f"{BOLD}{GOLD}╚══════════════════════════════════════════════════════════════════════════════════════╝{RESET}\n")

    for day in range(1, 366):
        weather = generate_daily_weather(day)
        log = builder.iterate_day(weather)

        # Print milestones and quarterly progress
        if day in [1, 60, 90, 150, 180, 250, 270, 320, 365] or (day % 30 == 0):
            h = log["height_meters"]
            fl = log["built_floors"]
            w = weather["condition"]
            vol = weather["volatility_index_pct"]
            
            vol_color = GREEN if vol < 30 else (YELLOW if vol < 60 else RED)
            print(f"  {BOLD}DAY {day:03d}/365{RESET} | Height: {CYAN}{h:6.1f}m{RESET} ({fl:03d} fl) | Weather: {w[:24]:<24} | Volatility: {vol_color}{vol:5.1f}%{RESET}")
            print(f"           ↳ {DIM}{log['phase']}{RESET}")
            print(f"           ↳ {GOLD}{log['mitigation_action']}{RESET}\n")
            
            if animate:
                time.sleep(0.08)

    # Save full 365-day JSON artifact
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "project": "The Synoptic Spire",
            "architect": "[PT:AC] Andy Kieckhefer",
            "target_height_m": builder.target_height,
            "final_height_m": round(builder.current_height, 1),
            "final_floors": builder.built_floors,
            "structural_durability_pct": round(builder.structural_health, 1),
            "legal_compliance_seals": builder.compliance_stamps,
            "days_simulated": 365,
            "daily_logs": builder.daily_logs
        }, f, indent=2)

    print(f"{BOLD}{GREEN}✔ 365-Day Volatility Simulation Complete! Final Height: {builder.current_height:.1f}m / 163 Floors.{RESET}")
    print(f"{BOLD}{GREEN}✔ Official Occupancy Certificate Issued under EU AI Act & NIST AI RMF 1.0!{RESET}")
    print(f"  Saved full telemetry audit to: {output_file}\n")

def main():
    parser = argparse.ArgumentParser(description="365-Day Daily Weather & Skyscraper Volatility Engine")
    parser.add_argument("--out", default="daily_weather_forecast_365.json", help="Output JSON path")
    parser.add_argument("--animate", action="store_true", help="Slow print animation")
    args = parser.parse_args()

    run_365_simulation(output_file=args.out, animate=args.animate)

if __name__ == "__main__":
    main()
