def remove_duplicate_words(strings):
    duplicate = []
    answer = ""
    
    for s in strings.split():
        if s not in duplicate:
            answer = answer + s + " "
            duplicate.append(s)
            
    return answer[:-1]