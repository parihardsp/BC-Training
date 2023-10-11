def space():
    print("-" * 20)


for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
print('Next Statement')

for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    else:
        print(i)

for i in range(1, 6):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

space()

for i in range(1, 4):
    print(f"Outer loop iteration {i}")
    for j in range(1, 4):
        print(f"  Inner loop iteration {j}")
        if i * j == 4:
            print("  Breaks inner loop due to i * j == 4")
            break

    if i == 3:
        print("Breaks outer loop due to i == 3")
        break

result=pow(2,3)
print(result)

print("-"*50)

def expo():
    check=True
    x=2
    while check:
        x=x*2
        print(f"Exponents of 2 are: {x}")
        if x==128:
            check=False
            return 'All done'

expo()

print("-"*50)

x = 5
assert x == 5, "x should be equal to 5" #if x!=5 then it will raise AssertionError and will not procede further.
y=10
print(dir(y))