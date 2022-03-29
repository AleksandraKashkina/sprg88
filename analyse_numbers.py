
def is_whole_number(number):
       if (number % 1 == 0) and (number > 0):
           return True


       return False

my_numbers = [1, 2, 3]
for my_number in my_numbers:
    print(is_whole_number(my_number))
