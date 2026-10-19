from decimal import Decimal

import finance_engine as engine


def test_annuity() -> None:

    result = engine.credits.annuity(
        amount=Decimal("1_000_000.00"),
        rate=Decimal("5.1"),
        months=12,
    )

    assert result.monthly_payment == Decimal("85653.31")
    assert result.over_payment == Decimal("27839.78")
    assert result.total_payment == Decimal("1027839.78")


def test_differentiated() -> None:
    result = engine.credits.differentiated(
        amount=Decimal("1_000_000.00"),
        rate=Decimal("2.5"),
        months=12,
    )

    assert result.first_payment == Decimal("85416.67")
    assert result.last_payment == Decimal("83506.94")
    assert result.total_payment == Decimal("1013541.67")
    assert result.over_payment == Decimal("13541.67")
