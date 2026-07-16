# CheckPoint — Python Practice Exercises

A repository with 20 hands-on programming logic exercises in Python, covering everything from basic conditional structures (`if/elif/else`) to the more modern pattern-matching syntax (`match/case`, available from Python 3.10 onward).

## How to run

Each exercise is a standalone script. Just run:

```bash
python "Exercicio N.py"
```

and answer the prompts in the terminal.

## Index

| # | Exercise | Main concept |
|---|-----------|---------------------|
| 1 | [BMI Calculator](#1-detailed-bmi-calculator) | `if/elif/else` |
| 2 | [Temperature Converter](#2-smart-temperature-converter) | `if/elif/else` + strings |
| 3 | [Discount by Payment Method](#3-discount-calculator-by-payment-method) | `if/elif/else` |
| 4 | [Seconds Converter](#4-seconds-converter) | Integer arithmetic (`//`, `%`) |
| 5 | [Leap Year](#5-leap-year-checker) | Logical operators |
| 6 | [Triangle Classifier](#6-triangle-validator-and-classifier) | Nested conditionals |
| 7 | [Retirement Rules](#7-retirement-eligibility-checker) | `if/elif/else` |
| 8 | [Income Tax](#8-income-tax-calculator) | `if/elif/else` (with bugs) |
| 9 | [Four-Operation Calculator](#9-basic-operations-calculator) | `if/elif/else` + error handling |
| 10 | [Cartesian Quadrant](#10-cartesian-quadrant-identifier) | Multiple conditionals |
| 11 | [Rock, Paper, Scissors](#11-rock-paper-and-scissors) | Nested conditionals |
| 12 | [Student Status](#12-student-status-grades-and-absences) | Nested conditionals |
| 13 | [Quadratic Equation (Bhaskara)](#13-quadratic-equation-bhaskara) | `math`, `if/elif/else` |
| 14 | [Date Validator](#14-date-validator) | `match/case` |
| 15 | [ATM Machine](#15-atm-machine-bill-breakdown) | Integer arithmetic |
| 16 | [Zodiac Sign](#16-zodiac-sign-identifier) | Extensive `if/elif/else` |
| 17 | [HTTP Status Codes](#17-http-status-code-identifier) | `match/case` |
| 18 | [Currency Converter](#18-currency-converter) | `match/case` |
| 19 | [Month Name and Days](#19-month-name-and-number-of-days) | Nested `match/case` |
| 20 | [Vehicle Toll](#20-toll-calculator) | `match/case` |

---

## 1. Detailed BMI Calculator

**Context:** calculate the user's Body Mass Index (BMI) from weight and height, and classify the result into one of the six ranges used by the WHO.

**How it was solved:**
- Reads `peso` (weight in kg) and `altura` (height in m) as `float`.
- Calculates `imc = peso / (altura ** 2)`.
- A chain of `if/elif/else` compares the BMI against the limits of each range (underweight, normal weight, overweight, obesity grades I to III) and sets the `classificacao` string.
- Prints the classification and the BMI formatted to 2 decimal places (`{imc:.2f}`).

**Note:** `print("Classificação:", classificacao)` appears duplicated in the file (once before printing the BMI and once after) — redundant, but doesn't break execution.

---

## 2. Smart Temperature Converter

**Context:** convert a temperature between Celsius and Fahrenheit, based on the user's choice.

**How it was solved:**
- Asks whether the user wants to convert from `'C'` to Fahrenheit or from `'F'` to Celsius, normalizing the input with `.upper()` to accept lowercase letters.
- Applies the standard formulas: `F = C * 9/5 + 32` and `C = (F - 32) * 5/9`.
- Handles invalid input (anything other than C/F) with an error message in the `else` branch.

---

## 3. Discount Calculator by Payment Method

**Context:** simulate a store's pricing policy that varies depending on the payment method chosen.

**How it was solved:**
- The user chooses among 3 options: PIX (instant payment), single credit card payment, or installment credit card.
- PIX applies a 10% discount (`preco * 0.9`), single credit card payment keeps the original price, and installments apply 5% interest (`preco * 1.05`).
- An `if/elif/else` handles the chosen option and calculates the corresponding final price.

---

## 4. Seconds Converter

**Context:** convert a number of seconds into hours, minutes, and seconds.

**How it was solved:**
- Uses integer division (`//`) and modulo (`%`) successively:
  - `horas = tempo // 3600`
  - the remainder becomes `tempo % 3600`, from which `minutos = tempo // 60` is extracted
  - the final remainder is the remaining total of seconds.
- Prints the three values in a single formatted line.

---

## 5. Leap Year Checker

**Context:** determine whether a year is a leap year, following the Gregorian calendar rule.

**How it was solved:**
- Directly applies the mathematical rule: a year is a leap year if it's divisible by 4 **and** not divisible by 100, **or** if it's divisible by 400.
- Implemented as a single boolean expression: `(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)`.

---

## 6. Triangle Validator and Classifier

**Context:** check whether three given side lengths form a valid triangle and, if so, classify it (equilateral, isosceles, or scalene).

**How it was solved:**
- Applies the triangle inequality: the sum of any two sides must be greater than the third side, checked for all three possible pairs.
- If the condition is satisfied, it classifies with nested `if/elif/else`: all sides equal → equilateral; two sides equal → isosceles; otherwise → scalene.

> ⚠️ **Point of attention:** the script has no `else` branch for the case where the sides do **not** form a valid triangle — in that scenario, the program simply prints nothing.

---

## 7. Retirement Eligibility Checker

**Context:** simulate simplified retirement eligibility rules based on age and years of contribution.

**How it was solved:**
- Reads age and years of contribution.
- `if/elif/else` with three tiers: full retirement (age ≥ 65 or contribution ≥ 30 years), special rule (age ≥ 60 and contribution ≥ 25 years), or not yet eligible.

---

## 8. Income Tax Calculator

**Context:** calculate the income tax owed based on the informed salary, using simplified brackets.

**How it was solved:**
- Compares the salary against two bracket limits (`<= 2.112` and `<= 2.826`) and applies an effective-rate formula in the second bracket (`salario * 0.075 - 1713.58`).

> ⚠️ **This exercise has real bugs and does not work correctly as-is:**
> 1. The limits `2.112` and `2.826` are floating-point numbers (2.112 and 2.826), and were almost certainly meant to be `2112.00` and `2826.65` — this looks like a mix-up between the Brazilian thousands separator and Python's decimal point.
> 2. The formula `salario * 0.075 - 1713.58` produces a **negative** value for any salary in that bracket (e.g., R$ 2,500 × 0.075 = 187.50 − 1,713.58 = −1,526.08), which doesn't make sense for a tax amount.
> 3. The `imposto` (tax) variable is calculated but **never printed** to the screen.
> 4. The real income tax table has more than two brackets; this script's `else` branch only reports "salary above the limit" without calculating anything for higher earners.
>
> It's recommended to review the official income tax bracket values and rewrite the logic before considering this exercise "solved."

---

## 9. Basic Operations Calculator

**Context:** a simple calculator with the four basic arithmetic operations.

**How it was solved:**
- Reads two numbers and the desired operation (`1` to `4`) as text.
- `if/elif/else` performs addition, subtraction, multiplication, or division.
- For division, there's an extra check for `num2 == 0`, avoiding a `ZeroDivisionError` and reporting "Invalid operation."

---

## 10. Cartesian Quadrant Identifier

**Context:** given a point (x, y), identify which quadrant of the Cartesian plane it's in, or whether it lies on one of the axes/origin.

**How it was solved:**
- A chain of `if/elif` handles, in this order: origin (x=0 and y=0), Y axis (x=0), X axis (y=0), and the four quadrants (Q1 to Q4) by combining the sign of x and y.

---

## 11. Rock, Paper, and Scissors

**Context:** simulate one round of the classic Rock, Paper, Scissors game against the computer.

**How it was solved:**
- Reads the user's move (normalized with `.lower()`).
- Compares it with the computer's move using the classic logic: rock beats scissors, scissors beats paper, paper beats rock.
- Handles ties and invalid moves.

> ⚠️ **Limitation:** the variable `computador = "pedra"` (rock) is hardcoded in the code — there's no `import random`, so the computer always plays "rock" on every run. To make it an actual game, `random.choice(["pedra", "papel", "tesoura"])` would be needed.

---

## 12. Student Status (Grades and Absences)

**Context:** determine a student's final status based on two grades and the percentage of absences.

**How it was solved:**
- First checks whether absences exceed 25% — in that case, automatic failure due to absences, without even calculating the average.
- Otherwise, calculates the average of the two grades and classifies it as Passed (≥ 7.0), Retake exam (≥ 5.0), or Failed by Grade, using nested `if/elif/else`.

---

## 13. Quadratic Equation (Bhaskara)

**Context:** solve a quadratic equation (ax² + bx + c = 0) using the Bhaskara (quadratic) formula.

**How it was solved:**
- Imports `math` to use `math.sqrt`.
- Handles the special case `A == 0` (would not be a quadratic equation).
- Calculates the discriminant (`delta = B**2 - 4*A*C`) and uses `if/elif/else` for the three possible scenarios: negative delta (no real roots), zero delta (single root), and positive delta (two real roots, calculated with the full formula).

---

## 14. Date Validator

**Context:** check whether a day/month/year combination forms a valid calendar date, accounting for leap years.

**How it was solved:**
- Calculates whether the year is a leap year using the same rule from Exercise 5.
- Uses `match/case` on the month to determine the day limit: February (28 or 29, depending on leap year), 30-day months (`4 | 6 | 9 | 11`), 31-day months (`1 | 3 | 5 | 7 | 8 | 10 | 12`), and a fallback `case _` for an invalid month.
- Validates the day against the calculated limit using a conditional expression (`"Data válida!" if 1 <= dia <= limite else "Data inválida!"`).

---

## 15. ATM Machine (Bill Breakdown)

**Context:** simulate the logic of an ATM machine, breaking down a withdrawal amount into the smallest number of available bills (100, 50, 20, 10, 5, and 2 units).

**How it was solved:**
- First rules out amounts that can't be formed with the available bills (amounts smaller than 2, or equal to 1 or 3).
- Then applies integer division and modulo successively for each bill, from largest to smallest, "reducing" the remaining amount at each step — the same technique used in Exercise 4.
- At the end, if any amount remains that can't be divided by the available bills, it reports the withdrawal as invalid; otherwise, it prints the quantity of each bill dispensed.

---

## 16. Zodiac Sign Identifier

**Context:** given a birth day and month, identify the corresponding zodiac sign.

**How it was solved:**
- First validates that month and day fall within plausible ranges (month 1–12, day 1–31).
- Uses a long chain of `elif`, each covering the date range of one sign (e.g., Aries runs from 03/21 to 04/19, tested as two conditions joined by `or`, since the range crosses a month boundary).
- As a possible improvement: this repetitive logic could be simplified with a list of tuples `(month_limit, day_limit, sign_name)` iterated in a loop, but as an `if/elif` practice exercise the current solution is correct.

---

## 17. HTTP Status Code Identifier

**Context:** given an HTTP status code, display its meaning.

**How it was solved:**
- Uses `match/case` to directly map the most common codes (200, 400, 401, 403, 404, 500) to their textual description.
- The `case _` covers any unregistered code.

---

## 18. Currency Converter

**Context:** convert an amount in Brazilian Reais to US Dollar, Euro, British Pound, or Japanese Yen, using fixed exchange rates.

**How it was solved:**
- Uses `match/case` on the chosen option (1 to 4) to select the corresponding exchange rate and divide the amount in reais by it.
- Formats the output with each currency's symbol (`$`, `€`, `£`, `¥`) and two decimal places.

> **Note:** the exchange rates are hardcoded in the source — fine for teaching purposes, but would require integration with a currency exchange API to reflect real, up-to-date values.

---

## 19. Month Name and Number of Days

**Context:** given a month number (1 to 12), display its full name and how many days it has.

**How it was solved:**
- Uses an outer `match/case` to group months by their number of days (31, 30, or February on its own).
- Inside each group, a second, nested `match/case` translates the month number into its Portuguese name.
- February is handled separately, since its number of days varies (28 or 29).

> **Note:** the solution works, but nesting two `match` statements is more verbose than necessary — the same result could be achieved with a single dictionary `{1: "Janeiro", 2: "Fevereiro", ...}` and a separate list of 30/31-day months.

---

## 20. Toll Calculator

**Context:** calculate the toll amount based on vehicle type.

**How it was solved:**
- Uses `match/case` to map the vehicle type (1 to 4: motorcycle, car, pickup truck, truck) to the corresponding fee (R$ 5, 10, 15, and 25).
- The `case _` handles invalid types.

---

## Summary of points of attention

| Exercise | Identified issue |
|---|---|
| 1 | Duplicated classification `print` (cosmetic, doesn't affect the result) |
| 6 | Missing handling for the case where the sides do **not** form a valid triangle |
| 8 | Incorrect bracket limits, formula produces a negative tax, `imposto` variable never printed, missing brackets from the real tax table |
| 11 | The computer's move is hardcoded (`"pedra"`/rock) — missing `import random` to make the game actually functional |

These issues don't prevent understanding the concept practiced in each exercise, but they would be the first targets for fixes if the repository evolves toward a "production" version.
