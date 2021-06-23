def count_sheeps(sheep):
  # TODO May the force be with you

    # reference: python list comprehension - if else
    # https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension
    sheep = [s if s is not None else 0 for s in sheep]
    
    return sum(sheep)