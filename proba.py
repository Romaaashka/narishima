# # типи данних 

# # integer ( int) , прості чілі числа 
# number = 5
# age = 22
# # float , числа з комою,або дробові 
# fnumber = 5.7
# # sting (str), строка із словами 
# name = " Roma "

# # bool тільки константи  "True"  "F"alse" більше нічого 
# status = True


# # print вивід на екран ( або коментарій ), ставляться лапки тільки якщо пишеш слова або запит по типу  print (" що тут таке ")
# #  щоб вивести конертну строку не потрібні лапки просто назву перемінної вписати по типу print( name )
# # екранування це бек слеш "   \"   " перед лапками щоб не завершалась строка а читалась далі 
# print(name)

# # екранування це бек слеш "( "він\"погана\"людина") " перед лапками щоб не завершалась строка а читалась далі 
# print ( "він\"погана\"людина")

# # но якщо використовувати одинарні лапки ' ' то не обов'язково використовувати бек слеш воно і так відтвориться
# # наприклад 
# print( 'він "дуже" погана людина ')

# # перевод строки " \n" , або просто вивести дві строки із print 

# print( 'Helo\nworld')

# # конкатенация, якщо вивести конкретну перемінну за лапки і додати " + " відбувається склеювання нашої строки і тексту в перемінній 
# print( " helo my name " + name  )

# # " тайп катсинг "  тобто сковертувати тип int в перемінній " age " в тип string
# print( " мені " +str(age)+ " роки" )

# # "input" перемінна для того щоб юзер вписував те що ми від нього хочем , наприклад: 
# # name =input(" введіть своє ім'я: ")
# # age = input(" укажіть свої роки: ")

# # print( "Привіт"+name+"!")
# # print( "тобі уже "+ age + " роки це круто ")


# # +,-,*,/,степінь ** ,ділення по модулю %,мінусове число(унарный минус),заокруглення , число пі 
# #  наприклад " ділення множення піднесення до степення "
# # a = 5 
# # b = 10 

# # c = a / * "**" b

# # print(c)

# # a = 5 
# # b = 10 

# # c = a % b

# # print(c)


# # a = 20

# # a = -a 

# # заокруглення, функція round прописується в дужках print і заокруглює число до цілого , приклад написання print(round(змінна))
# # наприклад:

# a = 5.68

# print(round(a))
# є ще також дві функції для заокруглення числа примусово до меншого або більшого значення ,але щоб зробити це в пайтоні то треба імпорутвати модуль math за допомогою import,
# прикладом для написання є  impotr math 
# цим самим для заокруглення числа примусово в меншу або більшу сторону в print прописуємо модуль і дописуєм до модулю floor(якщо хочемо закоруглити до меншого числа )
# або  ceil(якщо хочемо заокруглити до більшого)
# наприклад 

# import math

# a = 5.23

# print( math.ceil(a))

# число пі 3,14 але це не точно , щоб вивести точно потрібно імпортувати модуль math за допомогою  import math і в print прописати math.pi і тоді в терміналі виведеться точне число пі 
# наприклад 
import math 

print(math.pi)