from decimal import Decimal

import finance_engine as engine


def main():

    result = engine.deposits.simple_interest(
        amount=Decimal("100_000"),
        rate=Decimal("5"),
        days=365,
    )

    print(f"Simple interest income: {result.interest}")


if __name__ == "__main__":
    main()
