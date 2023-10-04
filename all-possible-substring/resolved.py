from collections import Counter 
def minion_game(string):
    # your code goes here
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    vowels_in_string = list(set([vowel for vowel in string if vowel in vowels]))
    consonants_in_string = list(set([cons for cons in string if cons not in vowels]))
    vowels_indexes = [i for i, letter in enumerate(string) if letter in vowels_in_string]
    consonansts_indexes = [i for i, letter in enumerate(string) if letter in consonants_in_string]
    stuart_word_list = []
    kevin_word_list = []
    for j in vowels_indexes:
        for i in range(len(string)):
            if i>=j:
                kevin_word_list.append(string[j:i+1])
    for j in consonansts_indexes:
        for i in range(len(string)):
            if i>=j:
                stuart_word_list.append(string[j:i+1])
    stuart_score = sum(dict(Counter(stuart_word_list)).values())
    kevin_score = sum(dict(Counter(kevin_word_list)).values())
    print(Counter(stuart_word_list))
    print(Counter(kevin_word_list))
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print(f"Kevin {kevin_score}")




# def minion_game(string):
#     s=len(string)
#     vowel = 0
#     consonant = 0
     
#     for i in range(s):
#         if string[i] in 'AEIOU':
#            vowel+=(s-i)
#         else:
#            consonant+=(s-i)          
#     if vowel < consonant:
#         print('Stuart ' + str(consonant))
#     elif vowel > consonant:
#         print('Kevin ' + str(vowel))
#     else:
#         print('Draw')
# if __name__ == '__main__':
#     minion_game('Draw')