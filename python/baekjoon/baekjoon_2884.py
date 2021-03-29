# baekjooin_2884 알람시계

hour, min = list(map(int, input().split()))
# set_time = 45
result = None
set_time = min - 45
if set_time >= 0:
    min = set_time
    result = [hour, min]
elif set_time < 0:
    hour -= 1
    if hour < 0:
        hour = 24 - abs(hour)
    min = 60 - abs(set_time)
    result = [hour, min]

print(f'{result[0]} {result[1]}')