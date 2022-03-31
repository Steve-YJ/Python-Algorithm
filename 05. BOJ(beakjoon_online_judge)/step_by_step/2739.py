n = int(input())
step = 1

while True:
  if step == 10:
    break
  else:
    print(f"{n} * {step} = {n * step}")
    step += 1