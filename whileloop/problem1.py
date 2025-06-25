""" def circle(n, k):
    safe_position = 0
    for i in range(2, n + 1):
        safe_position = (safe_position + k)%i
    return safe_position+1
print(circle(3, 2))
print(circle(10,3)) """
def circle(n, k):
    remove =0
    person = list(range(1,n+1))
    while len(person) > 1:
        remove = (remove + k - 1) % len(person)
        person.remove(person[remove])
    return person
print(circle(5,3))
print(circle(10,2))
    
