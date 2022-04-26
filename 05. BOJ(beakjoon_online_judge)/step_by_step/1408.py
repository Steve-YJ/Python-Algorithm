# 13:52:30
# 14:00:00
# 00:07:30

now = str(input())
target = str(input())

n_hour = now.split(":")[-3]
n_hour = int(n_hour)
n_min = now.split(":")[-2]
n_min = int(n_min)
n_sec = now.split(":")[-1]
n_sec = int(n_sec)

t_hour = target.split(":")[-3]
t_hour = int(t_hour)
t_min = target.split(":")[-2]
t_min = int(t_min)
t_sec = target.split(":")[-1]
t_sec = int(t_sec)


r_hour = t_hour - n_hour
r_min = t_min - n_min
r_sec = t_sec - n_sec


# print(f"r_hour: {r_hour}")
# print(f"r_min: {r_min}")
# print(f"r_sec: {r_sec}")


if t_sec < n_sec:
    r_min -= 1
    r_sec = 60 + r_sec
else:
    r_sec = r_sec

if t_min < n_min:
    r_hour -= 1
    r_min = 60 + r_min
else:
    r_min = r_min

if t_hour < n_hour:
    r_hour += 24
    
# print(f"r_hour: {r_hour}")
# print(f"r_min: {r_min}")
# print(f"r_sec: {r_sec}")


if r_hour < 10:
    r_hour = str("0") + str(r_hour)
if r_min < 10:
    r_min = str("0") + str(r_min)
if r_sec < 10:
    r_sec = str("0") + str(r_sec)

print(str(r_hour) + ":" + str(r_min) + ":" + str(r_sec))