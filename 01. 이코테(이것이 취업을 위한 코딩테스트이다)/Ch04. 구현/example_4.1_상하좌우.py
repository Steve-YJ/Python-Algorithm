"""
상.하.좌.우
* 다시 한 번 구현을 해보았다
* 조금 더 간결하면서 직관적인 코드를 작성할 수 없을까?
"""

n = int(input())

moving_plan = list(map(str, input().split()))

# starting point is seted to [1, 1]
row = 1
col = 1

# traveler will travel as planed
# moveing_types are 'L', 'R', 'U', 'D'
for m in moving_plan:
    if m == 'U':
        next_row = row - 1
        next_col = col + 0
    elif m == 'D':
        next_row = row + 1
        next_col = col + 0
    elif m == 'L':
        next_row = row + 0
        next_col = col - 1
    elif m == 'R':
        next_row = row + 0
        next_col = col + 1
    
    # traveler must be in the travel_map
    if next_row >= 1 and next_row <= n and next_col >= 1 and next_col <= n:
        # update row and col
        row = next_row
        col = next_col

print(row, col)
