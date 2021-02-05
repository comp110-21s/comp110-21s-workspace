"""A vaccination calculator."""

__author__ = "730403391"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


p: int = int(input("Population: "))
d_a: int = int(input("Doses administered: "))
d_p_d: int = int(input("Doses per day: "))
inserted_target_value: int = int(input("Target percent vaccinated: "))
working_target_percentage: float = (inserted_target_value / 100)
f_v: int = int(d_a / 2)
full_dose_per_day: int = int(d_p_d / 2)
t_n_p: int = round(working_target_percentage * p)
people_left: int = int(t_n_p - f_v)


days: timedelta = timedelta(people_left / full_dose_per_day)
today: datetime = datetime.today()
future: datetime = today + days
print("We will reach" " " +  str(inserted_target_value) + "%" + " " "vaccination in "  + str(round(people_left / full_dose_per_day)) + " " "days, which falls on" " " +  str(future.strftime("%B %d, %Y")) + ".")
