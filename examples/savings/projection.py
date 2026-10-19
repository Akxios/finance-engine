from decimal import Decimal

import finance_engine as engine


def main():

    result = engine.savings.projection(
        monthly_contribution=Decimal("50_000"),
        months=12,
    )

    print(f"{result.total_contribution} accumulated")


if __name__ == "__main__":
    main()
