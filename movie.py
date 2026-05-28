#Daisha
#Movie Theatre
#1. Write a function that collects the user’s age as input and prints what types of movie the user can see at the movie theatre

#Functions
#Main
def movie ():
    age =int( input("please enter your age: "))
        if age >= 18:
            print ("you can see any movie including Rated-R")
        elif age >= 13:
            print ("you can see pg-13 movies")
        else:
            print("you can se pg movies")

movie ()
