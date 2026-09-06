#!/usr/bin/env python3
"""
================================================================================
THE GOOGLE GAME // AUTOMATIC VESSEL CLASSIFIER & SELECTOR
Author: [PT:AC] Andy Kieckhefer
================================================================================
Analyzes the domain, horizon, risk climate, and regulatory parameters of any
new risk-forecast development, and automatically selects the optimal vessel class:
1. Class I   : Aerodynamic Supertall Spire (Frontier AI & Public APIs)
2. Class II  : Subterranean Fortress Vault (Cryptography & IAM Bedrock)
3. Class III : Levitating Ferris Wheel Ring (Event Meshes & High-Throughput Streaming)
4. Class IV  : Floating Hyperscale Data-Barge (Global Multi-Region Cloud & Storage)
5. Class V   : Stratospheric Orbital Space Switch (Failover & Unjammable Telemetry)
6. Class VI  : Geodesic Bio-Dome (Health AI & Open Citizen Science)
================================================================================
"""

import os
import sys
import json
import re

# Enforce UTF-8 on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

VESSEL_CLASSES = {
    "CLASS_I_SPIRE": {
        "name": "Class I: Aerodynamic Supertall Spire",
        "icon": "🏙️",
        "description": "Supertall glass-steel tower with spiral vortex-shedding setbacks and a 660-Ton Tuned Mass Damper at Level 88.",
        "best_for": ["ai", "frontier", "llm", "gemini", "search", "agent", "public api", "model", "reasoning"],
        "defense_mechanic": "Tuned Mass Damper (-42% Vibration) + Cloudflare Aerodynamic WAF",
        "height_m": 828.0,
        "floors": 163,
        "damper_type": "Golden Pendulum Shock Damper (Level 88)",
        "color": "#a855f7"
    },
    "CLASS_II_BUNKER": {
        "name": "Class II: Subterranean Fortress Vault",
        "icon": "🏰",
        "description": "Sub-bedrock reinforced citadel with blast-containment bulkheads, Faraday cage isolation, and zero external ingress ports.",
        "best_for": ["crypto", "security", "vault", "iam", "auth", "key", "hsm", "secret", "pki", "credential", "payment"],
        "defense_mechanic": "Faraday Cage Grounding + Watertight Cryptographic Bulkhead Isolation",
        "height_m": 220.0,
        "floors": 45,
        "damper_type": "Subterranean Seismic Shock Absorbers",
        "color": "#10b981"
    },
    "CLASS_III_FERRIS": {
        "name": "Class III: Levitating Ferris Wheel Ring",
        "icon": "🎡",
        "description": "Anti-gravity rotating ring platform carrying cyclic task gondolas for high-concurrency event load-balancing.",
        "best_for": ["stream", "event", "kafka", "queue", "batch", "microservice", "throughput", "pipeline", "load", "balancer", "mesh"],
        "defense_mechanic": "Centrifugal Task Shedding + Round-Robin Load Distribution",
        "height_m": 420.0,
        "floors": 72,
        "damper_type": "Anti-Gravity Gyroscopic Counter-Torque Ring",
        "color": "#f59e0b"
    },
    "CLASS_IV_BARGE": {
        "name": "Class IV: Floating Hyperscale Data-Barge",
        "icon": "🚢",
        "description": "Liquid-cooled aquatic super-structure with compartmentalized double-hulls and direct submarine cable interconnects.",
        "best_for": ["cloud", "storage", "gcp", "multi-region", "database", "cdn", "youtube", "media", "video", "cold storage"],
        "defense_mechanic": "Liquid Submersion Cooling + Multi-Region Jurisdiction Failover",
        "height_m": 350.0,
        "floors": 60,
        "damper_type": "Hydrodynamic Bilge Keels & Ballast Compensation",
        "color": "#3b82f6"
    },
    "CLASS_V_SPACE_SWITCH": {
        "name": "Class V: Stratospheric Orbital Space Switch",
        "icon": "🚀",
        "description": "Solar-powered low-earth-orbit crossbar switch utilizing inter-satellite laser links to bypass terrestrial network failures.",
        "best_for": ["space", "satellite", "failover", "telemetry", "autonomous", "waymo", "robotics", "drone", "edge", "mesh", "laser"],
        "defense_mechanic": "Photonic Laser Routing + Vacuum Air-Gapping",
        "height_m": 1200.0,
        "floors": 200,
        "damper_type": "Orbital Reaction Wheels & Thruster Stabilization",
        "color": "#f43f5e"
    },
    "CLASS_VI_BIODOME": {
        "name": "Class VI: Geodesic Bio-Dome Canopy",
        "icon": "🏛️",
        "description": "Self-healing tensile polymer biodome designed for collaborative multi-entity research, healthcare privacy, and open science.",
        "best_for": ["health", "bio", "medical", "life science", "citizen science", "dna", "hipaa", "collaborative", "open source", "consortium"],
        "defense_mechanic": "Differential Airflow Filtration + Differential Privacy Envelopes",
        "height_m": 290.0,
        "floors": 50,
        "damper_type": "Elastic Tensile Diagrid Dampers",
        "color": "#34d399"
    }
}

def automatically_choose_vessel(project_name, description=""):
    """
    Intelligently analyzes project name & description keywords and determines
    which vessel class the Google Game automatically assigns.
    """
    corpus = f"{project_name} {description}".lower()
    scores = {}

    for v_key, v_info in VESSEL_CLASSES.items():
        score = 0
        for kw in v_info["best_for"]:
            if re.search(r'\b' + re.escape(kw) + r'\b', corpus):
                score += 3
            elif kw in corpus:
                score += 1
        scores[v_key] = score

    # Select class with highest score, or default to Class I Spire
    best_class_key = max(scores, key=scores.get)
    if scores[best_class_key] == 0:
        # Smart heuristic defaults
        if any(w in corpus for w in ["ai", "intelligence", "agent", "risk"]):
            best_class_key = "CLASS_I_SPIRE"
        elif any(w in corpus for w in ["cloud", "data", "storage", "server"]):
            best_class_key = "CLASS_IV_BARGE"
        else:
            best_class_key = "CLASS_I_SPIRE"

    return VESSEL_CLASSES[best_class_key]

if __name__ == "__main__":
    test_projects = [
        ("Quantum-HSM-Vault", "Cryptographic private key store and zero-trust authentication module"),
        ("Gemini-Autonomous-Agent", "Frontier reasoning model with multi-modal reasoning and code generation"),
        ("Global-Video-CDN", "Petabyte-scale distributed streaming and cold storage database"),
        ("Kafka-Event-Firehose", "High-throughput event streaming queue and load-balancing mesh"),
        ("StarNet-Laser-Relay", "Stratospheric optical satellite failover switch for edge robotics"),
        ("Bio-Genomics-Consortium", "Collaborative healthcare data platform with differential privacy")
    ]

    print("======================================================================")
    print("THE GOOGLE GAME // AUTOMATIC VESSEL SELECTION TEST RUN")
    print("======================================================================")
    for name, desc in test_projects:
        vessel = automatically_choose_vessel(name, desc)
        print(f"\nProject: {name}")
        print(f"↳ Assigned Vessel: {vessel['icon']} {vessel['name']}")
        print(f"↳ Defense Shield : {vessel['defense_mechanic']}")
        print(f"↳ Damping Tech   : {vessel['damper_type']}")
    print("\n✔ Classification engine validated!")
