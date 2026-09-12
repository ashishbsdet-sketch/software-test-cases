# Requirements Traceability Matrix

| Requirement | Risk | Covered by | Coverage |
| --- | --- | --- | --- |
| REQ-AUTH-01 | Authorized access | TC-AUTH-001 | Positive |
| REQ-AUTH-02 | Account disclosure | TC-AUTH-002 | Negative |
| REQ-AUTH-03 | Brute-force attempts | TC-AUTH-003 | Boundary |
| REQ-AUTH-04 | Reset-token misuse | TC-AUTH-004 | Time boundary |
| REQ-AUTH-05 | Session reuse | TC-AUTH-005 | Security |
| REQ-SRCH-01 | Product discovery | TC-SRCH-001 | Functional |
| REQ-SRCH-02 | Incorrect filtered results | TC-SRCH-002 | Combination/state |
| REQ-CART-01 | Purchase path | TC-CART-001 | Positive |
| REQ-CART-02 | Invalid quantity | TC-CART-002 | Boundary |
| REQ-CART-03 | Lost guest cart | TC-CART-003 | Persistence |
| REQ-CHK-01 | Undeliverable order | TC-CHK-001 | Negative |
| REQ-CHK-02 | Incorrect charge | TC-CHK-002 | Calculation |
| REQ-CHK-03 | Order created after decline | TC-CHK-003 | Negative E2E |
| REQ-CHK-04 | Missing confirmation | TC-CHK-004 | Positive E2E |
| REQ-CHK-05 | Duplicate charge/order | TC-CHK-005 | Reliability |
| REQ-API-01 | Contract regression | TC-API-001 | API contract |
| REQ-API-02 | Data exposure | TC-API-002 | API security |
| REQ-MOB-01 | Blocked mobile purchase | TC-MOB-001 | Responsive boundary |
| REQ-A11Y-01 | Inaccessible controls | TC-A11Y-001, TC-A11Y-002 | Keyboard/semantics |

All 19 documented requirements have at least one test. Accessibility intentionally has two cases because keyboard operation and accessible semantics expose different risks.
