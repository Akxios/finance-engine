from decimal import Decimal

from finance_engine.engine import FinanceEngine


def main():
    finance = FinanceEngine()

    loan_comparison = finance.credits.loan_comparison(
        amount=Decimal("300_000.00"),
        rate=Decimal("5.0"),
        months=120,
    )

    print(
        "The total interest paid on an annuity-based loan will "
        + f"amount to {loan_comparison}, compared to a loan with a declining "
        + "(differentiated) payment schedule."
    )


if __name__ == "__main__":
    main()
