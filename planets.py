def weight_on_planets():
   # write your code here
   weight = input("What do you weigh on earth? ")
   print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format(int(weight) * 0.38, int(weight) * 2.34))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
