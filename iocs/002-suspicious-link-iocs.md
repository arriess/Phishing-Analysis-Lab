# IOC Set 002 — Suspicious Link Simulation

**Associated investigation:** [`investigations/002-suspicious-link-analysis.md`](../investigations/002-suspicious-link-analysis.md)  
**Source:** Simulated / benign training sample only

## Extracted Indicators

| Indicator Type | Value | Analyst Context |
|---|---|---|
| Initial domain | `secure-sharepoint-login.example` | Uses trusted-brand wording to resemble a collaboration/login service |
| Redirect domain | `m365-session-check.example` | Microsoft 365-themed destination used in the simulated redirect chain |
| Initial IP | `198.51.100.44` | TEST-NET-2 documentation address |
| Redirect IP | `203.0.113.25` | TEST-NET-3 documentation address |
| Initial path | `/auth` | Authentication-themed path consistent with a credential-harvest pretext |
| Redirect path | `/signin` | Sign-in themed destination |
| Continue parameter | `/account/verify` | Verification-themed navigation target |
| Embedded redirect parameter | `redirect=...` | Encoded redirect parameter hides the next destination from a casual user |
| User parameter | `employee@soc-lab.example` | Synthetic identity parameter indicating possible user targeting in the training scenario |

## IOC Handling Notes

All indicators are non-production training values. Reserved `.example` domains and TEST-NET address ranges are used so no live malicious infrastructure is contacted or published.
