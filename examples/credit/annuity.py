from decimal import Decimal

from finance_engine.engine import FinanceEngine


def main():
    finance = FinanceEngine()

    result = finance.credits.annuity(
        amount=Decimal("300_000.00"),
        rate=Decimal("5.0"),
        months=120,
    )

    print("Loan (annuity payments)")
    print(f"Monthly payment: {result.monthly_payment}")
    print(f"Overpayment: {result.over_payment}")
    print(f"Total paid: {result.total_payment}")


if __name__ == "__main__":
    main()
