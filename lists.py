if __name__ == '__main__':
    N = int(input())
    l=[ ]
    for i in range(0,N):
        ip=input().split()
        if ip[0]=="print":
            print(l)
        elif ip[0]=="insert":
            l.insert(int(ip[1]),int(ip[2]))
        elif ip[0]=="remove":
            l.remove(int(ip[1]))
        elif ip[0]=="append":
            l.append(int(ip[1]))
        elif ip[0]=="sort":
            l.sort()
        elif ip[0]=="pop":
            l.pop()
        else:
            l.reverse()
    
    
