months = ["январь", "февраль", "март", "апрель",
          "май", "июнь", "июль", "август", "сентябрь", "октябрь",
          "ноябрь", "декабрь"]

def convert_to_iso(date):
    parts = date.split(".")
    if len(parts) == 3:
        day, month, year = parts
    else:
        parts = date.split()
        if len(parts) == 3:
            day = parts[0]
            month = parts[1]
            year = parts[2]
        else:
            return None

    month = month.lower()
    if month in months:
        month_index = months.index(month) + 1
    else:
        try:
            month_index = int(month)
            if month_index < 1 or month_index > 12:
                return None
        except ValueError:
            return None

    try:
        day_int = int(day)
        if day_int < 1 or day_int > 31:
            return None
    except ValueError:
        return None

    try:
        year_int = int(year)
    except ValueError:
        return None

    return f"{year_int:04}-{month_index:02}-{day_int:02}"

while True:
    date = input()
    iso_date = convert_to_iso(date)

    if iso_date is not None:
        print(f"Дата: {iso_date}")
        break
    else:
        print(" ")