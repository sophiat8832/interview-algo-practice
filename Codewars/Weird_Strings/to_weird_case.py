def to_weird_case(words):
    word_list = list(words)
    i = 0
    for j in range(len(word_list)):
        if word_list[j] == " ":
            i = 0
        elif i % 2 == 0:
            word_list[j] = word_list[j].upper()
            i += 1
        else:
            word_list[j] = word_list[j].lower()
            i += 1
    return ''.join(word_list)