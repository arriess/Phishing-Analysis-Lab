# IOC Set 001 — Credential Phishing Simulation

**Associated investigation:** [`investigations/001-credential-phishing-analysis.md`](../investigations/001-credential-phishing-analysis.md)  
**Source:** Simulated / benign training sample only

## Extracted Indicators

| Indicator Type | Value | Analyst Context |
|---|---|---|
| Visible sender domain | `microsoft-support.example` | Brand-impersonation domain used by the synthetic sample |
| Reply-To domain | `account-check.example` | Does not match the visible sender domain |
| Return-Path domain | `account-check.example` | Supports the sender/reply-path mismatch observed during triage |
| Link domain | `login-microsoft.example` | Microsoft-themed lookalike naming used for the simulated credential-verification lure |
| Source host | `mail.account-check.example` | Synthetic sending host |
| Source IP | `192.0.2.55` | TEST-NET-1 documentation address; not a real attack host |
| URL path | `/verify` | Verification-themed path consistent with the phishing pretext |
| URL parameter | `session=TRAINING-001` | Synthetic training parameter; not a real token |
| SPF result | `fail` | Simulated authentication failure |
| DKIM result | `none` | Simulated missing DKIM signature |
| DMARC result | `fail` | Simulated authentication/alignment failure |

## IOC Handling Notes

All domains use the reserved `.example` namespace and the IP address is from TEST-NET-1. They are deliberately non-production indicators created for this portfolio exercise.

No live malicious URLs, real user addresses, credentials, tokens, production IP addresses, or third-party infrastructure are published in this IOC set.
