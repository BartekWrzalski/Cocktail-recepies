import py.constants as const
import requests


def get_cocktails_by_name(name):
    return requests.get(const.search_cocktail_by_name + name).json()['drinks']


def get_cocktails_by_first_letter(letter):
    return requests.get(const.search_cocktail_by_letter + letter).json()['drinks']


def lookup_cocktail_by_id(id):
    return requests.get(const.lookup_cocktail + id).json()['drinks']


def lookup_random():
    return requests.get(const.lookup_random_cocktail).json()['drinks']


def lookup_ten_random():
    return requests.get(const.lookup_ten_random_cocktails).json()['drinks']


def lookup_popular():
    return requests.get(const.lookup_popular).json()['drinks']


def get_filter_by_ingredients(ingredients):
    ingredients = ingredients.replace(", ", ",").replace(" ", "")
    return requests.get(const.filter_by_ingredients + ingredients).json()['drinks']


def get_filter_by_glass(glass):
    glass = glass.replace(" ", "_")
    return requests.get(const.filter_by_glass + glass).json()['drinks']


def get_filter_by_category(category):
    category = category.replace(" ", "_")
    return requests.get(const.filter_by_category + category).json()['drinks']


def get_filter_by_alcoholic(alcoholic):
    alcoholic = alcoholic.replace(" ", "_")
    return requests.get(const.filter_by_alcoholic + alcoholic).json()['drinks']