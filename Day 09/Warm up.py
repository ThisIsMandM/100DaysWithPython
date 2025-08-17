""" programming_dictionary = {
    "Bug": "An error in a program that prevent the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Function"])

programming_dictionary["Argument"] = "It's the actual value of the parameter."

# Loop through dictionary

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
     """

capitals = {
    "USA": "Washington",
    "Germany": "Berlin"
}

#Nested List in Dictionary

travel_log = {
    "USA": ["Washington", "New york", "Nashville"],
    "Germany": ["Berlin", "Dortmund"],
    "Italy": {
        "cities_visited": ["Rome", "Milan", "Turin"],
        "total_visits": 5
    }
}

print(travel_log["Italy"]["cities_visited"])
print(travel_log["USA"][2])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

print(travel_log["Germany"][0])

