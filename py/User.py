from py.constants import pickle_file
import pickle


class LoginException(Exception): pass


class User:
    def __init__(self, login, password):
        self.__login = login
        self.__passwd = password
        self.__favourite = []

    def add_favourite_drink(self, cocktail):
        self.__favourite.append(cocktail)

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__passwd

    def __eq__(self, other):
        return self.__login == other.get_login() and self.__passwd == other.get_password()


def load_users_data():
    with open(pickle_file, "rb") as file:
        try:
            users = pickle.load(file)
            return users
        except EOFError:
            return []


def save_pickled(user):
    users = load_users_data()
    if not users:
        users.append(user)

    for i in range(len(users)):
        if user.__eq__(users[i]):
            users[i] = user
        if i == len(users) - 1:
            users.append(user)

    with open(pickle_file, "wb") as file:
        pickle.dump(users, file)


def sign_in(login, password):
    users = load_users_data()
    for u in users:
        if u.get_login() == login and u.get_password() == password:
            return u
    raise LoginException("Incorrect login or password")


def register(login, password):
    users = load_users_data()
    if any(u.get_login() for u in users):
        raise LoginException("User already exists")
    return User(login, password)