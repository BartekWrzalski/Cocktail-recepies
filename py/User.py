from py.constants import pickle_file
import pickle


class LoginException(Exception): pass


class User:
    currentUser = None

    def __init__(self, login, password):
        self.__login = login
        self.__passwd = password
        self.__favourite = []

    def add_favourite_drink(self, cocktail):
        self.__favourite.append(cocktail)

    def remove_favourite(self, coctail):
        self.__favourite.remove(coctail)

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__passwd

    def get_favourite(self):
        return self.__favourite

    def __eq__(self, other):
        return self.__login == other.get_login() and self.__passwd == other.get_password()


def load_users_data():
    with open(pickle_file, "rb") as file:
        try:
            users = pickle.load(file)
            return users
        except EOFError:
            return []


def save_pickled():
    users = load_users_data()
    if not users:
        users.append(User.currentUser)

    for i in range(len(users)):
        if User.currentUser.__eq__(users[i]):
            users[i] = User.currentUser
        if i == len(users) - 1:
            users.append(User.currentUser)

    with open(pickle_file, "wb") as file:
        pickle.dump(users, file)
    User.currentUser = None


def sign_in(login, password):
    users = load_users_data()
    for u in users:
        if u.get_login() == login and u.get_password() == password:
            User.currentUser = u
    if not User.currentUser:
        raise LoginException("Incorrect login or password")


def register(login, password):
    users = load_users_data()
    if any(u.get_login() == login for u in users):
        raise LoginException("User already exists")
    User.currentUser = User(login, password)
