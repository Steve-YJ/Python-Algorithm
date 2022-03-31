# get hour, minutes
hour, min = map(int, input().split())
# get crime
ctime = int(input())
# calculate minutes
minutes = 60 * hour + min + ctime
# calc hour, min
hour = minutes // 60
min = minutes % 60
# condition
if hour >= 24:  # if hour over 24
  hour -= 24
# return result 
print(hour, min)