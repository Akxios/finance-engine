from decimal import Decimal

from finance_engine import FinanceEngine


def main():
    finance = FinanceEngine()

    result = finance.deposits.compound_interest(
        amount=Decimal("100_000"),
        rate=Decimal("5.0"),
        days=365,
        compounds_per_year=12,
    )

    print(f"Compound interest income: {result.interest}")


if __name__ == "__main__":
    main()
