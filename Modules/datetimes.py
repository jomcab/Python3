from datetime import datetime

# Creating a date using year, month, day as arguments.
birthday = datetime(1993, 7, 26, 4, 30, 15)

print("Year:", birthday.year)
print("Month:", birthday.month)
print("Day:", birthday.day)
print("Hour:", birthday.hour)
print("Minute:", birthday.minute)
print("Weekday:", birthday.weekday())

# Creating a date using datetime.now()
print("Now:", datetime.now())

# Parsing a date using strptime
parsed_date = datetime.strptime('Jan 15, 2022', '%b %d, %Y')
print("parsed_date using strptime():",parsed_date)

# Rendering a date as a string using strftime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print("formatted date using strftime():", date_string)