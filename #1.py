def start_end_day(datestart="2000.06.23",dateend="2017.07.10"):
    datestartlist = datestart.split(".")
    yearstart = int(datestartlist[0])
    monthstart = int(datestart[1])
    daystart = int(datestartlist[2])
    dateendlist = dateend.split(".")
    yearend = int(dateendlist[0])
    monthend = int(dateendlist[1])
    dayend = int(dateendlist[2])
    print "start:", yearstart, monthstart,daystart
    print "end:", yearend, monthend, dayend
    return yearstart, monthstart, daystart, yearend, monthend, dayend

def year_numbers(year):
    year_days = 0
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        year_days = 1
    return year_days + 365

def countmonth(year, month):
    year_days = year_numbers(year)
    if year_days == 365:
        if month == 1:
            days = 0
        elif month == 2:
            days = 31
        elif month == 3:
            days = 31 + 28
        elif month == 4:
            days = 31 + 28 + 31
        elif month == 5:
            days = 31 + 28 + 31 + 30
        elif month == 6:
            days = 31 + 28 + 31 + 30 + 31
        elif month == 7:
            days = 31 + 28 + 31 + 30 + 31
        elif month == 8:
            days = 31 + 28 + 31 + 30 + 31 + 30
        elif month == 9:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31
        elif month == 10:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 30
        elif month == 11:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31+ 30 + 31
        elif month == 12:
            days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 30 + 31 + 30
        return days
    else:
        if month == 1:
            days = 0
        elif month == 2:
            days = 31
        elif month == 3:
            days = 31 + 29
        elif month == 4:
            days = 31 + 29 + 31
        elif month == 5:
            days = 31 + 29 + 31 + 30
        elif month == 6:
            days = 31 + 29 + 31 + 30 + 31
        elif month == 7:
            days = 31 + 29 + 31 + 30 + 31
        elif month == 8:
            days = 31 + 29 + 31 + 30 + 31 + 30
        elif month == 9:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31
        elif month == 10:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 30
        elif month == 11:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31+ 30 + 31
        elif month == 12:
            days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 30 + 31 + 30
        return days

def countyears(year):
    days = 0
    years = range(1, year)
    for year_item in years:
        days += year_numbers(year_item)
    return days

#
days = countyears(2000) + countmonth(2000, 06) + 23
print days

days2 =  countyears(2017) + countmonth(2017, 07) + 10
print days2
print days2-days