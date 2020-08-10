#Initialize the largest and smallest values as 'None'  
largest  = None  
smallest = None  

while True:  
    num = input("Enter a number:")  
    if num == "done": #Type 'done' to get the output    
        break  
    try:  
        fnum = int(num)  #Convert input to int  

        #Get largest value  
        if largest is None:  
            largest = fnum  
        elif fnum > largest:  
            largest = fnum  

        #Get smallest value  
        elif smallest is None:   
            smallest = fnum  
        elif fnum < smallest:  
            smallest = fnum  

    except: 
        #If the user input is not 'done' or a number    
        print("Invalid input")   
        continue    


print("Maximum is",largest)  
print("Minimum is",smallest) 
