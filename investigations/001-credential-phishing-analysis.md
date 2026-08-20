# Investigation 001 — Credential Phishing Analysis

**Status:** 🟡 Planned  
**Scenario type:** Simulated / Benign Training Sample

## Objective

Investigate a simulated credential-phishing email using a repeatable SOC triage workflow. The final report will document sender/header observations, suspicious-link analysis, extracted indicators, analyst reasoning, MITRE ATT&CK mapping where justified, severity, and response recommendations.

## Planned Analysis

- Review visible sender and reply-to information
- Inspect relevant email headers
- Assess SPF, DKIM, and DMARC results when present
- Identify mismatched domains or display-name spoofing
- Safely inspect suspicious URL structure without interacting with live malicious content
- Extract and document sanitized IOCs
- Assess social-engineering indicators
- Classify the message
- Map supported behavior to MITRE ATT&CK
- Recommend containment and user-response actions

## Evidence

Evidence will be added only after the controlled investigation is performed. Any public screenshot will be sanitized before publication.

## Analyst Verdict

**Pending validation.**

## Ethics

This investigation will use a deliberately constructed or benign training sample. No real credentials, active phishing infrastructure, malicious payloads, or third-party targets will be used.
