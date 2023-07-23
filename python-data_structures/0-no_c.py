def no_c(my_string):
    new_string = ""

    for i in range(len(my_string)):
        str_char = my_string[i]

        if str_char.lower() != "c":
            new_string += str_char

    return new_string
