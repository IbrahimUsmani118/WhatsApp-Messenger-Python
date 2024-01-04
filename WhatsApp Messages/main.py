# Import library to start the module
import pywhatkit

# Enter a phone number
number = input("Enter a phone number with the country's extension: ")

# Enter a message
msg = input("Enter a message you would like to send: ")

# Enter the hour
hour = float(input("Enter the hour number you would like it to be sent(0-23): "))

# Enter the minute
minute = float(input("Enter the minute you would like it to be sent(0-59): "))

# The function which calls the previously defined variables
pywhatkit.sendwhatmsg(number, msg, hour, minute)

input()
