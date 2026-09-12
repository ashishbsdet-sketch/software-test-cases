# Checkout Test Cases

## TC-CHK-001 — Require mandatory delivery-address fields

- **Requirement:** REQ-CHK-01
- **Priority:** High
- **Type:** Negative / validation

### Preconditions

The cart contains one available product and checkout is open.

### Steps

1. Leave the postal code empty.
2. Complete every other required address field.
3. Select **Continue to payment**.

### Expected result

Checkout remains on the address step, postal code receives a specific validation message and entered values are retained.

## TC-CHK-002 — Reconcile the displayed order total

- **Requirement:** REQ-CHK-02
- **Priority:** Critical
- **Type:** Calculation / integration

### Preconditions

The cart contains a taxable $50 item, $5 shipping and a valid $10 discount.

### Steps

1. Apply the discount.
2. Continue to the order review.
3. Calculate subtotal minus discount plus shipping and displayed tax.
4. Compare the calculation with the final total.

### Expected result

Every component is itemized once and the final total equals the independently calculated amount.

## TC-CHK-003 — Preserve the cart after a declined payment

- **Requirement:** REQ-CHK-03
- **Priority:** Critical
- **Type:** Negative / end-to-end

### Preconditions

Checkout is ready for payment and the sandbox decline token is available.

### Steps

1. Submit the order using the decline token.
2. Observe the payment result.
3. Open order history.
4. Return to the cart.

### Expected result

A safe decline message appears, no order is created, inventory is unchanged and the cart remains available for retry.

## TC-CHK-004 — Create one order after successful payment

- **Requirement:** REQ-CHK-04
- **Priority:** Critical
- **Type:** Positive / end-to-end / smoke

### Preconditions

Checkout contains an in-stock product, valid address and approved sandbox payment token.

### Steps

1. Review the complete order.
2. Submit payment once.
3. Record the confirmation number.
4. Open order history.

### Expected result

Exactly one order is created with the reviewed total and a unique confirmation number shown on both pages.

## TC-CHK-005 — Prevent duplicate orders after repeated submission

- **Requirement:** REQ-CHK-05
- **Priority:** Critical
- **Type:** Reliability / negative

### Preconditions

The order is ready to submit and the network can be throttled.

### Steps

1. Enable a slow network profile.
2. Select **Place order** twice quickly.
3. Wait for the final response.
4. Review order history and payment transactions.

### Expected result

Only one payment and one order are created; repeated submission is ignored or returns the original result.
