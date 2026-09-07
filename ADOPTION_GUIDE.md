# 📘 GOOGLE GILDAN // PRACTICAL ADOPTION GUIDE
## How Any Engineering Squad Adopts Civil Risk-Forecasting & Measures Net Risk Drag
**Platform:** `GOOGLE GILDAN` · **Engine:** `RISK-FORECAST`  
**Master Architect:** `[PT:AC] Andy Kieckhefer`  
**Conformity:** EU AI Act · NIST AI RMF 1.0 · ISO/IEC 42001 · DoD UFC 4-010-01  

---

## 🚀 3-Minute Quick Adoption

Google Gildan is designed to be adopted into any software repository within 3 minutes, replacing vague status meetings with verifiable structural civil metrics:

### Step 1: Install or Clone Google Gildan Tooling
```bash
# Add as a dev dependency or clone adjacent to your repo
pip install google-gildan  # or clone scripts/
```

### Step 2: Add `gildan.config.json` to Your Repository Root
Create a minimal declaration file in your project:
```json
{
  "$schema": "https://raw.githubusercontent.com/GrowwithGoogle/Google-Gildan/main/schema/gildan.schema.json",
  "project_name": "Payment-Ingress-Core",
  "landscape_zone": "suburban",
  "vessel_class": "Class 3: Aerodynamic Monolith",
  "slos": {
    "max_acceptable_net_risk_pct": 10.0,
    "target_mttr_minutes": 60,
    "ci_feedback_max_seconds": 90
  },
  "contacts": {
    "lead_architect": "alice@google.com",
    "sre_steward": "bob@google.com"
  }
}
```

### Step 3: Run the Automated Civil Structural Inspection
```bash
# Audits scaffolding, windows, lifts, and stairwells
python scripts/adopt_project.py inspect . --submit "Payment-Ingress-Core"
```

### Step 4: Add to Your CI/CD Pipeline (GitHub Actions or Cloud Build)
Add this step to your `.github/workflows/ci.yml`:
```yaml
- name: Google Gildan Civil Structural Audit
  run: |
    python scripts/adopt_project.py inspect . --json-out gildan_permit.json
    python scripts/adopt_project.py check-risk --max-risk 10.0
```

---

## 🧮 The Net Risk Drag Scoring Algorithm

Your project's **Net Risk Drag Score** is computed deterministically from your repository artifacts:

$$\text{Net Risk Score} = 100.0 - \left( 0.25 \cdot S + 0.25 \cdot W + 0.25 \cdot L + 0.25 \cdot E \right)$$

*   **$S$ (Scaffolding):** Build hermeticity (lockfiles), CI feedback cadence (<90s = 100%), mock isolation.
*   **$W$ (Windows):** API contracts (OpenAPI / Protobuf), WAF edge rules, CSP headers, zero-trust secrets hygiene.
*   **$L$ (Lifts):** Vertical throughput, asynchronous pub/sub queues, rate limiters, connection pool safety.
*   **$E$ (Stairwells / Egress):** Out-of-band DR runbooks, chaos wargaming, backup failover circuits.

### Risk Tiers
*   🟢 **0.0% – 5.0% Net Risk:** **Titan Bedrock Standard.** Maximum resilience, immune to external gale shears.
*   🟡 **5.1% – 15.0% Net Risk:** **Tempered Metropolis Spire.** Level 88 Tuned Mass Damper active, safe for production.
*   🟠 **15.1% – 30.0% Net Risk:** **Reinforced Concrete.** Functional but experiences noticeable drag during regulatory shifts or traffic spikes.
*   🔴 **30.1%+ Net Risk:** **Unanchored Timber / High Hazard.** Immediate architectural retrofitting required.

---

## 🏆 The Risk-Averse Leaderboard
Projects achieving **< 5.0% Net Risk Score** qualify for the **Google Gildan Gold Seal of Generational Durability** and are entered into the global leaderboard ([`LEADERBOARD.md`](LEADERBOARD.md)).
