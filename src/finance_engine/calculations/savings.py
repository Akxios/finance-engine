from decimal import ROUND_HALF_UP, Decimal

from finance_engine.models.saving import (
    ProjectionInput,
    ProjectionResult,
)


def projection(
    monthly_contribution: Decimal,
    months: int,
) -> ProjectionResult:

    data = ProjectionInput(
        monthly_contribution=monthly_contribution,
        months=months,
    )

    monthly_contribution = data.monthly_contribution * data.months

    total = monthly_contribution.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP,
    )

    return ProjectionResult(
        total_contribution=total,
    )
