programming_dictionary = {
    "Bug": "An error in a program that prevent the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Function"])

programming_dictionary["Argument"] = "It's the actual value of the parameter."

# Loop through dictionary

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])