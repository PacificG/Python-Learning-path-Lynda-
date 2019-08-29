#
# Example file for working with classes
#


def main():
  class Circle():
    def area(self,r):
      self.c = 3.14 * r * r

    def color(self,color):
        self.d = color
  
  c = Circle()
  c.color('black')
  c.area(4)
  
if __name__ == "__main__":
  main()
