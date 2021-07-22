print("Hello World")
a=51
b=213
if ((a == 51) and (b == 2)):
  print("Yes. a is equal to 5")
elif (( a==51) and (b==21)):
  print("No. a 51 and b is 21")
else:
  print("No. a is not 51 and b is not 2, also a is not 51 an db is not 21")

def greet():
  print("Hellosdsd")
greet()  

def greet_with_name(name,age=5):
  print(f"Hello {name}, you are: {age}")

greet_with_name(name="sridhar",age=44)
greet_with_name("Soniya")
greet_with_name(age=22,name='shankar')