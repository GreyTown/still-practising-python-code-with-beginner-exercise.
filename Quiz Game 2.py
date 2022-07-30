print('This is a Capital Cities Quiz Game')
playing = input("Do you wanna play? ").lower()
score = 0

if playing != "yes":
	print("Bye Felicia! ")
	quit()
else:
	print("Okay, let's play! ")

#Question 1
answer = input("What is the Capital City of Uganda? ")
if answer.lower() == "kampala":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 2
answer = input("What is the Capital City of Kenya? ") 
if answer.lower() == "nairobi":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 3
answer = input("What is the Capital City of Poland? ")
if answer.lower() == "warsaw":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 4
answer = input("What is the Capital City of Turkey? ")
if answer.lower() == "instabul":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 5
answer = input("What is the Capital City of Jamaica? ").lower()
if answer == "kingstone":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 6
answer = input("What is the Capital City of Egypt? ").lower()
if answer == "cairo":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 7
answer = input("What is the Capital City of Ghana? ").lower()
if answer == "accra":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 8
answer = input("What is the Capital City of Nigeria? ").lower()
if answer == "abuja":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 9
answer = input("What is the Capital City of Rwanda? ").lower()
if answer == "kigali":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")

#Question 10
answer = input("What is the Capital City of Mozambique? ").lower()
if answer == "maputo":
	print("Correct! ")
	score += 1
else:
	print("Incorrect.")


print("You have scored",score,"correct questions out of 10")

if score >= 8:
	print("Good! You won yourself a gift!")




