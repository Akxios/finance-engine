class FinanceError(Exception):
    """Base class for exceptions in this module"""


class InvalidIncomeError(FinanceError):
    """Income is invalid"""


class InvalidMonthError(FinanceError):
    """Month is invalid"""


class InvalidAmountError(FinanceError):
    """Amount is invalid"""


class InvalidRateError(FinanceError):
    """Rate is invalid"""


class InvalidYearError(FinanceError):
    """Year is invalid"""


class InvalidDaysError(FinanceError):
    """Day is invalid"""
