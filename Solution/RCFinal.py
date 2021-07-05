import math
def s(a):
    s=0
    d=0
    while(a>0):
        if(a<10):
            d=s-a%10
        s=s+a%10
        
        a/=10
        a=int(a)
    
    return (int(s)+65,int(abs(d))+65)

while(True):
    print('Welcome to Shaastra RC Finals')
    print('Enter 1 for "THE HEIST"')
    print('Enter 2 for "ENCRYPTED CONVERSATION"')
    print('Enter 3 for "REVERTIGO"')
    print('Enter 4 for "NUMBERS ON THE WALL"')
    print('Enter 5 for "DOUG JUDY"')
    print('Enter 6 for "ANISH AND VISHAL"')
    print('Enter 7 for "THE ROBOT"')
    print('Enter 8 for "TREASURE HUNT"')
    print('Enter 9 for "THE MISSING BOY"')
    
    print('Enter 0 to exit the program')
    while True:
        try:
            
            n=int(input())
            if(n>9 or n<0):
                print('Enter in range 0-9')
            else:
                break
        except ValueError:
            print('Enter integer')
    print()
    if(n==1):
        print("THE HEIST")
        print('Enter an odd positive number below 69')
        print('Enter 0 to exit this question')
        print()
        while(True):
            while True:
                try:
                    x=int(input('Input : '))
                    
                    break
                except ValueError:
                    print("Enter an integer value")
            while True:
                if(x==0):
                    break
                if(x%2==0 or x<1 or x>69):
                    print('Enter an odd positive integer below 69')
                    x=int(input('Input :'))
                else:
                    break
            if(x==0):
                break
        
            c=(x+1)/2
            c=c-1
            for i in range(0,int(c)+1):
                for j in range(0,x):
                    if(j>=c-i and j<=c+i):
                        print('*',end='')
                    else:
                        print(' ',end='')
                print()
    elif(n==2):
        print("ENCRYPTED CONVERSATION")
        print('Enter any binary number (a number which has only 0s or 1s) greater than 0')
        print('Enter 0 to exit')
        print()
        while(True):
            while True:
                try:
                    x=int(input('Input : '))
                    l=list(str(x))
                   
                    b=True
                    for i in l:
                        if(i=='1' or i=='0'):
                            b=True
                        else:
                            b=False
                            break
                    if(b==True):
                        break
                    else:
                        print('Enter binary number')
                    
                    
                except ValueError:
                    print("Enter integer value")
            if(x==0):
                break
            s=0
            c=0
            for i in range(0,len(l)):
                s=s+int(l[i])* (2**(len(l)-i-1))
                if(l[i]=='1'):
                    c=c+1
         
            print(s**c)
                    
    
           

    

                
                
    elif n==3:
        print("REVERTIGO")
        print('Enter any integer between 10-1000')
        print('Enter 0 to exit this question')
        print()
        while True:
            while True:
                try:
                    x=int(input('Input : '))
                    if(x==0):
                        break
                    if(x>9 and x<1000):
                        break
                    else:
                        print('Enter integer BETWEEN 10-1000')
                except ValueError:
                    print('Enter integer value')
            if(x==0):
                break
            s=list(str(x))
            s1=""
            for i in s:
                s1=i+s1
            x1=int(s1)
            print(round(float(x1/x),3))

    elif n==4:
        print("NUMBERS ON THE WALL")
        print('Enter integer between 2-10000')
        print('Enter 0 to exit this question')
        print()
        L=[]
        for i in range(0,10000):
            L.append(0.0)
        L[0]=1.0
        L[1]=1.0
        for i in range(2,10000):
            L[i]=math.sqrt(L[i-1]**2+L[i-2]**2)
        while True:
            while True:
                try:
                    x=int(input('Input : '))
                    if (x==0):
                          break
                    if(x>1 and x<10000):
                        break
                    else:
                        print('Enter integer BETWEEN 2-10000')
                except ValueError:
                    print('Enter integer value')
            if(x==0):
                break
            print(round(L[x-1],3))

    elif n==5:
        print("DOUG JUDY")
        print('Enter a string in uppercase with length greater than 4')
        print('Enter 0 to exit this question')
        print()
        while True:
            while True:
            
                x=input('Input : ')
                if(x=='0'):
                    break
                elif(len(x)<4):
                    print('Enter string with length greater than 4')
                elif(x.isalpha()==True):
                    break
                else:
                    print('Enter String with no numbers/spaces/special characters')
            if(x=='0'):
                break
            x=x.upper()
            l=0
            b=list(x)
            a=0
            for i in range(0,len(x)):
                l=l+ord(b[i])
            l=l%len(x)
            for i in range(0,len(x)):
                
                a=ord(b[i])
                a=a+l
                if(a>90):
                    a=a-26
                       
                b[i]=chr(a)
                
                    
            print("".join(b))
            print()
        
            
    elif(n==6):
        print("ANISH AND VISHAL")
        print('Enter number of elements 2-10')
        print('Enter 0 to exit this question')
        print()
        while True:
            while True:
                try:
                    x=int(input('Number of elements : '))
                    if(x==0):
                        break
                    if(x<2 or x>10):
                            print('Enter in range')
                    else:
                        break
                except ValueError:
                    print('Enter integer')
            print('Enter ',x,' elements')
            if(x==0):
                break
            y=0
            d=0
            n=0
            print('Enter 0 at any point to reset')
            s=""
            for i in range(0,x):
                while True:
                    try:
                        
                        s='Enter element '+str(i+1)+': '
                        y=int(input(s))
                        
                        break
                    except ValueError:
                        print('Enter integer')
                if(y==0):
                    break
                
                n=n+y*y
                d=d+y*y*y
            if(y==0):
                print()
                break
            print(round(n/d,3))
            print()
                    
                
                
    elif (n==7):
        print("THE ROBOT")
        print('Enter number of elements 2-10')
        print('Enter 0 to exit this question')
        print()
        while True:
            while True:
                try:
                    x=int(input('Number of elements : '))
                    if(x==0):
                        break
                    if(x<2 or x>10):
                            print('Enter in range')
                    else:
                        break
                except ValueError:
                    print('Enter integer')
            print('Enter ',x,' positive integers')
            if(x==0):
                break
            arr=[]
            for i in range(0,x):
                while True:
                    try:
                        
                        s='Enter element '+str(i+1)+': '
                        y=int(input(s))
                        
                        break
                    except ValueError:
                        print('Enter integer')
                if(y==0):
                    break
                arr.append(y)
            s=0
            for i in range(0,x):
                for j in range(0,i):
                    if(arr[i]>arr[j]):
                        s=s+arr[i]
                    elif(arr[i]<arr[j]):
                        s=s-arr[i]
            print(s)
    
        
    elif(n==8):
        print("TREASURE HUNT")
        print('Enter latitute')
        print('Enter -1 to exit this question')
        print()
        while True:
            while True:
                try:
                    x=int(input('Enter degrees 0-90: '))
                    if(x==-1):
                        break
                    if(x>90 or x<0):
                        print('Enter within range')
                    else:
                        break
                except ValueError:
                    print('Enter integer')
            if(x==-1):
                break
            while True:
                try:
                    y=int(input('Enter minutes 0-60: '))
                    if(y==-1):
                        break
                    if(y>60 or y<0):
                        print('Enter within range')
                    else:
                        break
                except ValueError:
                    print('Enter integer')
            while True:
                try:
                    z=int(input('Enter seconds 0-60: '))
                    if(z==-1):
                        break
                    if(z>60 or z<0):
                        print('Enter within range')
                    else:
                        break
                except ValueError:
                    print('Enter integer')
            if(x==-1):
                break
            (a,b)=s(x)
            (c,d)=s(y)
            (e,f)=s(z)
            u=chr(b)+chr(a)
            v=chr(c)+chr(d)
            w=chr(e)+chr(f)
            print(u+v+w)
            print()
            
    elif n==9:
            print("THE MISSING BOY")
            print('Enter m,n between 10-1000000000 and p between 2-10')
            print('Enter m as 0 to end this question')
            while True:
                while True:
                    try:
                        m=int(input('Enter m: '))
                        if(m==0):
                            break
                        if(m<10 or m>1000000000):
                            print('Enter m between 10-1000000000')
                        else:
                            break
                    except ValueError:
                        print('Enter integer in range')
                if(m==0):
                    break
                while True:
                    try:
                        n=int(input('Enter n: '))
                        
                        if(n<10 or n>1000000000):
                            print('Enter n between 10-1000000000')
                        else:
                            break
                    except ValueError:
                        print('Enter integer in range')
                while True:
                    try:
                        p=int(input('Enter p: '))
                        
                        if(p>10 or p<2):
                            print('Enter p between 2-10')
                        else:
                            break
                    except ValueError:
                        print('Enter integer in range')


                m = float(m/n)
                m*= (10** (p-1))
                k = m - int(m)
                t = int(10*k)
                
                print(t)

        
           
            
    else:
        print('Program end')
        break
