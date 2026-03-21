# write a program to formate the current date and time as "monday, october 06,2025 09:30:15 AM" using strftime
import datetime
# from datetime import datetime

now = datetime.datetime.now()

formatted = now.strftime(" %A, %B, %d, %y,%I:%M:%S %p")
print(formatted)
