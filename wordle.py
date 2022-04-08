DIR = r"C:\Users\Eyal\Downloads\a03ef2cba789d8cf00c08f767e0fad7b-28804271b5a226628d36ee831b0e36adef9cf449" \
      r"\a03ef2cba789d8cf00c08f767e0fad7b-28804271b5a226628d36ee831b0e36adef9cf449\wordle-answers-alphabetical.txt "
LIST_OF_WORDS = open(DIR, "r")
LIST_OF_WORDS = LIST_OF_WORDS.read()
LIST_OF_WORDS = LIST_OF_WORDS.split()


# get rid of double letters


def grey_possibilities(grey_list, list_of_words=LIST_OF_WORDS):
    possible = []
    for item in list_of_words:
        is_valid = True
        for let in grey_list:
            if let in item:
                is_valid = False
        if is_valid:
            possible.append(item)
    return [len(possible), possible]


def green_possibilities(str_word, list_of_words=LIST_OF_WORDS):
    possible = []
    for item in list_of_words:
        is_valid = True
        for i in range(len(str_word)):
            if str_word[i] != '_' and str_word[i] != item[i]:
                is_valid = False
        if is_valid:
            possible.append(item)
    return [len(possible), possible]


def yellow_possibilities(str_word, list_of_words=LIST_OF_WORDS):
    possible = []
    for item in list_of_words:
        is_valid = True
        for i in range(len(str_word)):
            if str_word[i] != '_' and (str_word[i] not in item or str_word[i] == item[i]):
                is_valid = False
        if is_valid:
            possible.append(item)
    return [len(possible), possible]


def out_grey(grey_list, list_of_words=LIST_OF_WORDS):
    possible = []
    for item in list_of_words:
        is_valid = True
        for let in item:
            if let not in grey_list:
                is_valid = False
        if is_valid:
            possible.append(item)
    return [len(possible), possible]


def wordle(list_of_all=LIST_OF_WORDS):
    max_len = 0
    best = ""
    for word1 in list_of_all:
        count = 0
        for word2 in list_of_all:
            lst = []
            for let in str(word1):
                if str(let) in str(word2) and let not in lst:
                    count += 1
                    lst.append(let)
        if count > max_len:
            max_len = count
            best += " " + word1
    return best


def one_turn():
    words_left = LIST_OF_WORDS
    count_turns = 1
    while len(words_left) > 1 and count_turns <= 6:
        grey_list_str = input("please enter the greys")
        grey_list = grey_list_str.split(" ")
        print(grey_possibilities(grey_list, list_of_words=words_left)[0])
        words_left = grey_possibilities(grey_list, list_of_words=words_left)[1]
        ####################################################################
        yellow_list_str = input("please enter the yellows")
        print(yellow_possibilities(yellow_list_str, list_of_words=words_left)[0])
        words_left = yellow_possibilities(yellow_list_str, list_of_words=words_left)[1]
        ####################################################################
        green_list_str = input("please enter the greens")
        # green_list = green_list_str.split(" ")
        print(green_possibilities(green_list_str, list_of_words=words_left)[0])
        words_left = green_possibilities(green_list_str, list_of_words=words_left)[1]
        ####################################################################
        print(wordle(list_of_all=words_left))
        count_turns += 1


print(one_turn())
