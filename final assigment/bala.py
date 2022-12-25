food=["Tandoori Chicken", "Vegan Burger", "Truffle Cake"]
prices =[240, 320, 900]

myorderFood=[]
myorderCost=[]
counter=0
total=0

print ("Welcome to McGodbolds")


order = input("Can I take your order?")
if order =="No":
    exit()
else:
    print("Thank you")

nextOrder = True

while nextOrder==True:
    foodOrder = input("Please enter item")
    if foodOrder =="Tandoori Chicken":
        myorderFood.append(food[0])
        myorderCost.append(prices[0])
        counter=counter+1
        total=total+(prices[0])
    
    elif foodOrder=="Vegan Burger":
        myorderFood.append(food[1])
        myorderCost.append(prices[1])
        counter=counter+1
        total=total+(prices[1])

    elif foodOrder=="Truffle Cake":
        myorderFood.append(food[2])
        myorderCost.append(prices[2])
        counter=counter+1
        total=total+(prices[2])

  
    else:
        print("Not on Menu")
    finished = input("Have you Finished Ordering Y/N")
    if finished=="N":
        nextOrder=True
    else:
        nextOrder=False

y=0

print ("Here is your order")
print ("      ")
print ("***********")
while y<counter:
    
    print ("Item: "+ (myorderFood[y]))
    print ("Cost: $"+str(myorderCost[y]))
    y=y+1

print ("The Final Cost is  $"+str(total))
    
    
     
    
