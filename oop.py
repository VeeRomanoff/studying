# class Person:
#     def __init__(self, name, last_name, place_of_birth):
#         self.name = name
#         self.last_name = last_name
#         self.place_of_birth = place_of_birth


# person2 = Person('Kanye', 'West', 'USA')

# print(type(person2))
    
    
# class Robot:
#     """
#     This class implements a robot
#     """
#     def __init__(self, name, year_of_issue):
#         self.name = name 
#         self.year_of_issue = year_of_issue
#         ### left is name of atributes, right -- is name of parameters
#         ### self -- is an object itself
        
# r1 = Robot('Marvin', 2015)
# r2 = Robot('Sullivan', 2025)
# print(r2.year_of_issue)
# print(r1.year_of_issue) # this is how you reach some atrib in object 
# print(r1.__dict__) # this gives us a dictionary that stores the object's atributes {'key': 'Value'} 

# person_1 = {'Name': 'William', 'phone': '+79896729079', 'is_Married': True}
# person_2 = {'Name': 'Geroge', 'phone': '+12349927682', 'is_Married': False}
# person_3 = {'Name': 'Tom', 'phone': '+44123456622', 'is_Married': False}


# class Contact(): 
    # def __init__(self, name, phone, address, birthday):
    #     self.name = name
    #     self.phone = phone
    #     self.address = address 
    #     self.birthday = birthday
        
    # def show(self):
    #     print(f'{self.name} - адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}')
        
    # def show_contact(self):
    #     print(f'{self.name} - адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}')
        
        
        
# mike = Contact('Михаил Булгаков', '2-03-27', 'Россия, Москва, Большая Пироговская, дом 35б, кв. 6', '15.05.1891')
# vlad = Contact('Владимир Маяковский', '73-88', 'Россия, Москва, Лубянский проезд, д. 3, кв. 12', '19.07.1893')
# mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
# mike.phone = 'К-058-67'
# vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
# vlad.phone = '2-35-71'

# mike.show_contact()
# vlad.show_contact()


# import math

# class Planet:
    # def __init__(self, name, radius, temp_celcius):
    #     self.name = name
    #     self.surface_area = 4 * math.pi * radius * radius
    #     self.average_temp_celcius = temp_celcius
    #     self.average_temp_fahrenheit = temp_celcius * 9 / 5 + 32
        
    # def show_info(self):
    #     print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
    #     print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit}° по Фаренгейту.")

# jupiter = Planet('Юпитер', 69911, -107)
# venus = Planet('Венера', 6051, 462)

# jupiter.show_info()
# venus.show_info()


class Rapper():
    def __init__(self, name, age, how_famous):
        self.name = name
        self.age = age
        self.how_famous = how_famous
        
    def still_performing(self):
        return True

class ASAPRocky(Rapper):
    def __init__(self, name, age, how_famous):
        super().__init__(name, age, how_famous)
                
class KanyeWest(Rapper):
    def __init__(self, name, age, how_famous):
        super().__init__(name, age, how_famous)                
        

class RM(Rapper):
    def __init__(self, name, age, how_famous):
        super().__init__(name, age, how_famous)        
        

asap_rocky = ASAPRocky('ASAPRocky', 34, 10)
kanye_west = KanyeWest('YE West', 45, 10)
rm = RM('Kim Nam-joon', 28, 7)

# print(rm.name, rm.age, rm.how_famous)
# print(rm.still_performing())


class Feline():
    def __init__(self, name, color, age, is_Angry):
        self.name = name
        self.color = color
        self.age = age
        self.is_Angry = is_Angry
    
    def meow(self):
        return 'Meow!'
    
    
class Panthera(Feline):
    def __init__(self, name, color, age, is_Angry):
        super().__init__(name, color, age, is_Angry)
        
    def haunting_rate(self):
        if self.age < 2:
            return """He's still not good at haunting"""
        elif self.age < 10:
            return """He's really good at haunting"""
        else:
            return """Our buddy is pretty old for haunting"""

class Cat(Feline):
    def __init__(self, name, color, age, is_Angry, friendliness):
        super().__init__(name, color, age, is_Angry)
        self.friendliness = friendliness

class Cheetah(Feline):
    def __init__(self, name, color, age, is_Angry):
        super().__init__(name, color, age, is_Angry)
        
    def velocity_amount(self):
        return 9
        

class Hybrid(Panthera, Cheetah):
    def __init__(self, name, color, age, is_Angry):
        super().__init__(name, color, age, is_Angry)
    

cheethera = Hybrid('Samuel', "black", 7, True)
# print(cheethera.name, cheethera.color, cheethera.age, cheethera.is_Angry)
# print(cheethera.haunting_rate())
# print(cheethera.velocity_amount())









from math import pi

class Shape:
    def __init__(self, name):
        self.name = name
        
    def area(self):                                                                                                                 
        pass
    
    def fact(self):
        return "Я - двумерная фигура"
    
    def __str__(self):
        return self.name



class Square(Shape):
    def __init__(self, length):
        super().__init__("Квадрат")
        self.length = length
        
    def area(self):
        return self.length ** 2
    
    def fact(self):
        return "Любой угол квадрата равен 90 градусов."
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius
        
    def area(self):
        return pi * self.radius ** 2
    
a = Square(5)
b = Circle(10)

print(b)
print(b.fact())
print(a.fact())
print(b.area())