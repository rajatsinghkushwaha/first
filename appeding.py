def delandcreate(): #This function will allow the user to create a fresh file named output.txt
 user_data=input("Enter the text in your file: ")
 file1=open('output.txt', 'w')
 file1.write(user_data)
 file1.close()
 return()


delandcreate()  #function calling

def appendfile(): #This function will allow the user to append data to a file
 user_wish=input("Do you want to write something more to your file? y/n: ")
 if user_wish.lower()=='y':
    add=input("Enter the text you want to add to your file: ")
    file1=open('output.txt','a')
    file1.write('\n'+add)
    file1.close()
    return()
 elif user_wish.lower()=='n':
    return()
 else:
    print("Please enter y or n")
    appendfile()


appendfile() #function calling


def reading_file(): #This function allows to user to read the data on his file
 see=input("Do you want to see your file? y/n: ")
 if see.lower()=='y':
    file1=open('output.txt','r')
    seeing=file1.read()
    print(seeing)
    file1.close()
    return()
 elif see.lower()=='n':
     return()
 else:
     print("Please enter y or n")
     reading_file()


reading_file()  #function calling

again=input("Do you want to create fresh file? y/n: ")  #If user want to delete everything from a file and enter fresh data


def deldel():  #This function will delete everything from a file and allows the user to enter fresh data
 if again.lower()=='y':
    delandcreate()
    reading_file()
 elif again.lower()=='n':
    print("Thank you for your time")
    return()
 else:
    print("Please enter y or n")
    deldel()

deldel()  #function calling

