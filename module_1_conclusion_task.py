listOfgrades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort = sorted(list(students))
mean_grade_list = list(map(lambda a: sum(a)/len(a), listOfgrades))
mean_grade_dict = dict(map(lambda x,y: (x, y), students_sort, mean_grade_list))
print(mean_grade_dict)