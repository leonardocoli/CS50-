#So that we can automate some tests of your code, we ask that your program’s last line of output be AMEX\n or MASTERCARD\n or VISA\n or INVALID\n.
#For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
#Best to use get_int or get_string from CS50’s library to get users’ input, depending on how you to decide to implement this one.


#American Express uses 15-digit numbers, MasterCard uses 16-digit numbers, and Visa uses 13- and 16-digit numbers.
#American Express numbers start with 34 or 37
#MasterCard numbers start with 51, 52, 53, 54, or 55
#Visa numbers start with 4

#luhn algorithm
#Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
#Add the sum to the sum of the digits that weren’t multiplied by 2.
#If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!

Number = int(input("Card number?"))


def luhn_algorithm(Card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(Card_number)
    #print(digits)

    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]

    check_sum = 0
    check_sum += sum(odd_digits)

    for i in even_digits:
        check_sum += sum(digits_of(i*2)) #soma final luhn algorithm

    last_digit_check_sum = check_sum % 10 #ultimo digito soma luhn algorithm

    if last_digit_check_sum == 0:
        return True
    else:
        print("INVALID\n")
        return False

#luhn_algorithm(Number)


digits =  [int(d) for d in str(Number)]

first_two = ''.join(map(str, digits[0:2]))
first_d = str(digits[0])

amex = ["34", "37"]
master_card = ["51", "52", "53", "54", "55"]
visa = ["4"]


if luhn_algorithm(Number):
    if first_two in amex and len(digits) == 15:
        print("AMEX\n")
    elif first_two in master_card and len(digits) == 16:
        print("MASTERCARD\n")
    elif first_d in visa and len(digits) in [13, 16]:
        print("VISA\n")
    else:
        print("INVALID\n")
else:
    print("INVALID\n")
