from decimal import Decimal
from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field

from finance_engine.constants import MAX_CONTRIBUTION_AMOUNT, MAX_SAVING_MONTHS


class ProjectionInput(BaseModel):
    """Input data for savings projection."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
    )

    monthly_contribution: Decimal = Field(
        gt=0,
        le=MAX_CONTRIBUTION_AMOUNT,
        title="Monthly savings contribution",
        examples=[25000.00],
    )
    months: int = Field(
        12,
        gt=0,
        le=MAX_SAVING_MONTHS,
        title="Months of contributions",
        description="Number of months of savings contributions",
        examples=[12],
    )


class ProjectionResult(BaseModel):
    """Result of a savings projection."""

    model_config: ClassVar[ConfigDict] = ConfigDict(
        strict=True,
        frozen=True,
        extra="forbid",
    )

    total_contribution: Decimal = Field(
        gt=0,
        title="Total accumulated amount",
        description="The amount you have accumulated over a certain number of months",
        examples=[100000.00],
    )
