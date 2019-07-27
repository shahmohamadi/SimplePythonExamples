# calculate number of words with specific length in a string


def n_words_in_s(string, n):
    number_of_n_words = 0
    words = string.split()
    for this_word in words:
        if len(this_word) == n:
            number_of_n_words = number_of_n_words + 1
    return number_of_n_words


string = input("what is your string: ")

for n in range(1, 12):
    number = n_words_in_s(string, n)
    print("here is ", number, "word(s) with length of ", n, "in string")



