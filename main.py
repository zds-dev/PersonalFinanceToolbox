from models import *
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

predict_from =dt.datetime(2017, 1, 1)
predict_to = dt.datetime(2045, 1, 1)

# A sample of the power of this code. Working on a student loan calculator - aim to decide whether it is
# better to pay off the loan early or wait until the loan is written off.

if __name__ == "__main__":
    loans = []
    for years in range(2017, 2020):
        loans.append(YearlyInterestAccruing("student_loan", -9250, 1.06, dt.datetime(years, 1, 1)))
    figure = plt.figure()
    loans[0] = apply_regular_payment_into_asset(loans[0], 100, relativedelta(months=1), dt.datetime(2017, 1, 1), dt.datetime(2024, 1, 1))
    for loan in loans:
        plt.plot(loan.generate_timeseries(predict_to, predict_from, relativedelta(years=1)))

combinedAsset = loans[0] + loans[1] + loans[2]
plt.plot(combinedAsset.generate_timeseries(predict_to, predict_from, relativedelta(years=1)))
plt.show()