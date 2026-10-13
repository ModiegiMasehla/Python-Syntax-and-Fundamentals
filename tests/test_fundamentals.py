import pytest
from fundamentals import (
    water_alerts,
    weekend_temperatures,
    calculate_delivery_fee,
    library_loan,
    learner_qualifies,
)


class TestWaterAlerts:
    def test_output_and_priority(self, capsys):
        water_alerts(12)
        assert capsys.readouterr().out.strip().splitlines() == [
            "1", "2", "3", "SaveWater", "5", "CheckLeaks", "7",
            "SaveWater", "9", "10", "11", "Critical"
        ]

    def test_zero_prints_nothing(self, capsys):
        water_alerts(0)
        assert capsys.readouterr().out == ""

    @pytest.mark.parametrize("n", [4, 8, 16, 20])
    def test_multiples_of_four(self, n, capsys):
        water_alerts(n)
        lines = capsys.readouterr().out.splitlines()
        for value in range(1, n + 1):
            if value % 12 == 0:
                assert lines[value - 1] == "Critical"
            elif value % 4 == 0:
                assert lines[value - 1] == "SaveWater"

    def test_returns_none(self):
        assert water_alerts(1) is None


class TestWeekendTemperatures:
    @pytest.mark.parametrize("temps, expected", [
        ([18, 25, 31, 22, 27], [25, 31, 27]),
        ([], []),
        ([25, 25, 24], [25, 25]),
        ([10, 11, 12], []),
        ([40, 0, 26], [40, 26]),
    ])
    def test_filtering(self, temps, expected):
        assert weekend_temperatures(temps) == expected

    def test_preserves_order_and_input(self):
        values = [29, 18, 25, 30]
        original = values.copy()
        assert weekend_temperatures(values) == [29, 25, 30]
        assert values == original

    def test_returns_list(self):
        assert isinstance(weekend_temperatures([25]), list)


class TestCalculateDeliveryFee:
    @pytest.mark.parametrize("distance, items, expected", [
        (10, 2, 52), (1, 5, 28), (1, 1, 20), (5, 1, 32),
        (10, 3, 52), (10, 4, 58), (0, 1, 20),
    ])
    def test_fee_calculation(self, distance, items, expected):
        assert calculate_delivery_fee(distance, items) == expected

    @pytest.mark.parametrize("items", [4, 5, 8])
    def test_extra_item_charge(self, items):
        assert calculate_delivery_fee(10, items) == 52 + (items - 3) * 6

    @pytest.mark.parametrize("distance", [0, 1, 2, 10])
    def test_minimum_and_distance(self, distance):
        assert calculate_delivery_fee(distance, 1) == max(20, 12 + 4 * distance)


class TestLibraryLoan:
    @pytest.mark.parametrize("balance, books, expected", [
        (0, 1, "Success: Loan approved"),
        (0, 5, "Success: Loan approved"),
        (1, 2, "Error: Outstanding balance"),
        (-10, 3, "Success: Loan approved"),
        (0, 0, "Error: Invalid book count"),
        (0, -1, "Error: Invalid book count"),
        (0, 6, "Error: Invalid book count"),
    ])
    def test_loan_rules(self, balance, books, expected):
        assert library_loan(balance, books) == expected


class TestLearnerQualifies:
    @pytest.mark.parametrize("attendance, mark, done, total, expected", [
        (75, 50, 4, 4, True), (90, 80, 10, 10, True),
        (74, 80, 4, 4, False), (75, 49, 4, 4, False),
        (75, 80, 3, 4, False), (75, 80, 0, 0, False),
    ])
    def test_qualification_rules(self, attendance, mark, done, total, expected):
        assert learner_qualifies(attendance, mark, done, total) is expected

    def test_exact_boundaries_pass(self):
        assert learner_qualifies(75, 50, 2, 2) is True

    def test_returns_boolean(self):
        assert isinstance(learner_qualifies(75, 50, 1, 1), bool)
