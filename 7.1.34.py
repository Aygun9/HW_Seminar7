#7.1[34]: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
#не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
#Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения 
#одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
#Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
#Если ритм есть, функция возвращает True, иначе возвращает False

#Примеры/Тесты:
    #<function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
    #<function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
    #<function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
    #<function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
    #<function_name>("Пам-парам-пурум Пум-пурум-карам") -> True


def count_vowels(word):
    vowels = "aeiouy"
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

def check_rhythm(text):
    phrases = text.split() 
    vowel_counts = [] 
    for phrase in phrases:
        words = phrase.split("-") 
        phrase_vowel_counts = [count_vowels(word) for word in words] 
        vowel_counts.append(sum(phrase_vowel_counts))
    if len(set(vowel_counts)) == 1:
        return True
    else:
        return False



print(check_rhythm("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))




