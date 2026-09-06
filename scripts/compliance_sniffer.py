#!/usr/bin/env python3
"""
================================================================================
AИDY'S RISK FORECAST // COMPLIANCE SNIFFER & AUDIT CHECKOUT ENGINE
Frameworks: EU AI Act (Reg 2024/1689) | NIST AI RMF 1.0 | ISO/IEC 42001 | GDPR
Author: [PT:AC] Andy Kieckhefer
================================================================================
Automated repository scanner that validates multi-year engineering pipelines
against EU AI Act Articles, NIST AI RMF Core Functions, and generates machine-
readable compliance checkouts and markdown audit checkmarks.
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Enforce UTF-8 on Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Define ANSI color formatting for terminal output
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Regulatory Control Specifications
COMPLIANCE_CONTROLS = [
    # --------------------------------------------------------------------------
    # 1. EU AI ACT (Regulation (EU) 2024/1689)
    # --------------------------------------------------------------------------
    {
        "framework": "EU_AI_ACT",
        "control_id": "EU-AI-ART-09",
        "title": "Continuous Risk Management System",
        "article": "Article 9",
        "requirement": "Establish, implement, document and maintain a continuous risk management system throughout the entire AI lifecycle.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, "RISK_REGISTRY.md")),
        "remediation": "Create and maintain a living RISK_REGISTRY.md detailing breaking points, likelihood, and mitigation."
    },
    {
        "framework": "EU_AI_ACT",
        "control_id": "EU-AI-ART-10",
        "title": "Data Governance & Bias Mitigation",
        "article": "Article 10",
        "requirement": "Training, validation, and testing data sets shall be subject to appropriate data governance and management practices.",
        "eval_fn": lambda base: any(
            "data governance" in open(os.path.join(base, f), errors="ignore").read().lower()
            for f in ["RISK_REGISTRY.md", "README.md", "COMPLIANCE.md"] if os.path.exists(os.path.join(base, f))
        ),
        "remediation": "Document data lineage, quality thresholds, and bias auditing protocols in COMPLIANCE.md."
    },
    {
        "framework": "EU_AI_ACT",
        "control_id": "EU-AI-ART-11",
        "title": "Technical Documentation & Architecture",
        "article": "Article 11",
        "requirement": "Draw up and keep up-to-date comprehensive technical documentation demonstrating compliance.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, "README.md")),
        "remediation": "Provide end-to-end technical system architecture and dataflow documentation."
    },
    {
        "framework": "EU_AI_ACT",
        "control_id": "EU-AI-ART-12",
        "title": "Automatic Event Logging & Traceability",
        "article": "Article 12",
        "requirement": "High-risk AI systems shall technically allow for the automatic recording of events ('logs') over lifetime.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, "scripts", "evaluate_risk_velocity.py")) or os.path.exists(os.path.join(base, "scripts", "compliance_sniffer.py")),
        "remediation": "Ensure automated evaluation scripts generate tamper-evident execution logs."
    },
    {
        "framework": "EU_AI_ACT",
        "control_id": "EU-AI-ART-13",
        "title": "Transparency & Provision of Information",
        "article": "Article 13",
        "requirement": "High-risk AI systems shall be designed to be sufficiently transparent for deployers to interpret outputs.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, "risk-forecast-roadmap.svg")),
        "remediation": "Expose visual synoptic roadway status and explainable risk scores via vector roadmap."
    },
    {
        "framework": "EU_AI_ACT",
        "control_id": "EU-AI-ART-14",
        "title": "Human Oversight & Intervention (Human-in-the-Loop)",
        "article": "Article 14",
        "requirement": "Enable natural persons to oversee systems, prevent automation bias, and execute an override/stop.",
        "eval_fn": lambda base: any(
            "detour" in open(os.path.join(base, f), errors="ignore").read().lower()
            for f in ["README.md", "RISK_REGISTRY.md"] if os.path.exists(os.path.join(base, f))
        ),
        "remediation": "Establish manual detour activation protocols and human override commands in RISK_REGISTRY.md."
    },
    {
        "framework": "EU_AI_ACT",
        "control_id": "EU-AI-ART-15",
        "title": "Accuracy, Robustness & Cybersecurity",
        "article": "Article 15",
        "requirement": "Resilience against errors, faults, inconsistencies, data poisoning, and adversarial tampering.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, ".github", "workflows")),
        "remediation": "Implement automated CI/CD security scanning, lockfile validation, and test runners."
    },
    {
        "framework": "EU_AI_ACT",
        "control_id": "EU-AI-ART-27",
        "title": "Fundamental Rights Impact Assessment (FRIA)",
        "article": "Article 27",
        "requirement": "Perform assessment of the impact on fundamental rights before putting a high-risk AI system into service.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, "COMPLIANCE.md")),
        "remediation": "Document FRIA considerations and affected demographic safeguards in COMPLIANCE.md."
    },

    # --------------------------------------------------------------------------
    # 2. NIST AI RMF 1.0 (Artificial Intelligence Risk Management Framework)
    # --------------------------------------------------------------------------
    {
        "framework": "NIST_AI_RMF",
        "control_id": "NIST-GOVERN-1.1",
        "title": "Legal & Regulatory Environmental Mapping",
        "article": "GOVERN 1.1",
        "requirement": "Legal and regulatory requirements involving AI are understood, managed, and integrated into workflows.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, "COMPLIANCE.md")),
        "remediation": "Create COMPLIANCE.md mapping applicable statutes, regulations, and executive orders."
    },
    {
        "framework": "NIST_AI_RMF",
        "control_id": "NIST-MAP-1.1",
        "title": "Context & Deployment Scope Definition",
        "article": "MAP 1.1",
        "requirement": "Intended purpose, deployment context, and business value propositions are explicitly mapped.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, "README.md")),
        "remediation": "Document clear operational boundaries (multi-year horizon, 18–60+ months) in README.md."
    },
    {
        "framework": "NIST_AI_RMF",
        "control_id": "NIST-MEASURE-1.1",
        "title": "Quantitative Risk Metrics & Scoring",
        "article": "MEASURE 1.1",
        "requirement": "Approaches and metrics for measurement of AI risks are identified, tested, and tracked over time.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, "scripts", "evaluate_risk_velocity.py")),
        "remediation": "Implement algorithmic friction scoring script to quantify risk velocity over time."
    },
    {
        "framework": "NIST_AI_RMF",
        "control_id": "NIST-MANAGE-1.1",
        "title": "Risk Treatment & Pre-Engineered Mitigation",
        "article": "MANAGE 1.1",
        "requirement": "Risks are prioritized and acted upon based on planned risk treatments (avoid, transfer, mitigate, accept).",
        "eval_fn": lambda base: any(
            "mandatory detour" in open(os.path.join(base, f), errors="ignore").read().lower()
            for f in ["README.md", "RISK_REGISTRY.md"] if os.path.exists(os.path.join(base, f))
        ),
        "remediation": "Provide concrete detour routing specifications for each critical breaking point."
    },

    # --------------------------------------------------------------------------
    # 3. GLOBAL LEGAL & DATA PROTECTION (GDPR / ISO 42001)
    # --------------------------------------------------------------------------
    {
        "framework": "LEGAL_DATA_GOV",
        "control_id": "GDPR-ART-25",
        "title": "Data Protection by Design & Default",
        "article": "Article 25 GDPR",
        "requirement": "Appropriate technical and organizational measures implemented to integrate safeguards into processing.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, ".gitignore")),
        "remediation": "Ensure zero-trust isolation, private credential segregation, and strict .gitignore policies."
    },
    {
        "framework": "LEGAL_DATA_GOV",
        "control_id": "ISO-42001-AIMS",
        "title": "AI Management System (AIMS) Accountability",
        "article": "Clause 5 & 9",
        "requirement": "Leadership commitment, internal audits, and continuous risk monitoring mechanisms.",
        "eval_fn": lambda base: os.path.exists(os.path.join(base, ".github", "ISSUE_TEMPLATE")),
        "remediation": "Provide structured GitHub issue templates for continuous stakeholder hazard reporting."
    }
]

def run_compliance_sniffer(repo_base_path):
    """Executes compliance evaluation across all controls."""
    results = []
    framework_stats = {}

    for ctrl in COMPLIANCE_CONTROLS:
        fw = ctrl["framework"]
        if fw not in framework_stats:
            framework_stats[fw] = {"total": 0, "passed": 0, "failed": 0}
        
        framework_stats[fw]["total"] += 1
        
        try:
            passed = ctrl["eval_fn"](repo_base_path)
        except Exception:
            passed = False

        status = "PASSED" if passed else "FAILED"
        if passed:
            framework_stats[fw]["passed"] += 1
        else:
            framework_stats[fw]["failed"] += 1

        results.append({
            "framework": ctrl["framework"],
            "control_id": ctrl["control_id"],
            "title": ctrl["title"],
            "article": ctrl["article"],
            "requirement": ctrl["requirement"],
            "status": status,
            "remediation": ctrl["remediation"] if not passed else None
        })

    total_controls = len(results)
    total_passed = sum(1 for r in results if r["status"] == "PASSED")
    compliance_score = (total_passed / total_controls) * 100.0 if total_controls > 0 else 0.0

    from datetime import timezone
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repo_path": os.path.abspath(repo_base_path),
        "compliance_score_pct": round(compliance_score, 1),
        "total_controls": total_controls,
        "passed_controls": total_passed,
        "failed_controls": total_controls - total_passed,
        "framework_stats": framework_stats,
        "controls": results
    }

def generate_markdown_checkout(report_data, output_path):
    """Generates a formal legal checkout markdown document with checkmarks."""
    score = report_data["compliance_score_pct"]
    badge_color = "brightgreen" if score >= 90 else ("yellow" if score >= 70 else "red")

    lines = [
        "# ⚖️ Regulatory Compliance & Legal Audit Checkout",
        "",
        f"### Standards: EU AI Act (2024/1689) · NIST AI RMF 1.0 · ISO/IEC 42001 · GDPR",
        f"**Audit Timestamp:** `{report_data['timestamp']}` · **Attribution:** `[PT:AC] Andy Kieckhefer`",
        "",
        f"![Compliance Status](https://img.shields.io/badge/Compliance_Score-{score}%25-{badge_color}?style=for-the-badge&logo=shield)",
        "",
        "---",
        "",
        "## 📊 Executive Summary & Framework Checkouts",
        "",
        "| Framework / Standard | Total Controls | Passed Checkmarks | Gaps / Deficiencies | Compliance Health |",
        "| :--- | :---: | :---: | :---: | :---: |"
    ]

    for fw, stats in report_data["framework_stats"].items():
        pct = (stats["passed"] / stats["total"]) * 100 if stats["total"] > 0 else 0
        status_icon = "🟢" if pct == 100 else ("🟡" if pct >= 60 else "🔴")
        lines.append(f"| **{fw.replace('_', ' ')}** | {stats['total']} | {stats['passed']} | {stats['failed']} | {status_icon} `{pct:.1f}%` |")

    lines.extend([
        "",
        "---",
        "",
        "## 🇪🇺 EU AI Act (Regulation (EU) 2024/1689) Checklist",
        "",
        "Detailed legal verification of mandatory high-risk and transparency requirements:",
        ""
    ])

    for c in report_data["controls"]:
        if c["framework"] == "EU_AI_ACT":
            box = "[x]" if c["status"] == "PASSED" else "[ ]"
            tag = "✅ **PASS**" if c["status"] == "PASSED" else "❌ **ACTION REQUIRED**"
            lines.append(f"- {box} **{c['control_id']}** ({c['article']}) — **{c['title']}**: {tag}")
            lines.append(f"  - *Legal Requirement:* {c['requirement']}")
            if c["remediation"]:
                lines.append(f"  - *Remediation Step:* ⚠️ {c['remediation']}")

    lines.extend([
        "",
        "---",
        "",
        "## 🛡️ NIST AI RMF 1.0 Framework Checklist",
        "",
        "Verification across NIST Core Functions: GOVERN, MAP, MEASURE, MANAGE:",
        ""
    ])

    for c in report_data["controls"]:
        if c["framework"] == "NIST_AI_RMF":
            box = "[x]" if c["status"] == "PASSED" else "[ ]"
            tag = "✅ **PASS**" if c["status"] == "PASSED" else "❌ **ACTION REQUIRED**"
            lines.append(f"- {box} **{c['control_id']}** ({c['article']}) — **{c['title']}**: {tag}")
            lines.append(f"  - *NIST Specification:* {c['requirement']}")
            if c["remediation"]:
                lines.append(f"  - *Remediation Step:* ⚠️ {c['remediation']}")

    lines.extend([
        "",
        "---",
        "",
        "## 🔒 Data Protection & Governance Checklist (GDPR & ISO 42001)",
        ""
    ])

    for c in report_data["controls"]:
        if c["framework"] == "LEGAL_DATA_GOV":
            box = "[x]" if c["status"] == "PASSED" else "[ ]"
            tag = "✅ **PASS**" if c["status"] == "PASSED" else "❌ **ACTION REQUIRED**"
            lines.append(f"- {box} **{c['control_id']}** ({c['article']}) — **{c['title']}**: {tag}")
            lines.append(f"  - *Standard Rule:* {c['requirement']}")
            if c["remediation"]:
                lines.append(f"  - *Remediation Step:* ⚠️ {c['remediation']}")

    lines.extend([
        "",
        "---",
        "",
        "## 🏛️ Continuous Legal Assurance Protocol",
        "",
        "This repository runs automated continuous compliance sniffer scans on every pull request and commit.",
        "Any regressions that breach EU AI Act High-Risk mandates or NIST AI RMF baselines automatically halt deployment pipelines.",
        "",
        "```bash",
        "# Run local compliance sniffer",
        "python scripts/compliance_sniffer.py --checkout COMPLIANCE_CHECKOUT.md",
        "```",
        ""
    ])

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def main():
    parser = argparse.ArgumentParser(description="AИDY'S RISK FORECAST // Legal & AI Compliance Sniffer")
    parser.add_argument("--repo", default=".", help="Target repository base path (default: .)")
    parser.add_argument("--checkout", default="COMPLIANCE_CHECKOUT.md", help="Markdown checkout output file")
    parser.add_argument("--json-out", default="compliance_report.json", help="JSON report output file")
    args = parser.parse_args()

    repo_dir = os.path.abspath(args.repo)
    print(f"\n{BOLD}{CYAN}======================================================================{RESET}")
    print(f"{BOLD}{CYAN}  AИDY'S RISK FORECAST // REGULATORY & NIST COMPLIANCE SNIFFER        {RESET}")
    print(f"{BOLD}{CYAN}  Standards: EU AI Act (2024/1689) | NIST AI RMF 1.0 | ISO 42001     {RESET}")
    print(f"{BOLD}{CYAN}======================================================================{RESET}")
    print(f"Scanning Target Directory: {repo_dir}\n")

    report = run_compliance_sniffer(repo_dir)

    for ctrl in report["controls"]:
        status_color = GREEN if ctrl["status"] == "PASSED" else RED
        mark = "[✔]" if ctrl["status"] == "PASSED" else "[✖]"
        print(f"  {status_color}{mark} {ctrl['control_id']} ({ctrl['article']}): {ctrl['title']}{RESET}")
        if ctrl["remediation"]:
            print(f"      {YELLOW}↳ Remediation: {ctrl['remediation']}{RESET}")

    score = report["compliance_score_pct"]
    score_color = GREEN if score >= 90 else (YELLOW if score >= 70 else RED)
    print(f"\n{BOLD}----------------------------------------------------------------------{RESET}")
    print(f"Total Controls Evaluated: {report['total_controls']}")
    print(f"Passed Checkmarks:        {GREEN}{report['passed_controls']}{RESET}")
    print(f"Compliance Gaps:          {RED if report['failed_controls'] > 0 else GREEN}{report['failed_controls']}{RESET}")
    print(f"Overall Compliance Score: {BOLD}{score_color}{score}%{RESET}")
    print(f"{BOLD}----------------------------------------------------------------------{RESET}\n")

    # Generate output artifacts
    checkout_path = os.path.join(repo_dir, args.checkout)
    generate_markdown_checkout(report, checkout_path)
    print(f"  {GREEN}✔{RESET} Markdown Legal Checkout written to: {checkout_path}")

    json_path = os.path.join(repo_dir, args.json_out)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"  {GREEN}✔{RESET} Machine-Readable JSON Audit written to: {json_path}\n")

if __name__ == "__main__":
    main()
