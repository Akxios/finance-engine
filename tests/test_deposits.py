from decimal import Decimal

import pytest

from finance_engine.services.deposits import DepositService


@pytest.fixture
def service() -> DepositService:
    return DepositService()


def test_simple_interest(
    service: DepositService,
) -> None:
    result = service.simple_interest(
        amount=Decimal("100_000"),
        rate=Decimal("5"),
        days=90,
    )

    assert result.interest == Decimal("1232.88")


def test_compound_interest(
    service: DepositService,
) -> None:
    result = service.compound_interest(
        amount=Decimal("100_000"),
        rate=Decimal("5"),
        days=90,
        compounds_per_year=12,
    )

    assert result.interest == Decimal("1237.91")
