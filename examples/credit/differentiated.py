from decimal import Decimal

import finance_engine as engine
from finance_engine.models.credit import Payment


def main():

    result = engine.credits.differentiated(
        amount=Decimal("300_000.00"),
        rate=Decimal("5.0"),
        months=120,
    )

    print("Loan (differentiated payments)")
    print(f"First payment: {result.first_payment}")
    print(f"Last payment: {result.last_payment}")
    print(f"Total paid: {result.total_payment}")
    print(f"Over payment: {result.over_payment}")

    payment: Payment
    for payment in result.schedule:
        print(
            f"Month: {payment.month}, payment - {payment.payment}, "
            + f"remaining balance - {payment.remaining_balance}"
        )


if __name__ == "__main__":
    main()
