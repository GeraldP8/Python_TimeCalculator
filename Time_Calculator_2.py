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


def add_time(start, duration, day=""):

    #Cleanse day data into proper case
    if day.lower() == "monday":
        day = "Monday"
    elif day.lower() == "tuesday":
        day = "Tuesday"
    elif day.lower() == "wednesday":
        day = "Wednesday"
    elif day.lower() == "thursday":
        day = "Thursday"
    elif day.lower() == "friday":
        day = "Friday"
    elif day.lower() == "saturday":
        day = "Saturday"
    elif day.lower() == "sunday":
        day = "Sunday"

    timeswitch = {
             "12:00 am":"0:00:00",
             "1:00 am":"1:00:00",
             "2:00 am":"2:00:00",
             "3:00 am":"3:00:00",
             "4:00 am":"4:00:00",
             "5:00 am":"5:00:00",
             "6:00 am":"6:00:00",
             "7:00 am":"7:00:00",
             "8:00 am":"8:00:00",
             "9:00 am":"9:00:00",
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

    dayOfWeekSwitch = {
        "Monday":1,
        "Tuesday":2,
        "Wednesday":3,
        "Thursday":4,
        "Friday":5,
        "Saturday":6,
        "Sunday":7
    }

    #The idea is to convert all values to minutes, then increment the hour counter untill it reaches 24 then we increment the daycounter by 1 and set hourcounter back to 0
    #We try and achieve a 24hr model that we just convert back to the am/pm model using the dictionary
    time24_ampm = start[-2:]
    time24 = start[:len(start) - 2].split(":")[0]
    timemin = start[:len(start) - 2].split(":")[1]
    timeText = time24 + ":00 " + time24_ampm.lower()

    startTime = timeswitch[timeText]
    #Convert time into 24h format


    #Convert time into 24h format
    dur_timehour = duration[:len(duration)].split(":")[0]
    dur_timemin = duration[:len(duration)].split(":")[1]

    HourAdd = int(dur_timemin) + int(timemin)
    
    minutes = 0


    dayCounter = 0
    hourCounter = startTime.split(":")[0]
    minCounter =  (int(dur_timehour) * 60)

    
 
    if HourAdd >= 60:
        hourCounter = int(hourCounter) + 1
        minutes = int(HourAdd) - 60
    elif HourAdd < 60:
        minutes = HourAdd



    newHour = 0
    while int(minCounter) >= 0:
        
        newHour = newHour + 1

        if newHour >= 60:
            newHour = 0
            hourCounter = int(hourCounter) + 1


        if hourCounter == 24:
            hourCounter = 0
            dayCounter = int(dayCounter) +1
        
        minCounter = int(minCounter) - 1


    if len(str(minutes)) == 1:
        minutes = "0" + str(minutes)
    #Build new time in 24hr fashion
    dictLookup = str(hourCounter) + ':00:00' 
  
    ampmval = ""
    #Reverse lookup dictionary to get the am/pm format string
    for key in timeswitch.items():
        if key[1] == dictLookup:
            ampmval = key[0]

   
    #print(dictLookup)
    timeString = ampmval.split(":")[0] + ":"  + str(minutes) + " " + ampmval.split(":")[1][-2:].upper()
    #Build the days string
    if dayCounter < 1:
        dayString = ""
    elif dayCounter == 1:
        dayString = " (next day)"
    elif dayCounter > 1:
        dayString = " (" + str(dayCounter) + " days later)"
    
    #Check which day it is supposed to be now
    newDay = ""
    if len(day) > 0:
        if dayCounter == 0:
            newDay = ", " + day + " "
        elif dayCounter >= 1:
            initialDay = dayOfWeekSwitch[day]

            while dayCounter >= 1:
                initialDay = initialDay + 1
                if initialDay == 8:
                    initialDay = 1
                
                #Increment looping variable
                dayCounter = dayCounter - 1
            #print(dayCounter)
    
    #print(initialDay)
    #Reverse lookup dictionary to get the am/pm format string
    if len(day) > 1:
        for key in dayOfWeekSwitch.items():
            if key[1] == initialDay:
                newDay = ", " + key[0]

    new_time = timeString + newDay + dayString
    

    return new_time


print(add_time("11:59 PM", "24:05", "Wednesday"))



 #   def test_two_days_later_with_day(self):
 #       actual = add_time("11:59 PM", "24:05", "Wednesday")
 #       expected = "12:04 AM, Friday (2 days later)"
 #       self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:59 PM", "24:05", "Wednesday" to return "12:04 AM, Friday (2 days later)"')