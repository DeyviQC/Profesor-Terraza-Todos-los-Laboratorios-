l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

print("------------------a--------------")

s1 = set(l1)
s2 = set(l2)
print("Conjunto s1: ", s1)
print("Conjunto s2: ", s2)

print("------------------b--------------")

s3 = s1.intersection(s2)
print("Conjunto s3: ", s3)

print("------------------c--------------")

s4= s1.symmetric_difference(s2)
print("Conjunto s4: ", s4)

print("------------------d--------------")

l3 = sorted(list(s3) + list(s4), key=lambda x: x[1]) # key=lambda x: x[1] permite que se ordene segun el 2do elemeto de la tupla en este caso el valor numerico
print("Lista l3: ", l3)



