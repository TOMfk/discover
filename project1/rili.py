def is_leap_year(year):
    """
    判断闰年
    :param year:
    :return:
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_num_of_days_in_month(year, month):
    """
    获得每月的天数
    :param year:
    :param month:
    :return:
    """
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif is_leap_year(year):
        return 29
    return 28


def get_total_num_of_days(year, month):
    """
    获得1800年输入年月总天数
    :param year:
    :param month:
    :return:
    """
    days = 0
    for y in range(1800, year):
        if is_leap_year(y):
            days += 366
        else:
            days += 365

    for m in range(1, month):
        days += get_num_of_days_in_month(year, m)

    return days


def get_start_day(year, month):
    """
    获得输入年月的第一天星期几
    :param year:
    :param month:
    :return:
    """
    day = (3 + get_total_num_of_days(year, month)) % 7
    if day == 0:
        day = 7
    return day


# print(get_start_day(2018, 7))
# print()


def print_table_head(year, month):
    print(str(month) + "月                                           " + str(year) + "年")
    print("-----------------------------------------------------")

    l = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    for i in l:
        print(format(i, "4"), end=" ")


def print_calendar(year, month):

    print_table_head(year, month)
    days = get_num_of_days_in_month(year, month)
    start_day_of_week = get_start_day(year, month)
    # print(start_day_of_week)

    l = []

    # for i in range(start_day_of_week):
    while start_day_of_week > 0:
        l.append("")
        start_day_of_week -= 1

    for day in range(1, days + 1):
        l.append(day)

    for i in range(len(l)):
        print(format(l[i], '6'), end=" ")
        if i % 7 == 0:
            print()
        i -= 1


# print_calendar(2018, 7)
