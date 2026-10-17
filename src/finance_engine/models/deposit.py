from decimal import Decimal
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field

from finance_engine.constants import (
    MAX_ANNUAL_RATE,
    MAX_DEPOSIT_AMOUNT,
    MAX_DEPOSIT_DAYS,
)


class DepositInterestInput(BaseModel):
    """Input data for deposit interest."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
    )

    amount: Decimal = Field(
        gt=0,
        le=MAX_DEPOSIT_AMOUNT,
        title="Deposit amount",
        description="Total deposit amount.",
        examples=[100000.00],
    )
    rate: Decimal = Field(
        ge=0,
        le=MAX_ANNUAL_RATE,
        title="Deposit interest rate",
        description="The interest rate to be used for the deposit",
        examples=[5.0],
    )
    days: int = Field(
        ge=0,
        le=MAX_DEPOSIT_DAYS,
        title="Deposit duration",
        description="The number of days the deposit will remain open",
        examples=[365],
    )
    days_per_year: int = Field(
        365,
        ge=365,
        le=366,
        title="Days in a year",
        description="Number of days in a year",
        examples=[365],
    )


class SimpleInterestInput(DepositInterestInput):
    """Input data for deposit simple interest."""

    pass


class CompoundInterestInput(DepositInterestInput):
    """Input data for deposit compound interest."""

    compounds_per_year: int = Field(
        12,
        gt=0,
        title="Number of capitalizations per year",
        description="The deposit will yield different returns depending on the capitalization frequency",  # noqa: E501
        examples=[12],
    )


class DepositInterestResult(BaseModel):
    """Result of a deposit interest."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
    )

    interest: Decimal = Field(
        ge=0,
        title="Deposit interest",
        description="Interest to be earned on the deposit over the holding period",
        examples=[1000.00],
    )
