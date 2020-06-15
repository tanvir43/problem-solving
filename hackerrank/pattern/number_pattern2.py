#OUTPUT

#1
#1 2 
#1 2 3
#1 2 3 4
#1 2 3 4 5
#1 2 3 4 5 6

n = int(input("Enter Number of rows: "))

def number_patt2(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print(j+1, end=" ")
        print("\r")

if __name__ == "__main__":
    number_patt2(n)

