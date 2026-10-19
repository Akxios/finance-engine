from decimal import ROUND_HALF_UP, Decimal

from finance_engine.constants import CENT
from finance_engine.models.credit import (
    AnnuityResult,
    CreditInput,
    DifferentiatedResult,
    Payment,
)


def _round_money(value: Decimal) -> Decimal:
    return value.quantize(
        CENT,
        rounding=ROUND_HALF_UP,
    )


def differentiated(
    amount: Decimal,
    rate: Decimal,
    months: int,
) -> DifferentiatedResult:

    data = CreditInput(
        amount=amount,
        rate=rate,
        months=months,
    )

    monthly_rate = data.rate / Decimal("12") / Decimal("100")
    fixed_debt_part = data.amount / Decimal(data.months)

    schedule: list[Payment] = []
    current_balance = data.amount
    total_interest = Decimal("0")

    for month in range(1, data.months + 1):
        interest_part = current_balance * monthly_rate
        total_interest += interest_part

        monthly_payment = fixed_debt_part + interest_part
        current_balance -= fixed_debt_part

        schedule.append(
            Payment(
                month=month,
                payment=_round_money(monthly_payment),
                debt_part=_round_money(fixed_debt_part),
                interest_part=_round_money(interest_part),
                remaining_balance=max(
                    Decimal("0"),
                    _round_money(current_balance),
                ),
            )
        )

    total_payment = data.amount + total_interest

    return DifferentiatedResult(
        first_payment=schedule[0].payment,
        last_payment=schedule[-1].payment,
        total_payment=_round_money(total_payment),
        over_payment=_round_money(total_interest),
        schedule=schedule,
    )


def annuity(
    amount: Decimal,
    rate: Decimal,
    months: int,
) -> AnnuityResult:

    data = CreditInput(
        amount=amount,
        rate=rate,
        months=months,
    )

    monthly_rate = data.rate / Decimal("1200")

    if monthly_rate == 0:
        monthly_payment = data.amount / Decimal(data.months)
    else:
        factor = (Decimal("1") + monthly_rate) ** data.months

        coefficient = monthly_rate * factor / (factor - Decimal("1"))

        monthly_payment = data.amount * coefficient

    total_payment = monthly_payment * data.months
    over_payment = total_payment - data.amount

    return AnnuityResult(
        monthly_payment=_round_money(monthly_payment),
        over_payment=_round_money(over_payment),
        total_payment=_round_money(total_payment),
    )


def loan_comparison(
    amount: Decimal,
    rate: Decimal,
    months: int,
) -> Decimal:
    annuity_result = annuity(
        amount=amount,
        rate=rate,
        months=months,
    )

    differentiated_result = differentiated(
        amount=amount,
        rate=rate,
        months=months,
    )

    return annuity_result.total_payment - differentiated_result.total_payment
