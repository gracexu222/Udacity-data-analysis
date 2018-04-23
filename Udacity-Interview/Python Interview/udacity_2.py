"""
Question 2
Given a string a, find the longest palindromic substring contained in a.
Your function definition should look like question2(a), and return a string.
"""
# @param {string} s input string
# @return {bool} if string is palindrome or not
def isPalindrome(s):
    if not s:
        return False
    # reverse compare
    return s == s[::-1]

# @param {string} s input string
# @return {string} the longest palindromic substring
def question2(s):
    if not s:
        return ""

    n = len(s)
    longest, left, right = 0, 0, 0
    for i in xrange(0, n):
        for j in xrange(i + 1, n + 1):
            substr = s[i:j]
            if isPalindrome(substr) and len(substr) > longest:
                longest = len(substr)
                left, right = i, j
    # construct longest substr
    result = s[left:right]
    return result

# Main program
def main():
    print question2("ABCBACADCBBCDA")

if __name__ == '__main__':
    main()
