'''
merge_the_tools has the following parameters:
string s: the string to analyze
int k: the size of substrings to analyze
Prints
Print each subsequence on a new line. 
There will be n/k of them. No return value is expected.
'''
import textwrap as t
def merge_the_tools(string, k):
    k = len(string) // k
    new =  t.wrap(string, k)
    print(new)
    for i in new:
        for j in i:
            if i.count(j) > 1:
                print(new)
         
                
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)