# Illustrative Test Execution Report

> This is a controlled reporting example, not the result of testing a production application.

| Metric | Count |
| --- | ---: |
| Planned | 20 |
| Executed | 18 |
| Passed | 15 |
| Failed | 3 |
| Blocked | 2 |
| Not run | 0 |
| Pass rate among executed cases | 83.3% |

## Failed examples

| Test case | Observation | Suggested action |
| --- | --- | --- |
| TC-CART-002 | Quantity 11 was stored after refresh | Log a high-severity validation defect |
| TC-CHK-003 | A declined attempt created a pending order | Stop checkout release and triage |
| TC-MOB-001 | Sticky content covered checkout at 320px | Log responsive defect with viewport evidence |

## Blocked examples

| Test case | Blocker |
| --- | --- |
| TC-AUTH-004 | Reset-email service unavailable in QA |
| TC-CHK-005 | Network throttling profile unavailable on shared device |

## Release view

The build would not be recommended for release because a critical negative checkout case failed. The owner should also assess the cart and minimum-width defects before retest.
