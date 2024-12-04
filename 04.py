import lib, re

def check_for_word(word, word_search, x, y, x_dir, y_dir):
    for letter in word:
        if y < 0 or y >= len(word_search) or x < 0 or x >= len(word_search[0]):
            return False

        current = word_search[y][x]
        if current != letter:
            return False
        y += y_dir
        x += x_dir

    return True

def p1():
    data = lib.read().split('\n')
    word = 'XMAS'

    matches = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            matches += check_for_word(word, data, x, y, 1, 0)
            matches += check_for_word(word, data, x, y, 1, -1)
            matches += check_for_word(word, data, x, y, 0, -1)
            matches += check_for_word(word, data, x, y, -1, -1)
            matches += check_for_word(word, data, x, y, -1, 0)
            matches += check_for_word(word, data, x, y, -1, 1)
            matches += check_for_word(word, data, x, y, 0, 1)
            matches += check_for_word(word, data, x, y, 1, 1)
    print(matches)


def p2():
    data = lib.read().split('\n')

    matches = 0
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (check_for_word('MAS', data, x, y, 1, 1)
                and check_for_word('MAS', data, x+2, y, -1, 1)):
                matches += 1
            elif (check_for_word('MAS', data, x, y, 1, 1)
                and check_for_word('SAM', data, x+2, y, -1, 1)):
                matches += 1
            elif (check_for_word('SAM', data, x, y, 1, 1)
                and check_for_word('MAS', data, x+2, y, -1, 1)):
                matches += 1
            elif (check_for_word('SAM', data, x, y, 1, 1)
                and check_for_word('SAM', data, x+2, y, -1, 1)):
                matches += 1
    print(matches)

p2()
