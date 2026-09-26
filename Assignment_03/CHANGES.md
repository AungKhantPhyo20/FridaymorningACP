# Assignment 03 — CHANGES

**Name:** AUNG KHANT PHYO  **Student ID:** 6705140081

This is the written part of your submission. Explain **what you changed and why**, then record your **prompt log**. Keep before/after snippets to a line or two.

---

## 1 · What I changed

One row per change. Name the OOP concept and say how you checked the behaviour was unchanged.

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products, orders, and items were stored as nested tuples | Added `Product`, `OrderItem`, and `Order` objects with attributes and relationships | Classes / composition | Ran `python3 Assignment_03/Assignment_03.py` -> PASS |
| 2 | Discount and points used repeated tier `if/elif` chains | Added `NoneCustomer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` subclasses | Inheritance / polymorphism | The self-test compared the complete receipt output and passed |
| 3 | Constructors did not validate object state because there were no domain objects | Added validation for names, prices, categories, quantities, customers, and order items | Encapsulation | Tested the normal data through `build_orders()` and the self-test passed |
| 4 | Calculations and printing were mixed inside `calc()` | Added pure `subtotal()`, `tax()`, `discount()`, `total()`, and `points()` methods; `receipt()` handles formatting | Separation of concerns / pure methods | Compared refactored output with the locked legacy output; PASS |
| 5 | Tax, discount, bulk quantity, and points values were magic numbers and the legacy calculation used a global | Replaced them with named constants and made each `Product` calculate its own tax | Encapsulation / abstraction | Ran the complete program with `python3`; exact behavior was unchanged |

## 2 · Short reflection (4–6 sentences)

Which change improved the code the most, and why? Where did keeping the behaviour identical force you to be careful?

The new domain classes improved the code most because the data and the rules now live together in objects that are easier to understand. Customer subclasses remove the duplicated tier decisions and make discount and points behavior polymorphic. Keeping the output identical required preserving the original order, spacing, rounding, and string formatting. I also had to keep the tax and discount calculations numerically equivalent, including the bulk discount rule. The self-test compares the complete refactored output with the legacy output and printed PASS.

---

## 3 · Prompt log (Level 2 — required)

Record **every** prompt where AI helped. If you wrote a part yourself, say so in one row. AI-shaped code with an empty log does **not** meet the Level-2 policy.

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | "Check Assignment 03 and do everything needed to finish the `Assignment_03.py` and `CHANGES.md` files." | Implemented the `Product`, `OrderItem`, `Order`, and customer tier class family; separated calculations from receipt printing; added validation, named constants, and object construction. | Accepted with edits to match the assignment's exact output requirement. | Ran `python3 Assignment_03/Assignment_03.py`; it printed `PASS - behaviour is unchanged. Your refactor is safe.` |
| 2 | No other AI prompt was used for this assignment. | The implementation and documentation were completed from the assignment brief and the verified self-test. | N/A | Read the refactored code and checked the built-in behavior comparison. |
| 3 | No additional prompt. | No additional suggestion. | N/A | No additional change. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

---

## 4 · Before-you-submit checklist

- [ ] `python Assignment_03.py` prints **PASS**.
- [ ] No tuples / parallel lists left — products, orders, and items are objects.
- [ ] No `if tier == ...` chains — tiers are a class family.
- [ ] Calculation methods **return** values and do not `print`; printing is separate.
- [ ] Constructors validate state; no leftover `global`; magic numbers are named.
- [ ] The change table and reflection above are filled in.
- [ ] The prompt log is complete and the ownership statement is signed.
