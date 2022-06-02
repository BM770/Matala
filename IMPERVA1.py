# B"H

def isLeapYear(year):
    """
    Check if a year is a leap year
        :param year: year to check
        :type year: int
        :return: True if its a leap year, False if not
    """
    if year % 100 == 0 and not year % 400 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def daysInMonth(month, year):
    """
    Get number of days in a specific month & year
        :param month: month to check
        :type month: int
        :param year: year to check
        :type year: int
        :return: number of days in a specific month & year
    """
    daysInMonth = {
        1: 31,
        2: 29 if isLeapYear(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    return daysInMonth[month]


def addDaysToDate(date, daysToAdd):
    """
    Get new date after adding days to the provided date
        :param date: date to check
        :type date: str
        :param days: days to add
        :type days: int
        :return: new date
    """
    day, month, year = map(int, date.split("."))
    if (day + daysToAdd <= daysInMonth(month, year)):
        return f"{(day + daysToAdd):02d}.{month:02d}.{year:04d}"
    else:
        daysToReachNextMonth = daysInMonth(month, year) - day + 1
        newDaysToAdd = daysToAdd - daysToReachNextMonth
        newDay = 1
        newMonth = (month + 1) % 12
        newYear = year + 1 if month == 12 else year
        newDate = ".".join([str(newDay), str(newMonth), str(newYear)])
        return addDaysToDate(newDate, newDaysToAdd)


def checkMyFunction(date, daysToAdd):
    """
    Check if the function I wrote work as expected
        :param date: date to check
        :type date: str
        :param days: days to add
        :type days: int
        :return: True if my solution is expected, raise exception if not
    """
    from datetime import datetime
    from datetime import timedelta
    expectedSolution = datetime.strptime(date, "%d.%m.%Y") + timedelta(days=daysToAdd)
    expectedSolution = expectedSolution.strftime("%d.%m.%Y")
    mySolution = addDaysToDate(date, daysToAdd)
    if mySolution == expectedSolution:
        print(f'Got the expected solution={expectedSolution}')
    else:
        raise Exception(f"The solution ({mySolution}) is different from the expected ({expectedSolution})")


checkMyFunction('10.01.2008', 10)
checkMyFunction('29.06.2020', 8)
checkMyFunction('29.12.2020', 8)
