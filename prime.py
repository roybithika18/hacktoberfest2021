num = 17
if num > 1:
   for i in range(2, num//2):
      # If num is divisible by any number between 2 and n / 2, it is not prime
      if (num % i) == 0:
         print(num, "is not a prime number")
         break
      else:
         print(num, "is a prime number")
   else:
print(num, "is not a prime number")
