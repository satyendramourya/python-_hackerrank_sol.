import calendar as cal
# print(cal.calendar(2020,2,1,5,3))  --> 
# print(cal.firstweekday())
# print(cal.isleap(1600)) #----------> year
# print(cal.leapdays(2000,2020))       #---------->year , year
# print(cal.month(2022,5,2,1))       #---------->year,month,weidth ,height
# print(cal.monthrange(2022,5))         #---------->year , month
# cal.prcal(2020)        #----------> year
# cal.prmonth(2020,5)       #---------->year,month
# cal.setfirstweekday(6)
# print(cal.prmonth(2020,5))
# print(cal.weekday(2020,5,21))
# print(list(cal.month_name))
# print(list(cal.day_name))
# print(cal.monthcalendar(2020,5))
# print(cal.weekheader(10))       #----------> for formating the heading

month, date , year = map(int,input().split())
print(cal.day_name[cal.weekday(year , month,date)].upper())
print(cal.weekday(year , month,date))
