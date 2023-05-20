class Diary():
    def __init__(self):
        self.students = []
    def setstudent(self, student):
        self.students.append(student)

class Student():
    def __init__(self):                             # метод __init__ вызывается как только мы создаём экземпляр класса
        self.name = ""
        self.marks = []
    def __str__(self):                              # метод __str__ вызывается, когда мы выводим экземпляр класса на экран
        return f"Имя: {self.name}, оценки: {self.marks}"
    def setname(self, who):
        self.name = who
    def setmark(self, score):
        self.marks.append(score)

dnev = Diary()

# считывание учеников из базы данных (из файла)
# коммент

f = open("diary.txt", "r")
while True:
    flag = 0                                        # если 0, то ученика нет в дневнике, если 1 - то он есть
    name = f.readline()                             # читаем одну строку (имя) из файла f в переменную name
    name = name[0:-1]                               # обрезаем \n на конце имени
    if name == "":
        break
    
    for i in range(len(dnev.students)):             # проходимся по списку с учащимися
        if name == dnev.students[i].name:           # проверка, есть ли ученик с таким же именем уже в дневнике
            flag = 1                                # если ученик с таким именем уже есть, flag = 1
            num_st = i
            
    if flag == 0:                                   # выполняется, если ученика пока в дневнике нет (то есть надо его создать)
        student = Student()                         # создаём ученика
        student.setname(name)                       # даём имя ученику
        
    marks_str = f.readline()                        # читаем одну строку (оценки) из файла f в переменную marks_str
    marks_list = marks_str.split("; ")              # разделяем строку с оценками через ; и записываем в список marks_list
    
    for score in marks_list:                        # проходимся по оценкам в списке marks_list
        if '\n' in score:                           # если в оценке есть \n, то
            score = score[0:-1]                     # убираем \n из оценки
        if flag == 0:
            student.setmark(score)                  # добавляем оценку ученику (новому)
            dnev.setstudent(student)
        else:
            dnev.students[num_st].setmark(score)    # добавляем оценку ученику (с тем же именем)
        
f.close()

# считываем учеников, которых вводит преподаватель и записываем их в дневник

f = open("diary.txt", "w")                          # открываем файл на запись (с чистого листа)
print("Приветствуйем на портале ""ГМЭЖД""")
stud = input("Введите ученика, пример: Иван Иванов\n").strip(' ')                               # вводим ученика и обрезаем пробелы
score = input("Введите оценку этого ученика и дату выставления пример: 5, 02.03\n")             # вводим оценку ученика и дату оценки
next_or_close = input("Если вы хотите продолжить, напишите Далее, если закончить - Закрыть\n")  # вводим информацию о продолжении или закрытии


while next_or_close != "Закрыть":                                   # цикл работает, пока мы не введём "Закрыть"
    
    if stud == '' and score == '' and next_or_close == '':          # проверка на пустые вводы
        pass                                                        

    flag = 0
    
    for i in range(len(dnev.students)):             # проходимся по списку с учащимися
        if stud == dnev.students[i].name:           # проверка, есть ли ученик с таким же именем уже в дневнике
            flag = 1                                # если ученик с таким именем уже есть, flag = 1
            num_st = i                              

    if flag == 0:                                   # выполняется, если ученика пока в дневнике нет (то есть надо его создать)
        student = Student()                         # создаём ученика
        student.setname(stud)                       # даём имя ученику
        print("Имя:", student.name)
        
    if flag == 0:
        student.setmark(score)                  # добавляем оценку ученику (новому)
        dnev.setstudent(student)
    else:
        dnev.students[num_st].setmark(score)    # добавляем оценку ученику (с тем же именем)
        
    stud = input("Введите ученика, пример: Иван Иванов\n").strip(' ')
    score = input("Введите оценку этого ученика и дату выставления пример: 5, 02.03\n")
    next_or_close = input("Если вы хотите продолжить, напишите Далее, если закончить - Закрыть\n")
    
if next_or_close == "Закрыть":

    flag = 0
    
    for i in range(len(dnev.students)):             # проходимся по списку с учащимися
        if stud == dnev.students[i].name:           # проверка, есть ли ученик с таким же именем уже в дневнике
            flag = 1                                # если ученик с таким именем уже есть, flag = 1
            num_st = i                              

    if flag == 0:                                   # выполняется, если ученика пока в дневнике нет (то есть надо его создать)
        student = Student()                         # создаём ученика
        student.setname(stud)                       # даём имя ученику

    if flag == 0:
        student.setmark(score)                  # добавляем оценку ученику (новому)
        dnev.setstudent(student)
    else:
        dnev.students[num_st].setmark(score)    # добавляем оценку ученику (с тем же именем)

    for st in dnev.students:
        
        print("Ученик:", st.name)
        print("Оценки ученика:", '; '.join(st.marks))
        
        f.write(st.name + "\n")
        f.write('; '.join(st.marks) + "\n")
        
f.close()        
