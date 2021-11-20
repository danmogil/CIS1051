# dateTime implementation
# from datetime import timedelta

# sec = int(input("Enter a value in seconds: "))

# convert = timedelta(seconds=sec)
# format = str(convert).split(':')

# print(format[0] + " hours, " + format[1] + " minutes, and " + format[2] + " seconds.")


#mod implementation
seconds = int(input("Enter a value in seconds: "))

hours = seconds // 3600
seconds %= 3600
minutes = seconds //60
seconds %= 60
output = "%02i hours, %02i minutes, and %02i seconds." % (hours, minutes, seconds)
print(output)