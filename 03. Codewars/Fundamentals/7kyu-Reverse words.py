# training split() method

def reverse_words(text):
  #go for it
    split_txt = text.split(' ')
    return " ".join(s[::-1] for s in split_txt)