
'''
str -> vowels -> reverse vowel 
'''



def reverse_vowels_after_filtering(vowel_strs):
    vowels_set = {'a', 'e', 'i', 'o', 'u'} 

    str_chars = list(vowel_strs)
    vowels = []

    for i, char in enumerate(str_chars):

        if vowels_set.__contains__(char):
            vowels.append(char)
            str_chars[i] = ''
            
    vowels.reverse()
    vowel_counter = 0
    for i, char in enumerate(str_chars):
        if char == '':
            str_chars[i] = vowels[vowel_counter]
            vowel_counter += 1 
    
    reverse_vowels_after_filtering_ = "".join(str_chars)
    return reverse_vowels_after_filtering_


print(reverse_vowels_after_filtering('aegeg') == 'eegag')
