from datetime import datetime,date
d=date(2007,5,31)
dayofyear=d.timetuple().tm_yday
print(dayofyear)
