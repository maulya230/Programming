def print_formatted(number):
    # your code goes here
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(width,' '),end=" ")
        print(oct(i)[2:].rjust(width,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(width,' '),end=" ")
        print(bin(i)[2:].rjust(width,' '),end=" ")
        print("")
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
