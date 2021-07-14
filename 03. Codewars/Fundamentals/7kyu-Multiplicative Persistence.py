def per(n):
    if len(str(n)) == 1:
        return []
    else:
        results = []
        result = 1
        
        while True:
            if len(str(n)) == 1:
                return results
            for e in str(n):
                result *= int(e)
            results.append(result)  # append result
            n = result  # update n to result
            result = 1  # initialization
        