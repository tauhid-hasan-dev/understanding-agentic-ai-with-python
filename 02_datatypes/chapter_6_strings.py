today = "Friday"
significance = "Most important day of the week"

print(f"Today is {today}. {significance}" )

# string methods
print(f"Today is {today}. {significance}".upper())

print(f"Today is {today}. {significance}".lower())

print(f"Today is {today}. {significance}".title())

print(f"Today is {today}. {significance}".capitalize())


# string slicing
description = "This is a description"

print(f"Description: {description[0:5]}") # take the first 5 characters
print(f"Description: {description[0:5:1]}") # take every character
print(f"Description: {description[0:5:2]}") # take every other character
print(f"Description: {description[:8]}") # take the first 8 characters
print(f"Description: {description[8:]}") # take the last 8 characters
print(f"Description: {description[::-1]}") # reverse the string


# encoding and decoding
label_text = "Bugün çok güzel bir gün"
encoded_label_text = label_text.encode("utf-8")
print(f"Encoded label text: {encoded_label_text}")
decoded_label_text = encoded_label_text.decode("utf-8")
print(f"Decoded label text: {decoded_label_text}")

# string formatting
name = "John"
age = 30
print(f"Name: {name}, Age: {age}")


