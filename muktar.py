def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(5, 5))  # Output should be 10


def is_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is not even")

is_even(4)  # Output should be "4 is even"


def reverse_string(text):
    return text[::-1]  # Correctly reverses the string

print(reverse_string("hello"))  # Example usage


def count_vowels(text):
    vowels = 'aeiou'
    text = text.lower()
    return sum(1 for char in text if char in vowels)

print(count_vowels("hello"))  # Example usage


def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

print(calculate_factorial(5))  # Example usage


def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def sample_function():
    print("Sample function executed")

sample_function()  # Demonstrates decorator usage


def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

# Example usage
example_list = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
sorted_list = sort_by_age(example_list)
print(sorted_list)  # Output should be [('Bob', 25), ('Alice', 30), ('Charlie', 35)]


def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output should be {'a': 1, 'b': 5, 'c': 4}


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

car = Car('Toyota', 'Hilux', 2000)
car.display_info()  # Output should be car details
