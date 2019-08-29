#
# Example file for working with conditional statements
#

def main():
  x, y = 10, 100
  
  # conditional flow uses if, elif, else  
  if x<y:
    print('x is less than y')
  elif(x == y):
    print('x and y are same')
  else:
    print('x is greater than y')
  # conditional statements let you use "a if C else b"
  st = 'xyz' if (x<y) else 'yzw'
  print(st)

if __name__ == "__main__":
  main()
