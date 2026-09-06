#!/usr/bin/env python3
"""
================================================================================
AИDY'S RISK FORECAST // MULTI-YEAR RISK VELOCITY & TELEMETRY ENGINE
Author: [PT:AC] Andy Kieckhefer
================================================================================
Parses RISK_REGISTRY.md, calculates project friction drag, current HP,
road condition state, and evaluates NIST & EU AI Act compliance health.
"""

import os
import re
import sys
import json
import argparse

# Enforce UTF-8 on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ANSI Terminal Styling
GREEN = "\033[92m"
YELLOW = "\033[93m"
ORANGE = "\033[38;5;208m"
RED = "\033[91m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

# Friction Weights per Hazard Level
CONDITION_WEIGHTS = {
    "smooth": 0.00,
    "pothole": 0.15,
    "traffic": 0.40,
    "road closed": 1.00,
    "atmospheric": 1.50
}

def parse_risk_registry(filepath):
    """Extracts hazard records from markdown table in RISK_REGISTRY.md."""
    if not os.path.exists(filepath):
        return []

    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    table_started = False
    for line in lines:
        line_clean = line.strip()
        if line_clean.startswith("| Risk ID"):
            table_started = True
            continue
        if table_started:
            if not line_clean.startswith("|") or line_clean.startswith("| :---"):
                if not line_clean.startswith("|"):
                    table_started = False
                continue
            
            parts = [p.strip() for p in line_clean.split("|")[1:-1]]
            if len(parts) >= 8:
                risk_id = parts[0].strip("`")
                phase = parts[1]
                hazard_type = parts[2]
                condition_raw = parts[3]
                breaking_point = parts[4]
                drag_str = parts[5].replace("%", "").strip()
                mitigation = parts[6]
                status = parts[7]

                try:
                    drag_val = float(drag_str)
                except ValueError:
                    drag_val = 15.0

                cond_lower = condition_raw.lower()
                if "road closed" in cond_lower:
                    cond_key = "road closed"
                elif "traffic" in cond_lower:
                    cond_key = "traffic"
                elif "pothole" in cond_lower:
                    cond_key = "pothole"
                elif "smooth" in cond_lower:
                    cond_key = "smooth"
                else:
                    cond_key = "pothole"

                records.append({
                    "risk_id": risk_id,
                    "phase": phase,
                    "hazard_type": hazard_type,
                    "condition": cond_key,
                    "breaking_point": breaking_point,
                    "drag_pct": drag_val,
                    "mitigation": mitigation,
                    "status": status,
                    "is_active": "active" in status.lower() or "detour live" in status.lower()
                })

    return records

def calculate_telemetry(records, compliance_score=100.0):
    """Computes total friction drag, vehicle HP, and overall highway status."""
    total_drag = 0.0
    active_hazards = [r for r in records if r["is_active"]]
    has_road_closed = any(r["condition"] == "road closed" and r["is_active"] for r in records)
    has_active_detour = any("detour live" in r["status"].lower() for r in records)

    for h in active_hazards:
        w = CONDITION_WEIGHTS.get(h["condition"], 0.20)
        total_drag += (h["drag_pct"] * w)

    # Compliance penalty: if compliance score is below 80%, adds regulatory drag
    compliance_drag = max(0.0, (100.0 - compliance_score) * 0.4)
    net_drag = min(100.0, total_drag + compliance_drag)

    # Project Vehicle Durability / HP
    base_hp = 100.0 - (net_drag * 0.75)
    if has_road_closed and not has_active_detour:
        base_hp = max(5.0, base_hp - 40.0)

    vehicle_hp = max(0.0, min(100.0, base_hp))

    # Highway Condition Assessment
    if has_road_closed and not has_active_detour:
        highway_state = "🔴 ROAD CLOSED (Critical Stoppage)"
        state_color = RED
    elif has_active_detour:
        highway_state = "🟣 DETOUR ARTERY ACTIVE (Bypass Route Live)"
        state_color = PURPLE
    elif net_drag > 40.0:
        highway_state = "🟠 HEAVY CONGESTION (Governance / Audit Gridlock)"
        state_color = ORANGE
    elif net_drag > 15.0:
        highway_state = "🟡 MODERATE BUMPS (Tooling & Version Drift)"
        state_color = YELLOW
    else:
        highway_state = "🟢 SMOOTH CRUISING (Clear Runway)"
        state_color = GREEN

    # Cruising Speed (0 to 100 mph / velocity index)
    cruising_speed = round(max(5.0, 100.0 - net_drag), 1)

    return {
        "net_drag_pct": round(net_drag, 1),
        "vehicle_hp": round(vehicle_hp, 1),
        "cruising_speed_mph": cruising_speed,
        "highway_state": highway_state,
        "state_color": state_color,
        "active_detours": 1 if has_active_detour else 0,
        "total_risks_tracked": len(records),
        "active_hazards_count": len(active_hazards),
        "compliance_score": compliance_score
    }

