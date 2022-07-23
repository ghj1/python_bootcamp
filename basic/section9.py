programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving itmes from dictionary.
# print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# Create an empty dictionary.
empty_list = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary.
for key in programming_dictionary:
    print(key) # print key
    print(programming_dictionary[key]) # print value
    
# Nesting 
capitals = {
    "France" : "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# Nesting Dictionary in a Dictionary
# France key안에 dictionary를 만들고 cities_visited라는 key안에 
# 이 list를 값으로 넣어주세요 
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Europe": {"country_visited": ["France", "Germany","United Kingdom"], "total_visited": 8}
}

# Nesting Dictionary in a List
travel_log = [
    {
        "country":"France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "bundle":"Europe", 
        "country_visited": ["France", "Germany","United Kingdom"], 
        "total_visited": 8
    },
]