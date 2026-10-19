from decimal import ROUND_HALF_UP, Decimal

from finance_engine.constants import CENT


def remaining_qty(
    target_qty: int,
    current_qty: int,
) -> int:
    """Calculation of the remainder up to the target quantity"""

    return max(target_qty - current_qty, 0)


def progress_percent(
    current_qty: int,
    target_qty: int,
) -> Decimal:
    """Calculation of progress toward a goal"""

    if target_qty == 0:
        return Decimal("0.00")

    percent = Decimal(current_qty) / Decimal(target_qty) * 100

    return percent.quantize(Decimal(CENT), rounding=ROUND_HALF_UP)


def is_target_reached(
    current_qty: int,
    target_qty: int,
) -> bool:
    """Verification of goal achievement"""

    return current_qty >= target_qty


def calculate_average_price(
    current_qty: int,
    average_price: Decimal | None,
    purchase_qty: int,
    purchase_price: Decimal,
) -> Decimal:
    """Calculation of the weighted average price"""

    if purchase_qty <= 0:
        return average_price or Decimal("0")

    previous_cost = (average_price or Decimal("0")) * Decimal(current_qty)
    purchase_cost = purchase_price * Decimal(purchase_qty)
    new_qty = current_qty + purchase_qty

    if new_qty <= 0:
        return Decimal("0")

    average = (previous_cost + purchase_cost) / Decimal(new_qty)
    return average.quantize(Decimal("0.00000001"), rounding=ROUND_HALF_UP)


def calculate_total_invest(
    current_qty: int,
    average_price: Decimal | None,
) -> Decimal:
    """Calculating the value of a position based on the average price"""

    if current_qty <= 0 or average_price is None:
        return Decimal("0")

    total_invest = current_qty * Decimal(average_price)

    return total_invest.quantize(
        Decimal("0.00000001"),
        rounding=ROUND_HALF_UP,
    )


def cost_basis(
    average_price: Decimal,
    current_qty: int,
) -> Decimal:
    """Calculation of the initial cost of a position"""

    value = average_price * Decimal(current_qty)
    return value.quantize(Decimal(CENT), rounding=ROUND_HALF_UP)


def return_percent(
    market_value: Decimal,
    basis: Decimal,
) -> Decimal:
    """Calculation of yield relative to purchase cost"""

    percent = (market_value - basis) / basis * Decimal("100")
    return percent.quantize(Decimal(CENT), rounding=ROUND_HALF_UP)
