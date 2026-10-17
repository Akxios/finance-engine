from finance_engine.services.credits import CreditService
from finance_engine.services.deposits import DepositService
from finance_engine.services.savings import SavingsService


class FinanceEngine:
    """Main entry point for the financial calculation engine."""

    def __init__(self) -> None:
        self.credits: CreditService = CreditService()
        self.deposits: DepositService = DepositService()
        self.savings: SavingsService = SavingsService()
