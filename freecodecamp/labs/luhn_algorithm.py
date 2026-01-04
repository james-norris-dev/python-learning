# build a credit card validator using the Luhn algorithm

def verify_card_number(digits):
    cleaned_digits = ''.join(x for x in digits if x.isdigit())
    reversed_digits = cleaned_digits[::-1]
    sum_digits = 0
    for index, digit in enumerate(reversed_digits):
        if index % 2 != 0:
            result = int(digit) * 2
            if result > 9:
                result -= 9
                sum_digits += result
            else:
                sum_digits += result
        else:
            sum_digits += int(digit)

    if sum_digits % 10 == 0:
        return 'VALID!'
    else:
        return 'INVALID!'