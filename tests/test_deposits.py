from decimal import Decimal

import finance_engine as engine


def test_simple_interest() -> None:
    result = engine.deposits.simple_interest(
        amount=Decimal("100_000"),
        rate=Decimal("5"),
        days=90,
    )

    assert result.interest == Decimal("1232.88")


def test_compound_interest() -> None:
    result = engine.deposits.compound_interest(
        amount=Decimal("100_000"),
        rate=Decimal("5"),
        days=90,
        compounds_per_year=12,
    )

    assert result.interest == Decimal("1237.91")
