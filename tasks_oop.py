#     def __init__(self, name, phone):
# class User:
#         self.name = name
#         self.phone = phone
        
#     def show(self):
#         print(f'{self.name} ({self.phone})')

# class Friend(User):
#     def show(self):
#         print(f'Имя: {self.name} || Телефон: {self.phone}')

# user = User("Виктор Гюго", "+33 1 42 72 10 16")
# # у класса friend нет конструктора, но он есть
# # у родительского класса User, поэтому код сработает
# friend = Friend("Виктор Гюго", "+33 1 42 72 10 16")
# user.show()
# friend.show()


# импортируем функции из библиотеки math для рассчёта расстояния
# from math import radians, sin, cos, acos

# class Point:
#     def __init__(self, latitude, longitude):
#         self.latitude = radians(latitude)
#         self.longitude = radians(longitude)
        
#     # считаем расстояние между двумя точками в км
#     def distance(self, other):
#         cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
#         self.longitude - other.longitude)
#         return 6371 * acos(cos_d)

# class City(Point):
#         def __init__(self, latitude, longitude, name, population):
#               super().__init__(latitude, longitude)
#               self.name = name
#               self.population = population
#         def show(self):
#             print(f"Город {self.name}, население {self.population} чел.")
        
# class Mountain(Point):
#     def __init__(self, latitude, longitude, name, height):
#          super().__init__(latitude, longitude)
#          self.name = name
#          self.height = height
         
#     def show(self):
#         print(f'{self.name} - {self.height}')
        
# moscow = City(557558, 376173, 'Moscow', 12000000)
# moscow.show()
# everest = Mountain(2798785, 86925026, 'Everest', 8849)
# everest.show()

# comparison = Point(2798785, 86925026)
# print(comparison.distance(moscow))

class Human:
    def __init__(self, name):
        self.name = name
        
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю')
        self.question = question
        
    def __str__(self):
       return f'{self.name}'
        
class Student(Human):
    def __init__(self, name):
        super().__init__(name)
    
    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
        
        print(f'{self.someone}, {self.question}')
        someone.answer_question(question)
        print('')  
        
class Curator(Human):
    def __init__(self, name):
        super().__init__(name)
        
    def answer_question(self, question):
        if question == "Марина, мне грустненько, что делать?":
             print('Отдохни и возвращайся с вопросами по теории.')
        else:
            super().answer_question(question)

class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)
        
    def answer_question(self, question):
        if question == 'Ира, мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == 'Ира, как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)
    
        

class CodeReviewer(Human):
    def __init__(self, name):
        super().__init__(name)

    def answer_question(self, question):
        if question == 'Евгений, что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        elif question == 'Евгений, когда каникулы?':
            print('Очень интересный вопрос! Не знаю.')
        else:
            super().answer_question(question)


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')




