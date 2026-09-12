# API, Mobile and Accessibility Test Cases

## TC-API-001 — Validate the product pagination contract

- **Requirement:** REQ-API-01
- **Priority:** High
- **Type:** API / contract

### Preconditions

The API contains more than 20 active products.

### Steps

1. Send `GET /api/products?page=1&limit=20`.
2. Record the status, headers and response body.
3. Validate the pagination metadata and each product object.

### Expected result

The response is 200, contains no more than 20 unique products and includes stable page, limit and total metadata.

## TC-API-002 — Reject order history without authentication

- **Requirement:** REQ-API-02
- **Priority:** Critical
- **Type:** API / security / negative

### Preconditions

A customer has order history and no authentication token is supplied.

### Steps

1. Send `GET /api/orders` without an Authorization header.
2. Repeat with an expired token.
3. Compare both response bodies.

### Expected result

Both requests return 401 with a generic error and expose no order or customer data.

## TC-MOB-001 — Keep checkout usable at the minimum supported width

- **Requirement:** REQ-MOB-01
- **Priority:** Critical
- **Type:** Responsive / boundary

### Preconditions

The cart has one item and the viewport is 320 × 568.

### Steps

1. Open the cart in portrait orientation.
2. Scroll through the order summary.
3. Select the checkout action.
4. Rotate to landscape and return to portrait.

### Expected result

Content does not overlap or scroll horizontally, and the checkout action remains fully visible and selectable in both orientations.

## TC-A11Y-001 — Complete sign-in using only the keyboard

- **Requirement:** REQ-A11Y-01
- **Priority:** High
- **Type:** Accessibility / keyboard

### Preconditions

The sign-in page is open and the mouse is not used.

### Steps

1. Use Tab to move through email, password and sign-in.
2. Confirm visible focus at each control.
3. Enter valid credentials.
4. Activate sign-in using Enter.

### Expected result

Focus order is logical, every control has a visible indicator and the form can be submitted without a pointer.

## TC-A11Y-002 — Expose accessible names for checkout controls

- **Requirement:** REQ-A11Y-01
- **Priority:** High
- **Type:** Accessibility / semantics

### Preconditions

Checkout is open and a browser accessibility inspector is available.

### Steps

1. Inspect text fields, selections, error messages and icon buttons.
2. Compare each accessible name with its visible purpose.
3. Trigger one validation error and inspect its relationship to the field.

### Expected result

Controls have unique meaningful names, and validation errors are programmatically associated with the affected fields.
