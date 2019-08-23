def isprime(n):
  if(n==1):
      return False
  elif(n==2):
      return True
  else:
      for i in range(2,n):
          if(n%i==0):
              return False
      return True


def solve():
    A="sorabh"
    flag=True
    vowels=['a','e','i','o','u']
    for i in range(len(A)):
        if not(isprime(i+1)):
            if(A[i] in vowels):
                flag=False
                break
       
    if flag==True:
        B="YES"
    else:
        B="NO"
    print(B)


solve()
