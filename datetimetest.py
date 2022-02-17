from datetime import datetime

now = datetime.now()
print(now)
print(type(now))
nowYMD = now.strftime("%Y-%m-%d")
nowData = now.strftime("%H:%M:%S")
print(nowYMD)
print(nowData)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)