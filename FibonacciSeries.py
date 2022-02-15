
"""""        
COMPCS100. 2. Programming 1. 2.7 Fibonacci series
Reyver Serna:rs412764@tuni.fi
Student number: 412764
"""""
def main():
    # Define user's input'
    nterms = int(input("How many Fibonacci numbers do you want? "))

    # define the first two terms
    current_fib = 0
    previous_fib = 1
    count = 0

    # Check if the number of terms is valid
    if nterms <= 0:
        print()
    elif nterms == 1:
        print(current_fib)

    else:
        for i in range(nterms):
            print(f"{i+1}. {previous_fib}", sep="")
            next_fib = current_fib + previous_fib
            # update values
            current_fib = previous_fib
            previous_fib = next_fib
            count +=1

if __name__ == "__main__":
    main()