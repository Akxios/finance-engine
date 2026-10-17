from decimal import ROUND_HALF_UP, Decimal

from finance_engine.models.deposit import (
    CompoundInterestInput,
    DepositInterestResult,
    SimpleInterestInput,
)


class DepositService:
    @staticmethod
    def simple_interest(
        amount: Decimal,
        rate: Decimal,
        days: int,
        days_per_year: int = 365,
    ) -> DepositInterestResult:

        data = SimpleInterestInput(
            amount=amount,
            rate=rate,
            days=days,
            days_per_year=days_per_year,
        )

        interest = (
            data.amount
            * data.rate
            * Decimal(data.days)
            / (Decimal(data.days_per_year) * Decimal("100"))
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )

        return DepositInterestResult(interest=interest)

    @staticmethod
    def compound_interest(
        amount: Decimal,
        rate: Decimal,
        days: int,
        days_per_year: int = 365,
        compounds_per_year: int = 12,
    ) -> DepositInterestResult:

        data = CompoundInterestInput(
            amount=amount,
            rate=rate,
            days=days,
            days_per_year=days_per_year,
            compounds_per_year=compounds_per_year,
        )

        principal = data.amount
        annual_rate = data.rate / Decimal("100")

        period_rate = annual_rate / Decimal(compounds_per_year)
        years = Decimal(days) / Decimal(days_per_year)
        periods = Decimal(compounds_per_year) * years

        factor = (Decimal("1") + period_rate) ** periods
        final_amount = principal * factor
        interest = final_amount - principal

        interest = interest.quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )

        return DepositInterestResult(interest=interest)
