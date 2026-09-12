# Software Test Cases

[![Test Case Quality](https://github.com/ashishbsdet-sketch/software-test-cases/actions/workflows/validate-test-cases.yml/badge.svg)](https://github.com/ashishbsdet-sketch/software-test-cases/actions/workflows/validate-test-cases.yml)

This repository shows how I turn product requirements into clear, reviewable manual test coverage. The reference product is a fictional commerce application with web, mobile and API surfaces, so the cases can demonstrate realistic QA thinking without making claims about a real company.

## Coverage at a glance

| Suite | Cases | Main risks covered |
| --- | ---: | --- |
| Authentication | 5 | Access, lockout, session and password recovery |
| Search and cart | 5 | Discovery, filtering, boundaries and cart state |
| Checkout | 5 | Address validation, payment failure and order confirmation |
| API, mobile and accessibility | 5 | Contracts, authorization, responsive layout and keyboard use |
| **Total** | **20** | Positive, negative, boundary, integration and end-to-end |

## What is included

- concise requirements and acceptance criteria
- a risk-based test plan
- 20 detailed manual test cases
- requirement-to-test traceability matrix
- smoke and regression suite definitions
- an illustrative execution report
- reusable test-case and execution templates
- automated checks for duplicate IDs and missing sections

## Repository structure

```text
.
├── requirements/             # Test basis and acceptance criteria
├── test-cases/               # Detailed suites grouped by feature
├── suites/                   # Smoke and regression selections
├── traceability/             # Requirement coverage
├── execution/                # Sample execution reporting
├── templates/                # Reusable QA templates
├── docs/TEST_PLAN.md
└── scripts/validate_test_cases.py
```

## How to read a case

Every case states its requirement, priority, test type, preconditions, numbered actions and one observable expected result. Test data is specific enough to repeat while avoiding real personal or payment information.

## Run the quality check

```bash
python3 scripts/validate_test_cases.py
```

The validator discovers all test-case IDs, rejects duplicates and verifies that each case contains the required metadata and sections. GitHub Actions publishes the validated case count directly in the run summary.

## Portfolio note

The product, accounts and execution results are controlled examples. They demonstrate test design and reporting technique; they are not presented as results from a real production system.
