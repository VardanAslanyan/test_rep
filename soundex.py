

word = 'nmTymczak'

def soundex(text: str) -> str:
    letters = {'b': '1', 'f': '1', 'p': '1', 'v': '1', 'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2',
              'x': '2', 'z': '2', 'd': '3', 't': '3', 'l': '4', 'm': '5', 'n': '5', 'a': '0',
              'r': '6', 'e': '0', 'i': '0', 'o': '0', 'u': '0', 'y': '0', 'h': '0', 'w': '0', '': ''}
    all_letter = 'aeiouyhwbfpvcgjkqsxzdtlmnr'
    text_low = ''.join(j.lower() for j in text if j in all_letter)
    print(text_low)

    code = text_low[0].upper()
    count = 0
    g = ''
    for i in text_low:
        print(i, letters[i])
        if letters[i] != letters[g] and letters[i] != '0':
            code += letters[i]
            count += 1
        g = i
        if count == 3:
            break

    return code


print(soundex(word))




