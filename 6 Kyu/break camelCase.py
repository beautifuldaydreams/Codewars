# Description:
# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# solution("camelCasing")  ==  "camel Casing"

def solution(s):
    return "".join([i if i.islower() else " " + i for i in s ])
