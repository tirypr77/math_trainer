def addition_game():
    print "Welcome to Ryan's addition trainer! Do your best to answer the following 20 questions!"
    turn = 1
    correct = 0
    from random import randint
    for n in range(20):
        X = randint(1,50)
        Y = randint(1,50)
        print 'Question', turn, "of 20"
        while True:
              try:
                  guess = int(raw_input('%s + %s = ' % (X, Y))) 
                  guess = int(guess)
                  break
              except ValueError:
                     print("Not an integer! Please try again.")    
        if guess == (X+Y):
           print 'Correct!'
           print ' '
           correct += 1
           turn +=1
        else:
             print 'Wrong! Better luck next question!'
             print " "
             turn += 1
    print '%s correct out of 20 questions' % correct
    yup = []
    while True:
          yup = str(raw_input("Play again? [y/n]: "))
          if yup == "y":
             addition_game()
             break
          elif yup == "n":
               main_menu()
               break
          else:
               print "Please enter y or n"
               
def subtraction_game():
    print "Welcome to Ryan's subtraction trainer! Do your best to answer the following 20 questions!"
    turn = 1
    correct = 0
    from random import randint
    for n in range(20):
        X = randint(10,50)
        Y = randint(1,20)
        print 'Question', turn, "of 20"
        while True:
              try:
                  guess = int(raw_input('%s - %s = ' % (X, Y))) 
                  guess = int(guess)
                  break
              except ValueError:
                     print("Not an integer! Please try again.")    
        if guess == (X-Y):
           print 'Correct!'
           print ' '
           correct += 1
           turn +=1
        else:
             print 'Wrong! Better luck next question!'
             print " "
             turn += 1
    print '%s correct out of 20 questions' % correct
    yup = []
    while True:
          yup = str(raw_input("Play again? [y/n]: "))
          if yup == "y":
             subtraction_game()
             break
          elif yup == "n":
               main_menu()
               break
          else:
               print "Please enter y or n"
               
def multiplication_game():
    print "Welcome to Ryan's multiplication trainer! Do your best to answer the following 20 questions!"
    turn = 1
    correct = 0
    from random import randint
    for n in range(20):
        X = randint(1,20)
        Y = randint(1,10)
        print 'Question', turn, "of 20"
        while True:
              try:
                  guess = int(raw_input('%s * %s = ' % (X, Y))) 
                  guess = int(guess)
                  break
              except ValueError:
                     print("Not an integer! Please try again.")    
        if guess == (X*Y):
           print 'Correct!'
           print ' '
           correct += 1
           turn +=1
        else:
             print 'Wrong! Better luck next question!'
             print " "
             turn += 1
    print '%s correct out of 20 questions' % correct
    yup = []
    while True:
          yup = str(raw_input("Play again? [y/n]: "))
          if yup == "y":
             multiplication_game()
             break
          elif yup == "n":
               main_menu()
               break
          else:
               print "Please enter y or n"
               
               
def division_game():
    print "Welcome to Ryan's division trainer! Do your best to answer the following 20 questions!"
    turn = 1
    correct = 0
    from random import randint
    for n in range(20):
        X = randint(10,50)
        Y = randint(1,10)
        print 'Question', turn, "of 20"
        while True:
              try:
                  guess = int(raw_input('%s / %s = ' % (X, Y))) 
                  guess = int(guess)
                  break
              except ValueError:
                     print("Not an integer! Please try again.")    
        if guess == (X/Y):
           print 'Correct!'
           print ' '
           correct += 1
           turn +=1
        else:
             print 'Wrong! Better luck next question!'
             print " "
             turn += 1
    print '%s correct out of 20 questions' % correct
    yup = []
    while True:
          yup = str(raw_input("Play again? [y/n]: "))
          if yup == "y":
             division_game()
             break
          elif yup == "n":
               main_menu()
               break
          else:
               print "Please enter y or n"
     
  
def main_menu():
    while True:
          choice = str(raw_input("Welcome to Ryan's Math Trainer. Enter 1 for the addition trainer, 2 for subtraction, 3 for multiplication, and 4 for division. Or, enter q to exit the trainer. > "))
          if choice == '1':
             addition_game()
             break
          elif choice == '2':
               subtraction_game()
               break
          elif choice == '3':
               multiplication_game()
               break
          elif choice == '4':
               division_game()
               break
          elif choice == 'q':
               break
               exit()
          else:
               print ''
               print 'Please enter 1, 2, 3, 4, or q'
               print ''

main_menu()


