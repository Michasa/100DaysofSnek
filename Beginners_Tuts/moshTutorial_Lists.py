harijuku_girls = ['Love 💗', 'Angel 👼', "Music 🎵", 'Baby 👶', 'Gwen']
print(harijuku_girls[2:4])

# Exercise
numbers = [4, 5, 10, 5, 99, 99, 4, 400]
large_number = numbers[0]

for number in numbers:
    if number > large_number:
        large_number = number

print(large_number)


numbers.append(20)  # Add new to end of list
numbers.insert(3, 100)  # Insert at specific index
numbers.remove(5)  # Removes first instance of paramater given
print(numbers.count(99))  # Counts the number os instances of a number
print(numbers)

# removes and returns last item from a list, there is no `push` in python instead there is `append`
popped = numbers.pop()
print(popped)

# Exercise 2
numbers2 = [4, 5, 10, 10, 20, 60, 5, 4, 400]
for number in numbers2:
    print(number)
    duplication = numbers2.count(number)
    print(number, duplication)
    if duplication > 1:
        while duplication:
            numbers2.remove(number)
            duplication -= 1
print('after', numbers2)


# Tupples similar to arrays but are immutable. They use parenthesis and are best for lists that should not change
strict_numbers = (3, 4, 5)

# You can deconstruct lists similar to how it is in javascript, however it demands all items are accounted for (you can deconstruct 2 items if 3 exist)
x, y, z = strict_numbers
print(x, y, z)
