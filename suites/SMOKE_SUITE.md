# Smoke Suite

Run this suite after every QA deployment.

| Order | Test case | Reason |
| ---: | --- | --- |
| 1 | TC-AUTH-001 | Confirms customer access |
| 2 | TC-SRCH-001 | Confirms product discovery |
| 3 | TC-CART-001 | Confirms cart integration |
| 4 | TC-CHK-002 | Protects total calculation |
| 5 | TC-CHK-004 | Confirms the critical purchase journey |
| 6 | TC-API-002 | Protects order data |
| 7 | TC-MOB-001 | Protects the minimum supported viewport |

Stop and notify the team when a critical smoke case fails. Record environmental blockers separately from product failures.
