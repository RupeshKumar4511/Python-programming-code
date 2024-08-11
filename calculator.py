# This is real calculator which performs + , - , *, / ,//,%
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):    
  if y==0:
      return "cannot be divided"
  else:
       return x/y
  
     
def floordivision(x,y):
    if y==0:
      return "cannot be divided"
    else:
      return x // y

def reminder(x,y):
    if y==0:
      return "cannot be divided"
    else:
      return x % y
  
print("Operations :")
print("Add :  + ")
print("Subtract :  - ")
print("Multiplication :  * ")
print("Division :  / ")
print("Reminder :  % ")
print("Floor Division :  // ")



a = eval(input("enter number : "))
c = input("enter operation ")
b = eval(input("enter number : "))
list1 =[]
if(c== "+"):
     sum = add(a,b)
     list1.append(sum)
     print("result :",sum)
elif(c=='-'):
     sub = subtract(a,b)
     list1.append(sub)
     print("result :",sub)

elif(c== '*'):
         
         mul = multiply(a,b)
         list1.append(mul)
         print("result :",mul)

elif(c== '/'):
         div = divide(a,b)
         list1.append(div)
         print("result :",div)
else:
     print("InValid operation")



num = 0
while(num != 100000):
     
     d = input("enter operation : ")
     if(d == '+'):
          e = eval(input("enter number : "))
          sum = add(list1[0],e)
          list1.insert(0,sum)
          print("result :",sum)

          num += 1 
          continue
          
     elif(d == '-'):
          e = eval(input("enter number : "))
          sub = subtract(list1[0],e)
          list1.insert(0,sub)
          print("result :",sub)
          num += 1 
          continue

     elif(d == '*'):
          e = eval(input("enter number : "))
          mul = multiply(list1[0],e)
          list1.insert(0,mul)
          print("result :",mul)
          num += 1
          continue

     elif(d == '/'):
              e = eval(input("enter number : "))
              div = divide(list1[0],e)
              list1.insert(0,div)
              print("result :",div)
              num += 1
              continue
     elif(d == '='):
              print(list1[0])
              num += 1
              continue
    


     num += 1
     
             
    



        
     
     




