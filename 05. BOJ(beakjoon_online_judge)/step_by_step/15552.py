import sys
iter = int(input())

for i in range(iter):
  a, b = map(int, sys.stdin.readline().split())
  print(a + b)