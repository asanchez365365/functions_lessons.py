# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.

def all_positives(list):
      for num in list:
        if num <= 0:
            return False
        return True




# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.


def sum_less(list):
    total = 0
    for num in list:
        if 0 < num < 1000:
            total += num
    return total



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.

def count_even (numbers):
    return sum (1 for x in numbers if x % 2 == 0)

number= [1,2,3,4,5,6]

count_even(numbers)