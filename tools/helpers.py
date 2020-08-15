"""Helper functions used across multiple scripts."""

__author__ = "Kris Jordan <kris@cs.unc.edu>"

from datetime import datetime


def date_prefix(suffix: str) -> str:
    """Generate a date prefixed string given a suffix.
    
    Args:
        suffix: Will follow the date and a dash.

    Returns:
        A str in the format of "YY.MM.DD-HH.MM-{suffix}"
    """
    now = datetime.now()
    prefix = f"{str(now.year)[2:]}.{now.month:02}.{now.day:02}-{now.hour:02}.{now.minute:02}"
    return f"{prefix}-{suffix}"
