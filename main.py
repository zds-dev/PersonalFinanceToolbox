from personalfinancetoolbox.models import *
from personalfinancetoolbox.functions import *
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta
import datetime as dt

predict_from = dt.datetime(2021, 1, 1)
predict_to = dt.datetime(2030, 1, 1)

# A sample of the power of this code. Working on a student loan calculator - aim to decide whether it is
# better to pay off the loan early or wait until the loan is written off.

if __name__ == "__main__":
    loans = []
    for years in range(2017, 2020):
        loans.append(Debt("student_loan", -9250, 1.06, dt.datetime(years, 1, 1), 'yearly'))
    figure = plt.figure()
    rem = apply_regular_payment_into_debt(loans[0], 500, relativedelta(months=1), dt.datetime(2017, 1, 1), dt.datetime(2024, 1, 1))
    print("Paid off debt with repayment amount remaining "+str(rem))
    for loan in loans:
        val, times = loan.generate_timeseries(predict_to, predict_from, relativedelta(days=1))
        plt.plot(times, val)

combinedAsset = loans[0] + loans[1] + loans[2]
val, times = combinedAsset.generate_timeseries(predict_to, predict_from, relativedelta(years=1))
plt.plot(times, val)
plt.show()