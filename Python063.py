# Recursion

def CutLetters(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
       
        return CutLetters(word[1:])
    return word[0] + CutLetters(word[1:])

print(CutLetters("wwwooorrrllldd"))