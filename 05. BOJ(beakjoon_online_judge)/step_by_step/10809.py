# BOJ.10809.알파벳 찾기(finding alphabet)


value = str(input())  # e.g. baekjoon
alphabets = 'abcdefghijklmnopqrstuvwxyz'
# make list of alphabets
alphabets = [alphabet for alphabet in alphabets]
# make result list
result = [-1] * 26

# iterate alphabets and check if it exists
for idx, alphabet in enumerate(alphabets):
    if alphabet in value:
        result[idx] = value.index(alphabet)
        
# format output
result = " ".join(str(elem) for elem in result)
print(result)