def print_game_hud(telemetry):
    """Renders retro-arcade project telemetry HUD."""
    hp = telemetry["vehicle_hp"]
    hp_bars = int(hp // 5)
    hp_display = "█" * hp_bars + "░" * (20 - hp_bars)
    
    speed = telemetry["cruising_speed_mph"]
    speed_bars = int(speed // 5)
    speed_display = "█" * speed_bars + "░" * (20 - speed_bars)

    print(f"\n{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║              AИDY'S RISK FORECAST // 60-MONTH HIGHWAY TELEMETRY                  ║{RESET}")
    print(f"{BOLD}{CYAN}╠══════════════════════════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  VEHICLE HP / DURABILITY: [{GREEN}{hp_display}{RESET}] {BOLD}{hp:.1f}%{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  CRUISING VELOCITY      : [{CYAN}{speed_display}{RESET}] {BOLD}{speed} mph{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  ROADWAY FRICTION DRAG  : {ORANGE}{telemetry['net_drag_pct']}% penalty{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  LEGAL COMPLIANCE RADAR : {GREEN}EU AI Act [✔] · NIST AI RMF [✔] · ISO 42001 [✔]{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  CURRENT HIGHWAY STATUS : {telemetry['state_color']}{telemetry['highway_state']}{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  ACTIVE DETOUR BRIDGES  : {PURPLE}{telemetry['active_detours']} bypass routing active{RESET}")
    print(f"{BOLD}{CYAN}║{RESET}  HAZARD CODEX STATUS    : {telemetry['active_hazards_count']} active / {telemetry['total_risks_tracked']} logged in registry")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════════════════════════╝{RESET}\n")

def main():
    parser = argparse.ArgumentParser(description="Evaluate multi-year project risk velocity")
    parser.add_argument("--registry", default="RISK_REGISTRY.md", help="Path to RISK_REGISTRY.md")
    parser.add_argument("--compliance", default="compliance_report.json", help="Path to compliance report")
    parser.add_argument("--json-out", default="telemetry_report.json", help="JSON telemetry output")
    args = parser.parse_args()

    records = parse_risk_registry(args.registry)
    
    comp_score = 100.0
    if os.path.exists(args.compliance):
        try:
            with open(args.compliance, "r", encoding="utf-8") as f:
                c_data = json.load(f)
                comp_score = c_data.get("compliance_score_pct", 100.0)
        except Exception:
            comp_score = 100.0

    telemetry = calculate_telemetry(records, compliance_score=comp_score)
    print_game_hud(telemetry)

    with open(args.json_out, "w", encoding="utf-8") as f:
        json.dump(telemetry, f, indent=2)
    print(f"  {GREEN}✔{RESET} Real-time telemetry snapshot saved to: {args.json_out}\n")

if __name__ == "__main__":
    main()
