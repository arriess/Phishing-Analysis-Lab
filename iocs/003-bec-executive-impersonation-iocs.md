# IOC Set 003 — Executive Impersonation / BEC Simulation

**Associated investigation:** [`investigations/003-business-email-compromise.md`](../investigations/003-business-email-compromise.md)  
**Source:** Simulated / benign training sample only

## Extracted Indicators

| Indicator Type | Value | Analyst Context |
|---|---|---|
| Sender domain | `executive-mail.example` | Synthetic external domain used to impersonate an executive identity |
| Reply-To domain | `consultant-mail.example` | Reply path differs from the visible sender domain |
| Sender host | `mail.executive-mail.example` | Synthetic sending host |
| Source IP | `203.0.113.90` | TEST-NET-3 documentation address; not a real attack host |
| Payment amount | `EUR 48,750` | Fictitious high-value payment request used to create financial urgency |
| Payment reference | `PROJECT-ALPHA-003` | Synthetic transaction reference |
| SPF result | `pass` | Demonstrates that a sender-controlled domain can authenticate successfully while the message remains malicious in intent |
| DKIM result | `pass` | Authentication confirms domain control, not legitimacy of the claimed executive identity |
| DMARC result | `pass` | Alignment alone does not rule out BEC or impersonation |

## Behavioral Indicators

- Executive / CEO display-name impersonation
- Urgent same-day payment request
- High-value transfer request
- New beneficiary / changed bank details pretext
- Confidentiality pressure
- Instruction not to contact the supplier
- Request to bypass normal verification channels
- Reply-To mismatch

## Safety Notes

All names, organizations, domains, payment details, and infrastructure in this IOC set are fictitious or reserved for documentation. No live accounts, real bank details, or third-party infrastructure are involved.
