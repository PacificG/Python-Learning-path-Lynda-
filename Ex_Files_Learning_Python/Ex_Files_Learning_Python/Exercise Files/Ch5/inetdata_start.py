# 
# Example file for retrieving data from the internet
#
import urllib.request

def main():
  url = urllib.request.urlopen('http://www.google.com')
  print('result code:' + str(url.getcode()))

  data = url.read()
  print(data)
if __name__ == "__main__":
  main()
