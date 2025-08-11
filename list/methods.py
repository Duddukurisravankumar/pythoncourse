#different type of methods in list
num =[1,34,56,76,9,1,3]
num.insert(2,10)#insert the number into the list at required position
num.append(20)#add the number into list at the last index
num.extend([100,1000,200])#add the multiple elements at thew end
num.remove(1)#remove the first occurence of 1
poped =num.pop(3)#remove and store the element at index 3
index =num.index(76)#find the index of the number 76
count_num =num.count(56)#count the occurence of 56
num.sort()#sort the num list
num.reverse()#reverse the list
num_copy =num.copy()#create a copy of a list
num.clear()#remove the all the elements from list