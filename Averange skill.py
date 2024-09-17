grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)#упорядывачием список по возрастанию
print(students)#Проверяем порядок
a = sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])#Складываем оценки и делим на их количество
average_score = {students[0]: a[0], students[1]: a[1], students[2]: a[2], students[3]: a[3], students[4]: a[4]}#Присваиваем каждому ученику их средний балл
print(average_score)#Вот здесь посмотрел решение "https://github.com/denbaturin/homeworkDop1.py/blob/main/homeworkDop1.py" другого пока не придумал ничего