"""Convert a number in base-10 into a written out number in English."""
"""Get person to put a number in and return a ineger and get a string"""
# print("Please type a number between 1 and 99")
# # def input_num(num):
# #     return num = int(input("A number bewteen 1 and 99: "))
# num = int(input('A number between 1 and 99: '))
#
# tens = num // 10
# ones = num % 10
def get_tens_word(tens):
    if tens == 9:
        tens_word = 'ninety'
    elif tens == 8:
        tens_word = 'eighty'
    elif tens == 7:
        tens_word = 'seventy'
    elif tens == 6:
        tens_word = 'sixty'
    elif tens == 5:
        tens_word = 'fifty'
    elif tens == 4:
        tens_word = 'fourty'
    elif tens == 3:
        tens_word = 'thirty'
    elif tens == 2:
        tens_word = 'twenty'
    return tens_word

def get_ones_word(ones):
    if ones == 9:
        ones_word = 'nine'
    elif ones == 8:
        ones_word = 'eight'
    elif ones == 7:
        ones_word = 'seven'
    elif ones == 6:
        ones_word = 'six'
    elif ones == 5:
        ones_word = 'five'
    elif ones == 4:
        ones_word = 'four'
    elif ones == 3:
        ones_word = 'three'
    elif ones == 2:
        ones_word = 'two'
    elif ones == 1:
        ones_word = 'one'
    return ones_word


def make_teens_word(num):
    if num == 11:
        output = "eleven"
    elif num == 12:
        output = "twelve"
    elif num == 13:
        output = "thirteen"
    elif num == 14:
        output = "fourteen"
    elif num == 15:
        output = "fifteen"
    elif num == 16:
        output = "sixteen"
    elif num == 17:
        output = "seventeen"
    elif num == 18:
        output = "eighteen"
    elif num == 19:
        output = "nineteen"
    return output
    # continute with all teen numbers

def main():

    num = int(input('Please type a number between 1 and 99: '))

    if num == 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19:
        final_word = make_teens_word(num)
        print(final_word)
    else:
        tens = num // 10
        ones = num % 10

        tens_word = get_tens_word(tens)
        ones_word = get_ones_word(ones)
        print(tens_word)
# print(get_ones_word(ones))
# print(output(intager))

main()
