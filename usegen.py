from random import randint

class User:
    def name_gen():
        file = open('names.txt', 'r')
        files = file.read()
        names = files.split()
        length = len(names)
        random_name = names[randint(0, length)]

        return random_name
    def password(length):
        letters = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#&%qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#&%qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#&%qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#&%'
        letters = list(letters)
        i = 0
        s_key = ""
        while i < length:
            i = i+1
            lengthi = len(letters) - 1
            s_key += letters[randint(0, lengthi)]

        return s_key

    def current_age():
        age = randint(18, 75)
        return age

    def sex():
        user_sex = randint(1, 2)
        return user_sex
    def nation():
        user_nation = randint(0, 100)
        return user_nation


class Email:
    def email():
        f_name = User.name_gen()
        l_name = User.name_gen()
        email = f_name + l_name + str(randint(1000, 10000)) + User.password(8)[3:4]
        return email









