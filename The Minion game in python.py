def minion_game(string):
    # your code goes here
    p1=0
    p2=0
    n=len(string)
    for i in range(n):
        if s[i] in "AEIOU":
            p1+=n-i
        else:
            p2+=n-i
            
    if p1>p2:
        print("Kevin",p1)
    elif p1<p2:
        print("Stuart",p2)
    elif p1==p2:
        print("Draw")    
    else:
        print("Draw")        

if __name__ == '__main__':
    s = input()
    minion_game(s)
