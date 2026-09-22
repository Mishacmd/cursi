set_data = {42, 777, 'qwerty', 44, 44, 42, 6, 298}
print(set_data)

set_data2 = set([888,44,2,6,2])
set_3 = {1,2,3,4,5,6,7,8,9,0}

union = set_data | set_data2
print(union)

intersection = union & set_3
print(intersection)

difference = set_data - set_3
print(difference)

result = set_data ^ set_data2
print(result)

set_data.add(1000)
print(set_data)

set_data.remove(1000)
print(set_data)

set_data.update([178239, 68127, 809213])
print(set_data)

union2 = set_data | union
print(union2)

union2.discard(44)
print(union2)
union2.discard(44)
print(union2)