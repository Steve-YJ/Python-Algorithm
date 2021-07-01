def words_to_marks(s):
    # Easy one
    word = 'abcdefghijklmnopqrstuvwxyz'
    
    return sum([word.index(w)+1 for w in s])