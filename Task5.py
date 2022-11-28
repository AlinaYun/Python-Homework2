# Написать программу, которая будет ввыводит в консоль заданный текст (Python - один из самых популярных языков программирования в мире), затем принимать из консоли шаблон подстроки и 
# удалять в задданом тексте все слова в которых присутствует введенный шаблон
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире

text = "Python - один из самых популярных языков программирования в мире"

def delete_words(given_text, text_to_delete):
    given_text = given_text.split()
    result = []
    for word in given_text:
        if text_to_delete not in word:
            result.append(word)
    print (*result)

print(text)
delete_words(text, input("Введите подстроку: "))
