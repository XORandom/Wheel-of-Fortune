"""
Программа: "Поле чудес"
У игрока есть несколько жизней
есть секретные слова
После угадывания слово удаляется.
"""
import methods_
import structure_

if __name__ == '__main__':
    methods_.restore_life()
    methods_.hide_word()
    while structure_.eof_flag == 0:

        print('{} | \u2665x{}'.format(structure_.hidden_word, structure_.users_life))
        users_word = input('Назовите букву или слово целиком:')
        if users_word == structure_.current_word:
            methods_.you_won()
        elif len(users_word) == 1 and users_word in structure_.current_word:
            methods_.update_word(users_word)
            if structure_.current_word == structure_.hidden_word:
                methods_.you_won()
        else:
            methods_.lose_life()
