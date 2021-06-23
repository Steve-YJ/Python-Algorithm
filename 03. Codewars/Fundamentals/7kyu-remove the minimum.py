def remove_smallest(numbers):
#     raise NotImplementedError("TODO: remove_smallest")
    if len(numbers) < 1:  # https://redfox.tistory.com/34
        return numbers
        
    idx = numbers.index(min(numbers))
#     print(idx)
    return numbers[0:idx] + numbers[idx+1:]