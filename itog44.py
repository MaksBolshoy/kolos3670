#| Задание 44 |
#| --- |
#| В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. Ваша задача перевести его
#  в one hot вид. Сможете ли вы это сделать без get_dummies?





import random
import pandas as pd
lst = ['robot'] * 10 # создает массив с 10 словами robot
lst += ['human'] * 10 # создает и склеивает с предидущим массивом массив из 10 слов human
random.shuffle(lst) # перемешивает получившийся массив в случайном порядке
dictionary = {'whoAmI':lst} # создаем словарь с ключем whoAmI
data = pd.DataFrame(dictionary) # создаем датафрейм из получившегося словаря

data.head() # не использовали для проверки результата
result = pd.get_dummies(data) # тут делаем преобразование one hot

print(result)

# тут делаем one hot в ручную
# сначала объявлем переменную куда запишем результат
res = [{}] * len(lst) 
# делаем цикл в котором по индексу достаем значения из массива lst
for i in range(len(lst)):
    # если значение в массиве по индексу равно human тогда создаем словарь с ключами и их наличием 0 или 1
    if lst[i] == 'human':
        res[i] = {'whoAmI_human': 1,'whoAmI_robot': 0}

    elif lst[i] == 'robot':
        res[i] = {'whoAmI_human': 0,'whoAmI_robot': 1}

# для красоты делаем заголовок который будет отображать заголовок нашей таблицы
print("\twhoAmI_human\twhoAmI_robot")
resultString = ""
# собираем результирующую строку по индексу обходя получившейся массив res который мы сформировали выше
for index in range(len(res)):
    resultString += str(index) + '\t\t' + str(res[index]['whoAmI_human']) + '\t\t' + str(res[index]['whoAmI_robot']) + '\n'
print(resultString)










