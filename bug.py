def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 0 as expected

my_list = [1,2,3,4,5]
average = calculate_average(my_list)
print(f"The average is: {average}") #This will print 3.0 as expected

my_list = [1,2, 'a', 4, 5] #This will throw an error
average = calculate_average(my_list)
print(f"The average is: {average}")