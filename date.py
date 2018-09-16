import datetime


numdays =20
base = datetime.datetime.today()
date_list = [base - datetime.timedelta(days=x) for x in range(0, numdays)]

print(date_list[0].strftime('%Y%m%d') + 'a')

