# Python Syntax & Fundamentals— 



## Learning outcomes
- Basic Python syntax and output
- Conditional statements and boolean logic
- Functions, parameters, return values, and indentation
- Loops and list processing
- Simple algorithms and debugging
- Linux navigation/file-management concepts (written question)

## Assessment structure
- **Coding section:** five functions in `fundamentals.py`, tested with pytest.
- **Long-format section:** solved written responses in `answers.txt`.

## Run the tests
Install pytest if needed:

```bash
python -m pip install pytest
```

Run all tests from this folder:

```bash
python -m pytest -v
```

## Project structure

```text
python_syntax_variant/
├── fundamentals.py
├── answers.txt
├── README.md
└── tests/
    └── test_fundamentals.py
```

## Coding questions

1. **`water_alerts(n)`** — print numbers from 1 to `n`, replacing multiples of 4 with `SaveWater`, multiples of 6 with `CheckLeaks`, and multiples of both with `Critical`.
2. **`weekend_temperatures(temperatures)`** — return a new list containing temperatures of 25 or higher, preserving order.
3. **`calculate_delivery_fee(distance, items)`** — calculate a delivery fee using a base fee of R12, R4 per kilometre, R6 per item above 3, and a minimum fee of R20.
4. **`library_loan(balance, books_requested)`** — validate the number of books and whether the account has an outstanding balance.
5. **`learner_qualifies(attendance, mark, tasks_done, tasks_total)`** — return `True` only if attendance is at least 75%, the mark is at least 50%, and all tasks are completed.

All implementations and the written answers are included. The tests are designed to verify the intended behaviour and edge cases.
