#------------------1-------------------

numbers = [10, 20, 10, 30, 20, 40, 10, 50]
set1 = set(numbers)
print(numbers)
print(set1)

unique = len(set1)
print(unique)

is_30 = 30 in set1
print(is_30)

is_100 = 100 in set1
print(is_100)

#------------------2-------------------

data = [15, "Python", 15, True, "Python", 3.14, False, True]
set2 = set(data)
print(set2)

set2.add("Redis")
set2.add(100)
set2.discard("Python")

is_true = True in set2
print(is_true)

is_false = False in set2
print(is_false)

#------------------3-------------------

python_students = {"Anna", "Oleh", "Ivan", "Maria"}
redis_students = {"Oleh", "Maria", "Petro", "Sofia"}

union = python_students | redis_students
union2 = python_students.union(redis_students)

if union == union2:
    print("Union sets are equal")

#------------------4-------------------

intersection = python_students & redis_students
intersection2 = python_students.intersection(redis_students)
print(intersection)

#------------------5-------------------

all_students = {"Anna", "Oleh", "Ivan", "Maria", "Petro", "Sofia"}
python_students = {"Anna", "Oleh", "Ivan"}

difference = all_students - python_students
difference2 = all_students.difference(python_students)
print(difference)

#------------------6-------------------

numbers = {10, 20, 30}

numbers.add(40)
numbers.add(40)
numbers.update([50, 60, 70])

numbers.remove(20)
numbers.discard(100)

print(numbers.pop())
print(numbers)
