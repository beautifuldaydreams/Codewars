#Description:
#Write Number in Expanded Form
#You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
#expanded_form(12) # Should return '10 + 2'
#expanded_form(42) # Should return '40 + 2'
#expanded_form(70304) # Should return '70000 + 300 + 4'
#NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    front_digits = [int(char) for char in str(num)][::-1]
    reverse = []
    for i, val in enumerate(front_digits):
        val *= 10**i
        reverse.append(str(val))
    return " + ".join(i for i in reverse[::-1] if int(i) != 0)
