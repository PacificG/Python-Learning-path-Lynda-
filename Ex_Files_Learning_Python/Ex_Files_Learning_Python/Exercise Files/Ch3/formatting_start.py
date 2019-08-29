#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 

  #### Date Formatting ####
  now = datetime.now()
  print(now.strftime('The current year is %Y'))
  print(now.strftime('%a'+'%b'+'%d'))
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month


  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime('%c'))

  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime('%H'))


if __name__ == "__main__":
  main();