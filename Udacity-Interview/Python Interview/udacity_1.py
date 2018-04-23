"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
"""

# Turn on/off to enable/disable debugging
debug = True

# Find out if s1 and s2 strings are anagram of each other
# @param {string, string} input strings
# @return {bool} if strings are anagram of each other or not
def is_anagram(s1, s2):
    s1 = list(s1)
    # Sort a string and then compare with each other
    s1.sort()   # Quick sort O(n*log(n))
    return s1 == s2

# Find out sorted(possible substring of s) and compare with sorted(t).
# @param {string, string} input strings
# @return {bool} Question1 answer
def question1(s, t):
    global debug
    match_length = len(t)
    pattern_length = len(s)
    sorted_t = list(t)
    sorted_t.sort()     # Quick sort O(n*log(n))

    for i in range(pattern_length - match_length + 1):
        if debug:
            print (s[i: i+match_length], t)
        if is_anagram(s[i: i+match_length], sorted_t):
            return True
    return False

# Main program
def main():
    print question1("udacity", "ad")

if __name__ == '__main__':
    main()

"""
String S
String t

Case 1: ("udacity", "ad") -> True
string with 2 characters reversed from order in S

Case 2: ("udacity", "da") -> True
string with 2 characters same as in order in S

Case 3: ("udacity", "au") -> False
string with 2 alternative characters and reversed from order in S

Case 4: ("udacity, dacity") -> True
string with 6 characters same as in order in S

Case 4: ("udacity", "ciy") -> False
string with 2 characters same as in order in S and 1 character out of order.

Case 5: ("udacity", "xyz") -> False
string with new characters not in string S.

Case 5: ("udacity", "") -> True
empty string.

Case 6: ("ad", "udacity" ) -> False
string t's length is greater than string S.
"""
