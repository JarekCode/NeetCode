'''
https://leetcode.com/problems/valid-anagram/description/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

s = "anagram"
t = "nagaram"

# Time: O(n) | Space O(n)
def solution1(s, t):
    if len(s) != len(t):
        return False
    s_map = {}
    t_map = {}
    # Gather information on word 's'
    for letter in s:
        if letter not in s_map:
            s_map[letter] = 1
        else:
            s_map[letter] += 1
    # Gather information on word 't'
    for letter in t:
        if letter not in t_map:
            t_map[letter] = 1
        else:
            t_map[letter] += 1
    # Compare word 's' to word 't'
    for i in s_map:
        if i not in t_map:
            return False
        if s_map[i] != t_map[i]:
            return False
    return True

# Time: O(n) | Space O(n)
def solution2(s, t):
    if len(s) != len(t):
        return False
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        if s.count(letter) != t.count(letter):
            return False
    return True

print(solution1(s, t))
print(solution2(s, t))