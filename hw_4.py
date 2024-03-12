from datetime import datetime, timedelta

def find_next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            days_until_birthday = (birthday_this_year - today).days

            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year
                if congratulation_date.weekday() >= 5:
                    congratulation_date = find_next_weekday(congratulation_date, 0)

                congratulation_date_str = congratulation_date.strftime('%Y.%m.%d')

                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": congratulation_date_str
                })

        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')

    return upcoming_birthdays

users = [  # Список користувачів з їхніми датами народження
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith1", "birthday": "1990.03.19"},
    {"name": "Jane Smith2", "birthday": "1990.03.07"},
    {"name": "Jane Smith3", "birthday": "1990.03.15"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
