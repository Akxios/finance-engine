from decimal import Decimal

from finance_engine import FinanceEngine


def main():
    finance = FinanceEngine()

    result = finance.savings.projection(
        monthly_contribution=Decimal("50_000"),
        months=12,
    )

    print(f"{result.total_contribution} accumulated")


if __name__ == "__main__":
    main()
