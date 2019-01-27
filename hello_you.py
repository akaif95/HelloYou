#Ask the user for their name
name = input("What is your full name? ")

#Ask the user for their age

#!TRY USING THE TRY/EXCEPT CLAUSE
age = int(input("What is your current age? "))

#Ask where the user is from (city)
city_location = input("What city are you from? ")

#Ask user what their favorite hobby is
favorite_hobby = input("What is your favorite hobby? ")
print()

#Create Output Text
personal_data_text = """Okay, let's see if this is correct. Your name is {}, and
you are currently {} years old. You currently reside in the city of {} and your favorite hobby is {}.""".format(name, age, city_location, favorite_hobby)


#Print Output
print(personal_data_text)
    
