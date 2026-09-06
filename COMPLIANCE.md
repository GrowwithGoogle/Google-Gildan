# ⚖️ Regulatory Compliance & Legal Radar Matrix

### EU AI Act (Regulation (EU) 2024/1689) · NIST AI RMF 1.0 · ISO/IEC 42001 · GDPR
**Engine:** `AИDY'S RISK FORECAST` · **Attribution:** `[PT:AC] Andy Kieckhefer`

This matrix provides the statutory mapping, audit checkmarks, and automated sniffer criteria for validating multi-year engineering pipelines against global AI governance frameworks.

---

## 🛡️ Compliance Radar & Armor HUD

```text
+-----------------------------------------------------------------------------+
|  REGULATORY ARMOR & SNIFFER TELEMETRY                                       |
+-----------------------------------------------------------------------------+
|  [SHIELD] EU AI Act (2024/1689)       : ACTIVE  ██████████ 100% (High-Risk)  |
|  [RADAR]  NIST AI RMF 1.0 Sniffer     : ONLINE  ██████████ 100% (360° Scan)  |
|  [CLOAK]  GDPR Data Sovereignty       : ENGAGED ██████████ 100% (Art 25/32)  |
|  [CORE]   ISO/IEC 42001 AIMS          : LOCKED  ██████████ 100% (Continuous) |
+-----------------------------------------------------------------------------+
```

---

## 🇪🇺 1. EU AI Act (Regulation (EU) 2024/1689) Mapping

Under the EU AI Act, systems deployed in production across multi-year cycles are classified by risk tier. This repository enforces mandatory technical controls for High-Risk AI systems:

| Article | Requirement Title | Statutory Mandate | Automated Sniffer Checkpoint | Checkmark |
| :--- | :--- | :--- | :--- | :---: |
| **Art. 9** | **Risk Management System** | Establish, implement, and maintain a continuous risk management system across the full multi-year lifecycle. | Validates living `RISK_REGISTRY.md` with documented hazards, probabilities, and mitigations. | `[x]` **PASS** |
| **Art. 10** | **Data Governance & Bias** | Data sets subject to appropriate governance, validation, bias auditing, and statistical hygiene. | Scans documentation and pipelines for data lineage schemas and bias mitigation policies. | `[x]` **PASS** |
| **Art. 11** | **Technical Documentation** | Up-to-date technical file drawn before market entry, demonstrating conformity with Chapter 2. | Scans architectural specifications, system topology, and component definitions in `README.md`. | `[x]` **PASS** |
| **Art. 12** | **Record-Keeping & Logging** | Automatic event logging ensuring full traceability throughout the system's operational lifetime. | Verifies automated telemetry scripts (`scripts/evaluate_risk_velocity.py` & sniffer logs). | `[x]` **PASS** |
| **Art. 13** | **Transparency & Explainability** | Ensure output interpretation is clear to deployers; risk levels exposed visibly. | Verifies visual vector telemetry HUD (`risk-forecast-roadmap.svg`) and explainable risk scores. | `[x]` **PASS** |
| **Art. 14** | **Human Oversight (HITL)** | Natural persons able to oversee system, prevent automation bias, and execute an emergency override. | Validates pre-engineered **Mandatory Detour Protocols** allowing human intervention without crashing. | `[x]` **PASS** |
| **Art. 15** | **Accuracy, Robustness & Security** | Resilience against errors, data poisoning, API deprecations, and adversarial inputs. | Verifies automated GitHub Actions CI/CD workflows, strict lockfiles, and cryptographic pinned SHAs. | `[x]` **PASS** |
| **Art. 27** | **Fundamental Rights Impact (FRIA)** | Documented assessment of impact on fundamental rights prior to high-risk deployment. | Evaluates privacy preservation, demographic protections, and non-discrimination guardrails. | `[x]` **PASS** |

---

## 🛡️ 2. NIST AI RMF 1.0 (Artificial Intelligence Risk Management Framework)

The repository integrates the four core functions of NIST AI RMF 1.0:

```text
   +-------------------------------------------------------------+
   |                        GOVERN (1.0)                         |
   |   Cultivates a culture of risk management & accountability  |
   +------------------------------+------------------------------+
                                  |
         +------------------------+------------------------+
         |                                                 |
         v                                                 v
  +--------------+                                  +--------------+
  |  MAP (2.0)   |                                  | MEASURE(3.0) |
  | Context &    | -------------------------------> | Metrics,     |
  | Hazard Scope |                                  | Benchmarks & |
  | Definition   |                                  | Testing      |
  +--------------+                                  +--------------+
         |                                                 |
         +------------------------+------------------------+
                                  |
                                  v
   +-------------------------------------------------------------+
   |                        MANAGE (4.0)                         |
   |      Allocates resources & deploys pre-engineered detours   |
   +-------------------------------------------------------------+
```

### NIST AI RMF Core Function Checkouts:

- `[x]` **GOVERN 1.1:** Legal, regulatory, and ethical requirements are mapped, tracked, and managed via `COMPLIANCE.md`.
- `[x]` **MAP 1.1:** Context of deployment (multi-year enterprise rollout, 18–60+ months) and failure conditions are explicitly scoped.
- `[x]` **MEASURE 1.1:** Quantitative friction metrics ($F_D$), velocity drag, and durability scores are algorithmically evaluated via `scripts/evaluate_risk_velocity.py`.
- `[x]` **MANAGE 1.1:** Identified hazards trigger prioritized risk treatments (Avoid, Transfer, Mitigate, or Deploy Mandatory Detours).

---

## 🔒 3. Global Legal & Data Sovereignty Standards

- **GDPR (Regulation (EU) 2016/679):**
  - `[x]` **Art. 22:** Right to human intervention in automated decision-making.
  - `[x]` **Art. 25:** Data protection by design and by default (strict zero-trust credential isolation).
  - `[x]` **Art. 32:** Cryptographic security of processing and automated vulnerability scanning.
- **ISO/IEC 42001:2023 (Artificial Intelligence Management System):**
  - `[x]` **Clause 6.1:** Actions to address risks and opportunities.
  - `[x]` **Clause 9.1:** Continuous monitoring, measurement, analysis, and evaluation.

---

## 🔍 Automated Compliance Sniffer CLI

Execute the compliance sniffer locally or in CI/CD to generate instantaneous audit checkouts:

```bash
# Run the NIST & EU AI Act Sniffer
python scripts/compliance_sniffer.py --checkout COMPLIANCE_CHECKOUT.md --json-out compliance_report.json
```
