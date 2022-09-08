#Week 9 Exploration 2A

import datetime

graduation = datetime.date(2022, 6, 11)
hoy = datetime.date.today()
timedelta = graduation - hoy


print('There are ' + str(timedelta) + ' until graduation')


