#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while x < 10:
    print(x)
    x = x + 1

  # define a for loop
  for i in range(4):
    print(i)

  # use a for loop over a collection
  days = ['mon','tue','wed','thu']
  for d in days:
    print(d)
 
  # use the break and continue statements
  for d in range(8):
    print(d)
    if d % 2 == 0: continue
    elif d == 7 : break
  #using the enumerate() function to get index 
  for i,d in enumerate(days):
    print(i,d)

if __name__ == "__main__":
  main()
