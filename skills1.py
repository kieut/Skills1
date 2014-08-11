# Things you should be able to do.

# turn return into return!

# Write a function that takes a list and returns a new list with only the odd numbers.

def all_odd(some_list):
    odd_list = []
    for num in some_list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    even_list = []
    for num in some_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for word in word_list:
        if len(word) > 4:
            new_list.append(word)
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    x = some_list[0]
    for num in some_list:
        if num <= x:
            x = num
    return x

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    x = 0
    for num in some_list:
        if num > x:
            x = num
    return x

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []
    for num in some_list:
        half = float(num) / 2
        new_list.append(half)
    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for word in word_list:
        word_length = len(word)
        new_list.append(word_length)
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    mult_total = 1
    for num in numbers:
        mult_total = mult_total * num
    return mult_total


# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    single_string = ""
    for word in string_list:
        single_string += str(word) + " "
    return single_string


# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    sum = 0
    for num in numbers:
        sum += num

    print float(sum)/len(numbers)

# function calls with test lists
# some_list = [13, 50, 2, 14]
# word_list = ['I', 'have', 'a', 'puppy', 'named', 'raymond']

# all_odd(some_list)

# all_even(some_list)

# long_words(word_list)

# smallest(some_list)

# largest(some_list)

# halvesies(some_list)

# word_lengths(word_list)

# sum_numbers(some_list)

# mult_numbers(some_list)

# join_strings(word_list)

# average(some_list)

    