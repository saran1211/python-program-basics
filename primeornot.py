num=13
if num > 1:
    for i in range(2,num):
       if (num % i) == 0:
           print(num,"it is not a prime num")
           print(i,"times",num//i,"is",num)
           break
    else:
       print(num,"is a prime num")

else:
   print(num,"is a prime num")
