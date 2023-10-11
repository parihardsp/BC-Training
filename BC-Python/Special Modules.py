import random


print(random.randint(1,5))
print(random.randrange(10,100,5))
print(random.random())
print(random.uniform(10,20))

l=[10,2,5,9,91,100]

print(random.choice(l))
random.shuffle(l)
print(l)

print('-'*50)