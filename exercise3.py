import random

random_numbers = [random.randint(1,10) for _ in range(15)] # Generating 15 random numbers using list comprehension
print(random_numbers)

# Convert random numbers to a set
unique_numbers = set(random_numbers)

print(f"unique numbers: {unique_numbers}")

