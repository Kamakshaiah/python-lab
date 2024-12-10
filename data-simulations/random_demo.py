import random 


mylist = [1, 3, 5, 7, 9] 
 
n = random.choice(mylist) 
print(n)

n = random.randrange(20, 50, 4) 
print(n)

n = random.uniform(13,17) 
print(n) 

mylist = [1, 2, 3, 4, 5, 6, 7] 
 
random.shuffle(mylist) 
print(mylist) 

val = int(input("Enter seed value : ")) 
 
random.seed(val) 
for i in range(val): 
    print(random.random(), end = ' ')

# for vectors
rnd.sample(range(50, 100), 10)

# factors
g = rnd.choices(['m', 'f'], k=5)
print(g)
