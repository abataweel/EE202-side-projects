#Name:Ahmed Bataweel
#ID:2436391
from math import sqrt,acos,degrees

# getting coords from the user
welcomeMsg = input("Welcome to compute angles program, press (enter) to continue")
while True:
 try:
    #getting the input of points from the usre
     points = input("Enter the three pair of points for the triangle followed by comma (,):").split(",")
 
     if len(points) != 6: # checking for the length of (points) array
       print("Please enter enough number of points") 
       continue
     # assigning points from array
     x1 = float(points[0]) 
     y1 = float(points[1]) 
     x2 = float(points[2]) 
     y2 = float(points[3]) 
     x3 = float(points[4]) 
     y3 = float(points[5]) 
 
 
 
     # computing distance to get the length 
     a = sqrt((x3-x2)**2+(y3-y2)**2)
     b = sqrt((x3-x1)**2+(y3-y1)**2)
     c  = sqrt((x2-x1)**2+(y2-y1)**2)
     # computing angles using formula 
     A= acos((a*a-b*b-c*c)/(-2*b*c))
     B= acos((b*b-a*a-c*c)/(-2*a*b))
     C= acos((c*c-b*b-a*a)/(-2*a*b)) 
     
     # converting from radians to degrees
     angleA_deg = round(degrees(A),2)
     angleB_deg = round(degrees(B),2)
     angleC_deg = round(degrees(C),2)
     
     # displaying the angles 
     print(f'The three angles of the triangle are: A:{angleA_deg} B:{angleB_deg} C:{angleC_deg}')
 except ValueError:
     print("Please enter points points as numbers only")
     continue
 isExit = input("Press enter to compute angles again or e to exit the program")
 if isExit == 'e':
     print("Thanks for using the program, program closed")
     break
 else:continue