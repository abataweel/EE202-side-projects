from math import sqrt

while True:
   
 coff_A,coff_B,coff_C = eval(input("Enter a,b,c:"))
#works fine but needs to check of all 3 values are entered as well as all are numbers  no strings
 
 if coff_A ==0:
        print("a must not be equal to 0, please enter a valid value")
        continue

 diskcriminant = coff_B**2-4*coff_A*coff_C # calculating the discriminant
 if diskcriminant <0: 
    print("The equations has no real roots")
 if diskcriminant == 0:
     identicalRoot = -coff_B-sqrt(diskcriminant)/2*coff_A
     print("the equation has an indetical root", identicalRoot)
 if diskcriminant >0: 
     r1=  -coff_B-sqrt(diskcriminant)/2*coff_A
     r2 = -coff_B+sqrt(diskcriminant)/2*coff_A
     print("The roots of the equations are r1:",r1,"r2:",r2)
 cont= input("do you want to continue?").lower()
 if cont =="e"  :
     print("exit the loop")
     break
 else: continue
  
 
    
 