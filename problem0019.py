months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1900
curr_day = 1
first_sun_count = 0

while year < 2001:
    for i in range(len(months)):
        days = months[i]
        if (i == 1) and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            days += 1
        curr_day += days
        curr_day = curr_day % 7
        if curr_day == 0 and year != 1900:
            first_sun_count += 1
    year += 1

print(first_sun_count)