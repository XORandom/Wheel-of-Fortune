"""
Здесь будут используемые методы
"""
import random
import structure_


def you_won():
    """
    Сообщает о победе игрока и предлагает сыграть еще, если слова еще есть.
    :return:
    """
    print('Вы выиграли! Приз в студию!')

    # Если слова не закончились
    if structure_.eof_flag == 0:
        if input('Сыграем еще раз, да/нет: ') == 'да':
            restore_life()
            hide_word()
        else:
            structure_.eof_flag = 1
    else:
        print('Закончились слова')
        structure_.eof_flag = 1


def restore_life():
    """
    Восстанавливает здоровье игрока. Выполняется в начале игры или при повторной игре. Символ здоровья \u2665.
    :return: users_life = здоровье игрока.
    """
    if structure_.mode == 'easy':
        structure_.users_life = 3
    elif structure_.mode == 'medium':
        structure_.users_life = 5
    elif structure_.mode == 'hard':
        structure_.users_life = 7


def lose_life():
    """
    Удаляет здоровье при потере жизни игроком. Символ здоровья \u2665. users_life = здоровье игрока.
    :return:
    """
    print('Неправильно. Вы теряете жизнь')
    if structure_.users_life > 1:
        structure_.users_life -= 1
    else:
        structure_.eof_flag = 1
        print('Жизни закончились!')


def hide_word():
    """
    Выбирает слово из списка и скрывает от пользователя за символом \u25A0. Создает экземпляр для сравнения.
    :return:
    """

    if len(structure_.bag_of_words) == 1:
        structure_.current_word = structure_.bag_of_words[0]
        structure_.bag_of_words.remove(structure_.current_word)  # Добавить функционал удаления слов
    else:
        structure_.current_word = random.choice(structure_.bag_of_words)  # Выбрать случайное слово из списка
        structure_.bag_of_words.remove(structure_.current_word)  # Добавить функционал удаления слов
        structure_.hidden_word = '\u25A0'*len(structure_.current_word)  # Создать замаскированное слово
    if not structure_.bag_of_words:
        structure_.eof_flag = 1
        print('Закончились слова')
    return structure_.hidden_word


def update_word(users_word):
    """
    Обновляет слово, раскрывая скрытые символы.
    :return:
    """

    for i in range(len(structure_.current_word)):
        if users_word == structure_.current_word[i]:
            new = structure_.hidden_word[:i] + users_word + structure_.hidden_word[i+1:]
            structure_.hidden_word = new

