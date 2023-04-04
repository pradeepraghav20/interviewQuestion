

# from datetime import datetime
from datetime import timedelta

from datetime import *
def calculate_subscription(date,month,pmc):
    total_days=month*30
    per_day_charge=total_days/pmc

    Begindate = datetime.strptime(date, "%Y-%m-%d")
    print("Beginning date")
    print(Begindate)

    # # calculating end date by adding 10 days
    # Enddate = Begindate + timedelta(days=10)



calculate_subscription("2022/06/19", 1, 1000)