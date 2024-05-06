def verify_card_number(card_number):
    # create a verification function, used for checking the card is compatible with the Luhn Alogrithm definition
    sum_of_odd_digits = 0
    reversed_card_number = card_number[::-1]
    # creating a reversed_card_number to make the card variable being in reverse
    odd_numbers = reversed_card_number[::2]
    # picking the numbers of the reversed card that are odd

    for digit in odd_numbers:
        sum_of_odd_digits += int(digit)
        # sum all odd digits and storing it in sum_of_odd_digits
        
    sum_of_even_numbers = 0
    # using the reversed card variable I pick the even numbers with [1::2]
    even_numbers = reversed_card_number[1::2]
    for digit in even_numbers:
        # making the product of each number in even_numbers variable
        number = int(digit) * 2
        if number >= 10:
            # making a conditional for the numbers that are greater than 10 to divide them in, for instance, if we have a 12 in our credit car, it divides our number in 1+2 and add it to number var
            number = (number // 10) + (number % 10)
        sum_of_even_numbers += number

    total = sum_of_even_numbers + sum_of_odd_digits
    # sum the even numbers and odd numbers
    print(total)
    return total % 10 == 0
    # returning a kind of conditional to verify it in the next function easier

card_number_input = input('Enter your credit card number here to check its validity, ej(4111-1111-4555-1142): ')
def main(card_number_input):
    
    translation = str.maketrans({'-': '', ' ': ''})
    card_number_translated = card_number_input.translate(translation)
# verification:
    if verify_card_number(card_number_translated):
        print('VALID!')
    else:
        print('INVALID!')

main(card_number_input)