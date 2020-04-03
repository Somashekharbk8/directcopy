
# Deep copy

a= [1,2,3,4]
b = a.copy()
a[1] = 12  
print(a)  #[1,12,3,4]
print(b)  #[1,2,3,4]

#direct copy
list = [1,2,3,4,5,6,7,7] 
b = list
list[1]=10  
print(b)  # [1, 10, 3, 4, 5, 6, 7, 7]
print(list) # [1, 10, 3, 4, 5, 6, 7, 7]

