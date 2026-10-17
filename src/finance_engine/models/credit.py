from decimal import Decimal
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field

from finance_engine.constants import (
    MAX_CREDIT_AMOUNT,
    MAX_CREDIT_MONTHS,
    MAX_CREDIT_RATE,
)


class CreditInput(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
    )

    amount: Decimal = Field(
        gt=0,
        le=MAX_CREDIT_AMOUNT,
        title="Credit money",
        examples=[1000000.00],
    )
    rate: Decimal = Field(
        ge=0,
        le=MAX_CREDIT_RATE,
        title="Credit interest rate",
        description="The interest rate to be used for the credit",
        examples=[5.0],
    )
    months: int = Field(
        gt=0,
        le=MAX_CREDIT_MONTHS,
        title="Loan term",
        examples=[12],
    )


class Payment(BaseModel):
    """Details of a single loan payment."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
    )

    month: int = Field(
        gt=0,
        title="Month number",
        description="Sequential number of the payment in the loan repayment schedule.",
        examples=[1],
    )
    payment: Decimal = Field(
        ge=0,
        title="Payment amount",
        description="Total monthly payment amount: principal and interest.",
        examples=[9500.50],
    )
    debt_part: Decimal = Field(
        ge=0,
        title="Principal repayment",
        description="The portion of the payment allocated to repaying the principal.",
        examples=[8000.00],
    )
    interest_part: Decimal = Field(
        ge=0,
        title="Monthly interest",
        description="The portion of the payment accrued as loan interest.",
        examples=[1500.50],
    )
    remaining_balance: Decimal = Field(
        ge=0,
        title="Remaining debt",
        description="The remaining principal balance after a payment is made.",
        examples=[92000.00],
    )


class AnnuityResult(BaseModel):
    """Result of the loan calculation with annuity payments."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
    )

    monthly_payment: Decimal = Field(
        ge=0,
        title="Monthly payment",
        description="The amount of the monthly payment, which remains constant throughout the loan term.",  # noqa: E501
        examples=[8884.88],
    )
    over_payment: Decimal = Field(
        ge=0,
        title="Total interest paid",
        description="The total amount of interest paid in addition to the original loan amount.",  # noqa: E501
        examples=[6618.52],
    )
    total_payment: Decimal = Field(
        ge=0,
        title="Total repayment amount",
        description="The sum of all payments over the entire loan term, including principal and interest.",  # noqa: E501
        examples=[106618.52],
    )


class DifferentiatedResult(BaseModel):
    """Result of the loan calculation with differentiated payments."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
    )

    first_payment: Decimal = Field(
        ge=0,
        title="First payment",
        description="Amount of the first scheduled payment.",
        examples=[9333.33],
    )
    last_payment: Decimal = Field(
        ge=0,
        title="Final payment",
        description="The amount of the final scheduled payment.",
        examples=[8416.67],
    )
    over_payment: Decimal = Field(
        ge=0,
        title="Total interest paid",
        description="The total amount of interest accrued over the entire loan term.",
        examples=[6500.00],
    )
    total_payment: Decimal = Field(
        ge=0,
        title="Total payment amount",
        description="The sum of all payments over the entire loan term.",
        examples=[106500.00],
    )
    schedule: list[Payment] = Field(
        title="Payment schedule",
        description="List of payments broken down by principal, interest, and outstanding balance.",  # noqa: E501
    )
