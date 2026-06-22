date = input()

day, month, year = date.split("-")

months = {
    "JAN": "01",
    "FEB": "02",
    "MAR": "03",
    "APR": "04",
    "MAY": "05",
    "JUN": "06",
    "JUL": "07",
    "AUG": "08",
    "SEP": "09",
    "OCT": "10",
    "NOV": "11",
    "DEC": "12"
}

day_num = int(day)

if day_num >= 80:
    full_year = 1900 + day_num
else:
    full_year = 2000 + day_num

month_num = months[month]
new_day = int(year)

if full_year % 400 == 0 or (full_year % 4 == 0 and full_year % 100 != 0):
    print(f"({new_day}, {month_num}, {full_year}) is a leap year")
else:
    print(f"({new_day}, {month_num}, {full_year}) is not a leap year")