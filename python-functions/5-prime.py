def is_prime(number):
    is_prime_number = False

    if number == 1:
        return is_prime_number
    else:
        if number > 1:
            for i in range(2, number):
                if (number % i) == 0:
                    is_prime_number = True
                    break

            if is_prime_number:
                is_prime_number = False
            else:
                is_prime_number = True

    return is_prime_number
