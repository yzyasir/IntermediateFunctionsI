import random
def randInt(min=0, max=100):
    # print(min)
    # print(max)
     
    # num = random.randint(min, max) 
    num = random.ramdom * max
    return num
print(randInt())
print(randInt(max=50))
print(randInt(min=90))
print(randInt(min=10, max=20))
#print(randInt()) 		    # should print a random integer between 0 to 100
#print(randInt(max=50)) 	    # should print a random integer between 0 to 50
#print(randInt(min=50)) 	    # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500