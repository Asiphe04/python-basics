# Prinitng out a statemtent, or output

print('Hello World !') 

#--------------------------------------------------------------------------------------------------

#Variables

doctor = 'DR. Asiphe' #String

doc_number = 781149972 #number

patient_sick = True #booean



print('Hello' + ' ' + doctor )

#IntToStr
print('Hello' + ' ' + doctor + str(doc_number) + str(patient_sick) ) #converting numbr and boolean to string

#--------------------------------------------------------------------------------------------------

#cconverting text to uppercase, lowercase and all upercases 

dummyText = 'change to uppercase'

print(dummyText.capitalize()) #captilizing first letter
print(dummyText.upper()) #captailiing all letters
print(dummyText.lower()) #lowering all letters

#--------------------------------------------------------------------------------------------------


print(len(dummyText)) #checking length of a string

print(dummyText[3]) #targetting a specific position of a letter

print(dummyText.index('n')) #getting the position  where the specific letter is 

print(dummyText.replace('Change','Convert')) #replacing a word 

#user input
user_title = input("Please enter yor title: ")
user_name = input("Please enter your first name: ")
print("Hello" + ' ' + user_title + ' ' + user_name)

