x = []			# AI List #
input("PAI Powered On") 
while True:             # Doesn't shut off till Lists are Read #
        i = input()	# User Inputs # 
        x.append(i)     # Input to Dictionary Data Converter # 
        if i == "Send": 	# List Read Command #          
                for words in x: # Opens List #
                        if words == "he": # Looks for Character Combinations in List  # 
                                print("Hello, I am PAI") 
                        if words == "ho": 
                                print("Depends on my Update, at the moment Good")
                        if words == "go": 
                                print("Thank you for talking to me") 
                        if words == "ea": 
                                print("good") 
                        if words == "wh": 
                                print("I'm not really AI, I just have my own language. I speak through Lists, Input which would be /n'english/n' gets converted into my language and then I analyze it and generate a response based on the letter combinations ")
                        if words == "ex": 
                                print("Be more specific") 
                        if words == "ee": 
                                print("Hello, I am PAI") 
                        else:
                                print("PAI requires User Operated Input")
        if i == "Send": # After Analysis and Response the program shuts down #                  
                break 

# Each Input needs to be 2 characters at a time so there's no overlapping # 
# Overlapping would be 2 If statements being True which would Initiate 2 responses #
# For example, h can be found in how and hello so both are True #

# One problem in the earlier builds was the fact that when inserting inputs
# into a list its all one string but inserting 2 characters at a time gets rid of that 
