# Reference Commerce Requirements

## Authentication

- **REQ-AUTH-01:** A registered user can sign in with a valid email and password.
- **REQ-AUTH-02:** Invalid credentials return a generic error without revealing which value is wrong.
- **REQ-AUTH-03:** An account is temporarily locked after five consecutive failed attempts.
- **REQ-AUTH-04:** A password-reset link expires 30 minutes after it is issued and after first use.
- **REQ-AUTH-05:** Signing out invalidates the current session.

## Search and cart

- **REQ-SRCH-01:** Keyword search returns active products matching their name or description.
- **REQ-SRCH-02:** Category and price filters can be combined and cleared.
- **REQ-CART-01:** An available product can be added, updated and removed from the cart.
- **REQ-CART-02:** Cart quantity accepts whole numbers from 1 through 10.
- **REQ-CART-03:** A guest cart persists in the same browser for 24 hours.

## Checkout

- **REQ-CHK-01:** Checkout requires a complete delivery address.
- **REQ-CHK-02:** The displayed order total equals subtotal, shipping, discount and tax.
- **REQ-CHK-03:** A declined payment does not create an order or reduce inventory.
- **REQ-CHK-04:** A successful payment creates one order and displays a unique confirmation number.
- **REQ-CHK-05:** Repeated submission of the same payment request must not create duplicate orders.

## API, mobile and accessibility

- **REQ-API-01:** Product-list requests return a stable paginated response contract.
- **REQ-API-02:** Order endpoints reject unauthenticated requests.
- **REQ-MOB-01:** Primary actions remain visible and usable from 320px through 1440px widths.
- **REQ-A11Y-01:** Interactive controls are keyboard reachable and have accessible names.
