'''
Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
Scoring
A player gets +1 point for each occurrence of the substring in the string S.
'''
def count_substring(string, sub_string):
    total = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            total += 1
    return total
def minion_game(string):
    stuart = 0
    kevin = 0
    vowels = 'AEIOU'  
    newk = []
    news = []  
    for i in range(len(string)):
        for i in range(len(string[i:])):
            if string[i] in vowels:
                newk.append(string[i:])
                kevin = sum([count_substring(string, i) for i in set(newk)])  
            else:
                news.append(string[i:])
                stuart = sum([count_substring(string, i) for i in set(news)])
    print(newk)
    print(news)
    if kevin > stuart:
        print(f'Kevin {kevin}')
    if kevin == stuart:
        print('Draw')
    else:
        print(f'Stuart {stuart}')
        

if __name__ == '__main__':
    s = input()
    minion_game(s)