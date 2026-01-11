# Game logic - every 5 seconds
a = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour, minute=datetime.now().minute, second=datetime.now().second)
b = a + timedelta(0,5) # days, seconds, then other fields.

while datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day, hour=datetime.now().hour, minute=datetime.now().minute, second=datetime.now().second) != b:
    elem.click()
    print(datetime.now())
    print(b)


