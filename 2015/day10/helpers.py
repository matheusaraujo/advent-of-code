def look_and_say(number):
    digit, copies, result = number[0], 1, ""
    for i in range(1, len(number)):
        if number[i] != digit:
            result += str(copies) + digit
            digit, copies = number[i], 1
        else:
            copies += 1

    return result + str(copies) + digit


def look_and_say_n(initial_number, n):
    number = initial_number
    for _ in range(n):
        number = look_and_say(number)
    return len(number)
