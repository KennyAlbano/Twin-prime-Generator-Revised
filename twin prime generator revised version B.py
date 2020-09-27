#Summary of twin prime generator written by Kenny Albano:
    #computes and displays a list of twin primes based on user input

i=0
primes=[2]
currentVal=3
twinPrimes=[]
m=int(input("how many tuples of twin primes do you want to dispaly?"))
n=m*10

#computes primes list
while(len(primes)<n):
    if(currentVal%primes[i]==0):
        currentVal=currentVal+2
        i=0
    if(len(primes)==(i+1)):
        primes.append(currentVal)
    if(currentVal%primes[i]!=0):
        i+=1
        
#uses primes list to computes twin primes list
i=0
while(i<n):
    if(primes[i]-primes[i-1]==2):
        twinPrimes.append((primes[i-1],primes[i]))
    i+=1
    
#Displays twin primes list    
i=0    
while(i<m):    
    print(twinPrimes[i])
    i+=1
    

    #note: A tuple in this case would (3,5) for the first 2 tuple
    #note: A twin prime tuple is a an ordered list of two prime numbers seperated by a difference of 2
    #note: A prime number is a number divisible under the set of Natural numbers N by only itself and 1
    #note: Natural numbers are just all the numbers you count with starting at 1 and going to infinity

#THE MEANING OF EACH VARIABLE:
    #i is simply an index
    #primes[] is a list of prime numbers. This list is always smaller than or equal to n.
    #currentVal is the natural number to divide by (divisor)
    #twinPrimes[] is a  list of 2 tuples of twin prime numbers
    #m is the user input of how many 2 tuples to display
    #n is the maximum number of prime numbers in the list of primes[]

#How the Program Actually works:
    #This program first computes a list of prime numbers.
        #The size of this list is not important as long as it is suffiently large compared to the list of twin primes.
            #sufficiently large in this case is very hard to calcualte;
                #so I used 10 times larger than the list of twin primes, which works in all test cases so far tested to be sufficient.
        #The list of primes is generated through the mathematical shortcut that all primes other than "2" are odd.
            #Otherwise the line currentVal=currentVal+2 would have be replaced by currentVal+=1
        #Also during the calcualtion of prime numbers I sped up the computation by;
            #only dividing by prime numbers currently on the list. Otherwise I could have done the slower but, more common method;
                #of dividing by every natural number to test for primeness.
    #After the program computes a suffiently long list of primes it begins computeing twin primes.
        #The computation for the twin primes list is simple.
            #The program runs through the list of primes any that are twin primes or seperated by a difference of 2 are added to
                #the twin primes list
    #Lastly the program runs through and prints all the twin primes.

#Program Limitations:
    #Becomes slow and possibly unresponsive if you input a number too large. (Over 100)
    #May not work for very large numbers in theory due to the current assumption
        #of twin primes being distributed 10X or less sparesly than primes
