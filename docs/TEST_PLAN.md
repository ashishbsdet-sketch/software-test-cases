# Risk-Based Test Plan

## Objective

Validate the highest-value customer journey from sign-in and product discovery through cart and checkout, while also checking API contracts, responsive behaviour and keyboard access.

## Scope

**In scope:** authentication, password recovery, search, filtering, cart state, totals, address validation, payment outcomes, order creation, product/order APIs, responsive layout and keyboard accessibility.

**Out of scope:** real payment settlement, third-party delivery fulfilment, production performance, penetration testing and destructive account recovery.

## Test approach

| Test type | Purpose |
| --- | --- |
| Smoke | Confirm the build supports the critical purchase path |
| Functional | Verify each acceptance criterion |
| Negative | Confirm invalid input fails safely and clearly |
| Boundary | Exercise attempt, quantity, time and viewport limits |
| Integration | Check UI, payment and order-service outcomes together |
| API | Verify status, authorization and response contracts |
| Accessibility | Check keyboard operation, focus and accessible names |

## Test environment

- QA web and mobile-responsive build
- Current Chrome and Firefox; Safari on macOS/iOS
- PostgreSQL-backed test environment
- Payment sandbox with approved and declined test tokens
- Synthetic customer, product and address data only

## Entry criteria

- Acceptance criteria reviewed
- QA environment deployed and reachable
- Test accounts and products available
- Payment sandbox stable
- Known blocking issues communicated

## Exit criteria

- All smoke cases pass
- No open critical or high-severity checkout defect
- At least 95% planned cases executed
- Failed and blocked cases have linked defects or reasons
- Product owner accepts remaining risk

## Reporting

Report progress by passed, failed, blocked and not-run counts. A failed case must identify the actual result and related defect. Retesting uses the same environment details and retains a separate result.
