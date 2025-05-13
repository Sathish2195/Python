import netmiko
from netmiko import ConnectHandler

n = 5

if n == 0:
 print("Hello world")
else:
  print("Bye world")

  while n < 10:
    print("Hello" + "n")
    n +=1
    print(n)

