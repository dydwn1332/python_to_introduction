a = 2
for b in range(1, 10):
    print("%d x %d = %d" %(a, b, a*b))


print("-" * 50)

for a in range(1, 10):
    for b in range(1, 10):
        print("%d x %d = %d" %(a, b, a*b))
    print("-" * 50)