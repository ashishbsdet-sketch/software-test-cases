# Search and Cart Test Cases

## TC-SRCH-001 — Find an active product using a partial keyword

- **Requirement:** REQ-SRCH-01
- **Priority:** High
- **Type:** Positive / functional

### Preconditions

An active product named “Wireless Keyboard” is searchable.

### Steps

1. Enter `wireless key` in search.
2. Submit the search.
3. Review the result list.

### Expected result

The Wireless Keyboard appears, and every returned product matches the keyword in its name or description.

## TC-SRCH-002 — Combine and clear category and price filters

- **Requirement:** REQ-SRCH-02
- **Priority:** Medium
- **Type:** Functional / state

### Preconditions

Search results span multiple categories and price ranges.

### Steps

1. Select the Accessories category.
2. Set the maximum price to $50.
3. Apply the filters.
4. Clear all filters.

### Expected result

The combined result set respects both filters, and clearing restores the original unfiltered results.

## TC-CART-001 — Add an available product to an empty cart

- **Requirement:** REQ-CART-01
- **Priority:** Critical
- **Type:** Positive / smoke

### Preconditions

The cart is empty and Wireless Keyboard is in stock.

### Steps

1. Open the Wireless Keyboard details.
2. Select **Add to cart**.
3. Open the cart.

### Expected result

One Wireless Keyboard is shown with quantity 1, the correct unit price and a matching cart badge.

## TC-CART-002 — Enforce the maximum quantity boundary

- **Requirement:** REQ-CART-02
- **Priority:** High
- **Type:** Boundary / negative

### Preconditions

One in-stock product is in the cart.

### Steps

1. Change quantity to `10` and update the cart.
2. Confirm the cart accepts the value.
3. Change quantity to `11` and update again.

### Expected result

Quantity 10 is accepted; quantity 11 is rejected with a clear message and does not change the stored cart total.

## TC-CART-003 — Restore a guest cart in the same browser

- **Requirement:** REQ-CART-03
- **Priority:** Medium
- **Type:** Persistence / integration

### Preconditions

The user is signed out and the browser allows local storage and cookies.

### Steps

1. Add one product to the cart.
2. Close the browser.
3. Reopen the application in the same browser profile within 24 hours.
4. Open the cart.

### Expected result

The same product, quantity and price are restored without requiring sign-in.
