from . import jalali
from django.utils import timezone


def persian_numbers_converter(mystr):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for english_num, persian_num in numbers.items():
        mystr = mystr.replace(english_num, persian_num)
    return mystr


def jalali_converter(time):
    jmonth = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد','شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']

    time = timezone.localtime(time)

    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonth):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    def get_clock():
        minute = str(time.minute)
        if len(minute) == 1:
            minute += '0'
        hour = str(time.hour)
        if len(hour) == 1:
            hour = '0' + hour
        return hour + ":" + minute
    output = "{} {} {} , ساعت {}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        get_clock(),
    )

    return persian_numbers_converter(output)
