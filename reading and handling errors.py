try:
 b=input("Enter the file name that you want to see: ") #the user needs to enter the filename to open it
 with open(b , 'r') as a:
      reading_file=a.read()
      print(reading_file)
except FileNotFoundError:
    print("This file does not exist")
