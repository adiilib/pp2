from datetime import datetime, timezone, timedelta

def parse(s):
    date_part, tz_part = s.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    sign = 1 if '+' in tz_part else -1
    h, m = map(int, tz_part[4:].split(':'))
    offset = timezone(sign * timedelta(hours=h, minutes=m))
    
    return dt.replace(tzinfo=offset).astimezone(timezone.utc)

d1 = parse(input())
d2 = parse(input())

seconds = abs((d1 - d2).total_seconds())
print(int(seconds // 86400))