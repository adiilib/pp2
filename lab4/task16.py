from datetime import datetime, timedelta, timezone

def parse(s):
    dt, tz = s.rsplit(' ', 1)
    dt = datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")
    sign = 1 if '+' in tz else -1
    h, m = map(int, tz[4:].split(':'))
    return dt.replace(tzinfo=timezone(sign*timedelta(hours=h, minutes=m))).astimezone(timezone.utc)

start, end = parse(input()), parse(input())
print(int((end - start).total_seconds()))