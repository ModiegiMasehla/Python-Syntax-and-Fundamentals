"""Solved : Python fundamentals and problem solving."""


def water_alerts(n: int) -> None:
    """Print numbers from 1 to n with water-use alerts for multiples of 4 and 6."""
    for number in range(1, n + 1):
        if number % 4 == 0 and number % 6 == 0:
            print("Critical")
        elif number % 4 == 0:
            print("SaveWater")
        elif number % 6 == 0:
            print("CheckLeaks")
        else:
            print(number)


def weekend_temperatures(temperatures: list) -> list:
    """Return a new list containing temperatures of 25 degrees or higher."""
    warm_days = []
    for temperature in temperatures:
        if temperature >= 25:
            warm_days.append(temperature)
    return warm_days


def calculate_delivery_fee(distance: int, items: int) -> int:
    """Calculate delivery fee: R12 base, R4/km, R6 per item above 3, minimum R20."""
    base_fee = 12
    fee_per_km = 4
    total = base_fee + (fee_per_km * distance)

    if items > 3:
        extra_items = items - 3
        total += extra_items * 6

    if total < 20:
        total = 20

    return total


def library_loan(balance: int, books_requested: int) -> str:
    """Approve a library loan if the account is clear and at most 5 books are requested."""
    if books_requested <= 0 or books_requested > 5:
        return "Error: Invalid book count"
    if balance > 0:
        return "Error: Outstanding balance"
    return "Success: Loan approved"


def learner_qualifies(attendance: int, mark: int, tasks_done: int, tasks_total: int) -> bool:
    """Return True when attendance >= 75, mark >= 50, and every task is submitted."""
    if tasks_total <= 0 or tasks_done != tasks_total:
        return False
    if attendance < 75:
        return False
    if mark < 50:
        return False
    return True
