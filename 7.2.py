first_sentence = input("Enter your first sentence: ")
second_sentence = input("Enter your second sentence: ")


def sentence_transformer(str1, str2):

    for string in [str1, str2]:
        if string[-1] not in ['.', '!', '?']:
            print(string[0].upper() + string[1:] + '.')
        else:
            print(string[0].upper() + string[1:])


sentence_transformer(first_sentence, second_sentence)
