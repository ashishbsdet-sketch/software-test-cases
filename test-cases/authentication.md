# Authentication Test Cases

## TC-AUTH-001 — Sign in with valid credentials

- **Requirement:** REQ-AUTH-01
- **Priority:** Critical
- **Type:** Positive / smoke

### Preconditions

A registered, active customer exists and the sign-in page is open.

### Steps

1. Enter the registered email.
2. Enter the correct password.
3. Select **Sign in**.

### Expected result

The account home page opens, the customer name is visible and a new authenticated session is created.

## TC-AUTH-002 — Reject an incorrect password without exposing account details

- **Requirement:** REQ-AUTH-02
- **Priority:** High
- **Type:** Negative / security

### Preconditions

A registered customer exists and is not locked.

### Steps

1. Enter the registered email.
2. Enter an incorrect password.
3. Select **Sign in**.

### Expected result

Sign-in is rejected with a generic credentials message that does not confirm whether the email exists.

## TC-AUTH-003 — Lock the account after the fifth failed attempt

- **Requirement:** REQ-AUTH-03
- **Priority:** Critical
- **Type:** Boundary / security

### Preconditions

A registered customer has no recent failed attempts.

### Steps

1. Submit an incorrect password four times.
2. Confirm the fifth attempt has not yet been submitted.
3. Submit an incorrect password for the fifth time.
4. Attempt to sign in with the correct password.

### Expected result

The fifth failure activates the temporary lock, and the correct password is rejected until the lock period ends.

## TC-AUTH-004 — Reject an expired password-reset link

- **Requirement:** REQ-AUTH-04
- **Priority:** High
- **Type:** Negative / boundary

### Preconditions

A reset link was generated more than 30 minutes ago.

### Steps

1. Open the expired reset link.
2. Enter and confirm a compliant new password.
3. Submit the form.

### Expected result

The password is not changed and the user is prompted to request a new link.

## TC-AUTH-005 — Prevent reuse of the session after sign-out

- **Requirement:** REQ-AUTH-05
- **Priority:** Critical
- **Type:** Security / regression

### Preconditions

The customer is signed in on an account page.

### Steps

1. Select **Sign out**.
2. Use the browser Back button.
3. Refresh the previously authenticated page.

### Expected result

Protected account content is not displayed and the user is redirected to sign-in.
