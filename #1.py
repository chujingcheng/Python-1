from Tkinter import *

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
    days = 0
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

def countIt():
    startdate = start_var.get()
    enddate = end_var.get()
    yearstart, monthstart, daystart, yearend, monthend, dayend = start_end_day(startdate, enddate)
    days = countyears(yearstart) + countmonth(yearstart, monthstart) + daystart
    print days

    days2 =  countyears(yearend) + countmonth(yearend, monthend) + dayend
    print days2
    intervel =  days2-days
    print intervel
    result_var.set(intervel)
    return 0

lable_width = 20
entry_width = 40
button_width = 50
root = Tk()
root. title("Days Counting!")
info = Label(root, text="Welcome!", width = button_width)
info.grid(row=0, column=0, columnspan=2)
start_info = Label(root,text = "Start Date", width=lable_width)
start_info.grid(row=1,column=0)
start_var = StringVar()
start_var.set("2000.06.23")
start_Entry = Entry(root, width=entry_width, textvariable = start_var)
start_Entry.grid(row=1, column=1)
end_info = Label(root, text="End Date:", width=lable_width)
end_info.grid(row=2, column=0)
end_var = StringVar()
end_var.set("2017.07.11")
end_Entry = Entry(root, width=entry_width, textvariable=end_var)
end_Entry.grid(row=2, column=1)


submit_button = Button(text = "count days", command = countIt, width = button_width)
submit_button.grid(row=3, column=0, columnspan=2)
res_info = Label(root, text="days in between", width=lable_width)
res_info.grid(row=4,column=0)
result_var = StringVar()
result_Entry = Entry(root, width=entry_width, textvariable=result_var, state="disabled")
result_Entry.grid(row=4, column=1)

root.mainloop()



