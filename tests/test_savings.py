from decimal import Decimal

import pytest
from pydantic import ValidationError

import finance_engine as engine


def test_projection() -> None:
    result = engine.savings.projection(
        monthly_contribution=Decimal("50000.00"),
        months=12,
    )

    assert result.total_contribution == Decimal("600000.00")


@pytest.mark.parametrize(
    ("monthly_contribution", "months"),
    [
        (Decimal("0"), 12),
        (Decimal("-100"), 12),
        (Decimal("50000"), 0),
        (Decimal("50000"), -1),
    ],
)
def test_projection_rejects_invalid_input(
    monthly_contribution: Decimal,
    months: int,
) -> None:
    with pytest.raises(ValidationError):
        _ = engine.savings.projection(
            monthly_contribution=monthly_contribution,
            months=months,
        )
