def convert_seconds(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)


    day_word = "день" if days % 10 == 1 and days % 100 != 11 else "дні" if 2 <= days % 10 <= 4 and not (
                12 <= days % 100 <= 14) else "днів"


    time_format = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    return time_format



print(convert_seconds(0))  # 0 днів, 00:00:00
print(convert_seconds(224930))  # 2 дні, 14:28:50
print(convert_seconds(466289))  # 5 днів, 09:31:29
print(convert_seconds(950400))  # 11 днів, 00:00:00
print(convert_seconds(1209600))  # 14 днів, 00:00:00
print(convert_seconds(1900800))  # 22 дні, 00:00:00
print(convert_seconds(8639999))  # 99 днів, 23:59:59
print(convert_seconds(22493))  # 0 днів, 06:14:53
print(convert_seconds(7948799))  # 91 день, 23:59:59