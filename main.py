import math

user_input = input("operation:")
if user_input == "add":
 num1 = float(input("Enter a number:"))
 num2 = float(input("Enter another number:"))
 result = str(num1+num2)
 print (" the answer is"+ result)
if user_input == "subtract":
 num1 = float (input("Enter a number:"))
 num2 = float (input("Enter another number:"))
 result = str(num1-num2)
 print (" the answer is" + result)
if user_input == "multiply":
 num1 = float (input("Enter a number:"))
 num2 = float (input("enter another number:"))
 result = str(num1*num2)
 print (" the answer is" + result)
if user_input == "divide":
 num1 = float (input("Enter a number:"))
 num2 = float (input("Enter another number:"))
 result = str(num1/num2)
 print (" the answer is" + result)
if user_input == "square root":
 num1 = float (input("Enter a number:"))
 result = str(math.sqrt(num1))
 print ("the answer is" + result)
if user_input == "square":
 num1 = float (input("Enter a number:"))
 result = str(num1*num1)
 print ("the answer is" + result)
if user_input == "cos":
 num1 = float (input("Enter a number:"))
 result = str(math.cos(num1))
 print ("the answer is" + result)
if user_input == "sin":
 num1 = float (input("Enter a number:"))
 result = str(math.sin(num1))
 print ("the answer is " + result)
if user_input == "tan":
 num1 = float (input("Enter a number:"))
 result = str(math.tan(num1))
 print ("the answer is " + result)
if user_input == "cubing":
 num1 = float (input( "Enter a number:"))
 result = str(num1*num1*num1)
 print (" the answer is " + result)
if user_input == "exponent":
 num1 = float(input("Enter a number:"))
 num2 = float(input("Enter another number:"))
 result = str(num1**num2)
 print (" The answer is " + result)
if user_input == "atan":
 num1 = float(input("Enter a number:"))
 result = str(math.atan(num1))
 print (" The answer is " + result)
if  user_input == "acos":
 num1 = float(input("Enter a number:"))
 result = str(math.acos(num1))
 print ("the answer is" + result)
if user_input == "asin":
 num1 = float(input("Enter a number:"))
 result = str(math.asin(num1))
 print ("the answer is" + result)
if user_input == "area of a circle":
 radius = float(input("Enter a number:"))
 result = str(radius*radius*3.14)
 print ("the answer is" + result)
if user_input == "circumference":  
 radius = float(input("Entrer a number:"))
 result = str(2*3.14*radius)
 print ("the answer is" + result)
if user_input == "area of a rectangle":
 length = float(input("Enter a length:"))
 width = float(input("Enter a width:"))
 result = str(length*Width)
 print ("The area of the rectangle is:" + result)
if user_input == "perimeter of a recangle":
 length = float(input("Enter a length:"))
 width = float(input("Enter a width:"))
 result = str(length+width+length+width)
 print ("The primeter of a rectangle is:" + result)
if user_input == "area of a square":
 length = float(input("Enter a length:"))
 width = float(input("Enter a width:"))
 result = str(length*Width)
 print ("The area of the square is:" + result)
if user_input == "perimeter of a square": 
 length = float(input("Enter a length:"))
 width = float(input("Enter a width:"))
 result = str(length+length+width+width)
 print (" the perimeter of the square is:" + result)                                          
if user_input == "area of a parallelogram":
 base = float(input("Enter the width of the parallelogram:"))
 height = float(input("Enter the hieght of the paralleogram:"))
 result = str(base*height)
 print ("The area of the parallelogram is:" + result)
if user_input == "perimeter of a parallelogram":
 base = float(input("Enter the width of the base of the parallelogram:"))
 side = float(input("Enter the legth of the side of the parallelogram:"))
 result = str(2*base+2*base)
 print ("The perimeter of the parallelogram is:" + result)              
if user_input == "area of a hexagon":
 side = float(input("Enter the length of one of the sides of the hexagon:"))
 result = str(math.sqrt(3)(3)/2(side*side))
 print ("The area of the Hexagon is:" + result)
