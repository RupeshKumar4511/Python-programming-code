# This is a Simple calculator which performs addition, subtraction, multiplication, division ,Integer division,reminder after dision.

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


try:
     a = eval(input("enter number : "))
     c = input("enter operation ")
     b = eval(input("enter number : "))
     result =0;
     if(c== "+"):
          sum = add(a,b)
          result = sum
          print("result :",sum)
     elif(c=='-'):
          sub = subtract(a,b)
          result = sub
          print("result :",sub)

     elif(c== '*'):
         
         mul = multiply(a,b)
         result = mul
         print("result :",mul)

     elif(c== '/'):
         div = divide(a,b)
         result = div
         print("result :",div)
     else:
           print("InValid operation")



     num = 0
     while(num != 100000):
     
          d = input("enter operation : ")
          if(d == '+'):
               e = eval(input("enter number : "))
               sum2 = add(result,e)
               result = sum2
               print("result :",sum2)

               num += 1 
               continue
          
          elif(d == '-'):
               e = eval(input("enter number : "))
               sub2 = subtract(result,e)
               result = sub2
               print("result :",sub2)
               num += 1 
               continue

          elif(d == '*'):
               e = eval(input("enter number : "))
               mul2 = multiply(result,e)
               result = mul2
               print("result :",mul2)
               num += 1
               continue

          elif(d == '/'):
              e = eval(input("enter number : "))
              div2 = divide(result,e)
              result = div2
              print("result :",div)
              num += 1
              continue
          elif(d == '='):
              print(result)
              num += 1
              continue

          else:
              print("wrong operation")

          num += 1
except:
     print("wrong enteries")
    


    
     
             
    



        
     
     








        
     
     




