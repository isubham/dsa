
def is_palindrome(word):
    reversed_word = "".join(list(reversed(list(word))))
    return word == reversed_word

def no_of_palindromes(sentence):
    '''
    :param sentence:
    :return: all palindromes
    '''
    palindrome_count = 0
    words = sentence.split(" ")
    for word in words:
        if is_palindrome(word):
            palindrome_count += 1
    return palindrome_count


# print(is_palindrome("aba") == True)

print(no_of_palindromes("aba bcb abc") == 2)


