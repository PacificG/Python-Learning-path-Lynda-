#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print(timedelta(days=365,hours=5,minutes=6))


# print today's date
now = datetime.now()
print(now)

# print today's date one year from now
print(str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print(str(now + timedelta(days=2,weeks=3)))

# calculate the date 1 week ago, formatted as a string
print(str(now - timedelta(weeks=1)))

### How many days until April Fools' Day?


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  


