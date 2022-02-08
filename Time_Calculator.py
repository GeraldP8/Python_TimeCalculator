#add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

#add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

#add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

#import additional modules

import datetime

def add_time(start, duration, day=""):

    #Get our dictionary mapping
    switch = {'Monday':"1900-01-01 00:00:00.000000",
              'Tuesday':"1900-01-02 00:00:00.000000",
              'Wednesday':"1900-01-03 00:00:00.000000",
              'Thursday':"1900-01-04 00:00:00.000000",
              'Friday':"1900-01-05 00:00:00.000000",
              'Saturday':"1900-01-06 00:00:00.000000",
              'Sunday':"1900-01-07 00:00:00.000000",
              "":"1900-01-01 00:00:00.000000"
    }

    #Set a anchor date to use
    anchor_date = switch[day]

    #Convert time into 24h format
    time24_ampm = start[-2:]
    time24 = start[:len(start) - 2].split(":")[0]
    timemin = start[:len(start) - 2].split(":")[1]
    timeText = time24 + ":00 " + time24_ampm.lower()

    

    timeswitch = {
             "12:00 am":"00:00:00",
             "1:00 am":"01:00:00",
             "2:00 am":"02:00:00",
             "3:00 am":"03:00:00",
             "4:00 am":"04:00:00",
             "5:00 am":"05:00:00",
             "6:00 am":"06:00:00",
             "7:00 am":"07:00:00",
             "8:00 am":"08:00:00",
             "9:00 am":"09:00:00",
             "10:00 am":"10:00:00",
             "11:00 am":"11:00:00",
             "12:00 pm":"12:00:00",
             "1:00 pm":"13:00:00",
             "2:00 pm":"14:00:00",
             "3:00 pm":"15:00:00",
             "4:00 pm":"16:00:00",
             "5:00 pm":"17:00:00",
             "6:00 pm":"18:00:00",
             "7:00 pm":"19:00:00",
             "8:00 pm":"20:00:00",
             "9:00 pm":"21:00:00",
             "10:00 pm":"22:00:00",
             "11:00 pm":"23:00:00",
    }
    #print(timemin)

    time24hr = timeswitch[timeText]


    #Build anchor datetime format
    anchor_datetime = anchor_date[:10] + " " + time24hr.split(":")[0] + ":" + timemin.rstrip() + ":00"

    #Get hours to add
    addHours = duration.split(":")[0]
    addMinutes = duration.split(":")[1]

    #new time
    #print(anchor_datetime)
    #"1900-01-01 00:00:00.000000"

    castDate = datetime.datetime.strptime(anchor_datetime, '%Y-%m-%d %H:%M:%S')
    new_time  = castDate + datetime.timedelta(hours = int(addHours)) + datetime.timedelta(minutes = int(addMinutes))

    #Calculate days past
    daysPast = int(str(str(new_time).split("-")[2:3])[2:4]) - int(str(anchor_datetime.split("-")[2:3])[2:4])

    new_time = daysPast

    return new_time

print(add_time("6:30 PM", "205:12", ""))