# Phishing Response Playbook

## Purpose

Provide a repeatable SOC workflow for triaging and responding to reported phishing emails in a controlled training environment.

## Workflow

1. **Intake** — Record the report context without opening suspicious attachments or visiting suspicious links.
2. **Preserve evidence** — Retain the original message or sanitized training equivalent, including headers when available.
3. **Triage sender identity** — Compare display name, From, Reply-To, and sender domain.
4. **Review authentication** — Check SPF, DKIM, and DMARC results when present and interpret them as supporting evidence rather than a standalone verdict.
5. **Analyze content** — Identify urgency, credential requests, payment requests, impersonation, unusual language, and other social-engineering indicators.
6. **Analyze links safely** — Parse and defang URLs. Use benign or approved analysis methods; do not browse active malicious infrastructure.
7. **Extract indicators** — Document relevant domains, URLs, hostnames, IPs, or hashes using sanitized/defanged notation where appropriate.
8. **Assess scope and impact** — Determine whether the scenario suggests credential theft, malware delivery, BEC, or another objective.
9. **Classify** — Record the analyst verdict, severity, confidence, and false-positive considerations.
10. **Respond** — Recommend containment, blocking, credential-reset, user notification, escalation, or additional investigation as appropriate to the controlled scenario.
11. **Document** — Produce a concise analyst report with evidence, reasoning, MITRE ATT&CK mapping where supported, and sanitized screenshots.

## Example Classification Fields

- Verdict: Benign / Suspicious / Phishing
- Severity: Informational / Low / Medium / High
- Confidence: Low / Medium / High
- Primary risk: Credential theft / Malware delivery / BEC / Other
- User interaction: None / Link clicked / Credentials submitted / Unknown

## Safety

This playbook is for authorized training and defensive analysis only. It does not require interacting with active malicious infrastructure or collecting real credentials.
