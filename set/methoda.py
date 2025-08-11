s={22,"bq","1a",4911,23,65}
s.add(11)#add the element to the set
print(s)
s.remove(4911)#remove the element but shows the erroe if not present
s.discard(1)#remove if element is present else not show error
print(s)
s.pop()#remove the first element is the set
print(s)
s.clear()#clear the all the elements in set and there is a empty set
print(s)
c={1,2,3,4,5}
d={34,23,12,4,5}
union =d.union(c)#(c | d)
print(union)
intersection =d.intersection(c)#(c & d )
print(intersection)
difference = c.difference(d)#( c - d)
print(difference)
symentric = c.symmetric_difference(d)#(A ^ b)
print(symentric)