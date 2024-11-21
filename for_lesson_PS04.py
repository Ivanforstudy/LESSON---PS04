

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


#browser = webdriver.Chrome()
#browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
# Для создания скриншота пишем:
#browser.save_screenshot("dom.png")
#time.sleep(5)
#browser.quit()
# Для переключения на следующую страницу меняем browser.quit() на browser.get()
#browser.get("https://ru.wikipedia.org/wiki/Selenium")
# Тут так же создаем скриншот:
#browser.save_screenshot("selenium.png")
#time.sleep(5)
# Для перезагрузки страницы пишем:
#browser.refresh()
#time.sleep(5)

# Добавляем библиотеку, которая позволяет вводить данные на сайт с клавиатуры:
# from selenium.webdriver import Keys
# Также добавляем библиотеку для поисков элементов на сайте: from selenium.webdriver.common.by import By
#browser = webdriver.Chrome()
#browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
# Ищем на странице слово Википедия:
#assert "Википедия" in browser.title
#time.sleep(10)

#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
#search_box = browser.find_element(By.ID, "searchInput")
#search_box.send_keys("Солнечная система")
#time.sleep(3)

# Ищем на странице слово Википедия:
#Добавляем не только введение текста, но и его отправку
#search_box.send_keys(Keys.RETURN)
#time.sleep(5)
# A - ссылка
#a = browser.find_element(By.LINK_TEXT, "Солнечная система")
#Добавляем клик на элемент
#a.click()
#time.sleep(5)

#9. Запускаем программу.
#find_element находит первый попавшийся элемент, подходящий под условия поиска.
#find_elements находит несколько элементов





# Попробуем брать контент с сайта.

import random
browser = webdriver.Chrome()
#Далее одинаково для всех браузеров

#Сразу заходим на страницу солнечной системы
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")
time.sleep(5)
#2. Исследуем код параграфов на странице. Находим тег.

#3. Пишем новый код:

#paragraphs = browser.find_elements(By.TAG_NAME, "p")
#Для перебора пишем цикл
#for paragraph in paragraphs:
#    print(paragraph.text)
#    input()


#Запускаем программу. Каждый раз, нажимая на клавишу Enter,
# мы будем получать последующий параграф (абзац) текста статьи.
#Удаляем код для параграфов и пишем новый код:

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
#Чтобы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
      hatnotes.append(element)

print(hatnotes)
hatnote = random.choice(hatnotes)

#Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)
time.sleep(5)