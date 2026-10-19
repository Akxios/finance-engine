from decimal import Decimal

import finance_engine as engine


def main():

    loan_comparison = engine.credits.loan_comparison(
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
