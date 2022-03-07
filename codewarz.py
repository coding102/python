# VOWEL COUNT
# %%
def get_count(sentence):
    vowel_num = 0  # counter
    for i in sentence:  # loop through sentence
        if i in "AEIOUaeiou":  # does letter in sentence match any of these vowels?
            vowel_num = vowel_num + 1  # if so add it to the counter
    return vowel_num


print(get_count('aeiouaeiou'))


# %%
