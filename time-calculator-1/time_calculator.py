def add_time(start, duration, day=None):

    day_map = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }

    timely, midday = start.split()
    hour, minutes = timely.split(':')
    hour = int(hour)
    minutes = int(minutes)

    if midday == "PM":
        hour += 12

    duration_hour, duration_minutes = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)

    total_minutes = minutes + duration_minutes
    ans_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = hour + duration_hour + extra_hours

    ans_hour = (total_hour % 24) % 12

    if ans_hour == 0:
        ans_hour = 12
    ans_hour = str(ans_hour)

    total_day = (total_hour // 24)

    ans_midday = ""
    if (total_hour % 24) <= 11:
        ans_midday = "AM"
    else:
        ans_midday = "PM"

    if ans_minutes <= 9:
        ans_minutes = '0' + str(ans_minutes)
    else:
        ans_minutes = str(ans_minutes)

    time_stamp = ans_hour + ":" + ans_minutes + ' ' + ans_midday
    if day == None:
        if total_day == 0:
            return time_stamp
        if total_day == 1:
            return time_stamp + ' (next day)'
        return time_stamp + ' (' + str(total_day) + ' days later)'
    else:
        ans_day = (day_map[day.lower().capitalize()] + total_day) % 7
        for i, j in day_map.items():
            if j == ans_day:
                ans_day = i
                break
        if total_day == 0:
            return time_stamp + ', ' + ans_day
        if total_day == 1:
            return time_stamp + ', ' + ans_day + ' (next day)'
        return time_stamp + ', ' + ans_day + ' (' + str(
            total_day) + ' days later)'
