print('A type of Integer is 1')
print('A type of Float is 1.2')
print('A type of Complex is 1 + 3j')
print('A type of String is Hello')
print('A type of Boolean is T for True')
my_list = ['Banana', 'Orange', 'Mango', 'Avocado']
print(f'A type of list is {my_list}')

coordinate_1 = (2, 3)
coordinate_2 = (10,8)

x_distance = coordinate_1[0] - coordinate_2[0]
y_distance = coordinate_1[1] - coordinate_2[1]

EuclideanDistance = (x_distance**2 + y_distance**2)**(1/2)

print(f'The Eyclidean Distance of {coordinate_1} and {coordinate_2} is {EuclideanDistance}')
