# concatenar cadenas
text1 = 'fundamentos con '
text2 = 'Python'
result = text1 + text2
print(result)
print('____________________________________')
print('')

# concatenar otra cadena
name = 'David'
lastname = 'Muñoz'
fullName = name + ' ' + lastname
print(fullName)
print('____________________________________')
print('')

#format string
price = 97
text3 = f'the price is {price:.2f} dollars'
print(text3)
print('____________________________________')
print('')

#math operacion
text4 = f'la multiplicacion es {20 * 59}'
print(text4)
print('____________________________________')
print('')

#funcion Capitalize()
text5 = 'python es un lenguaje de alto nivel de programacion'
result1 = text5.capitalize()
print(result1)
print('____________________________________')
print('')

#funcion casefold()
title = 'Cien Años de Soledad'
titleConvert = title.casefold()
print(titleConvert)
print('____________________________________')
print('')

#String center
fruit = 'banana'
textCenter = fruit.center(20, '-')
print(textCenter)
print('____________________________________')
print('')

#string count
title1 = 'I love apples, apple are my favorite fruit'
result2 = title1.count('apple')
print(result2)
print('____________________________________')
print('')

#string endswith
text6 = 'Curso, fundamentos con Python.'
result3 = text6.endswith('.')
print(result3)
print('____________________________________')
print('')

#string expandtabs
letter = 'F\tU\tP'
letterSpaces = letter.expandtabs(2)
print(letterSpaces)
print('____________________________________')
print('')

#string find
text7 = 'Hello, welcome to Colombia.'
result4 = text7.find('welcome')
print(result4)
print('____________________________________')
print('')

#funcion title
text8 = 'welcome to my world'
result5 = text8.title()
print(result5)
print('____________________________________')
print('')

#funcion isalnum
alphanumeric = 'Python312'
result6 = alphanumeric.isalnum()
print(result6)
print('____________________________________')
print('')

#funcion isalpha
letters = 'Space X'
result7 = letters.isalpha()
print(result7)