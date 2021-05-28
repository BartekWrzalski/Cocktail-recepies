from py.config import cocktail_key
import requests

KEY = cocktail_key

pickle_file = "py/users_data.p"

categories = [cat for cat in
              requests.get(f"https://www.thecocktaildb.com/api/json/{KEY}/list.php?c=list").json()["drinks"]]

glasses = [gls for gls in
           requests.get(f"https://www.thecocktaildb.com/api/json/{KEY}/list.php?g=list").json()["drinks"]]

ingredients = [ingr for ingr in
               requests.get(f"https://www.thecocktaildb.com/api/json/{KEY}/list.php?i=list").json()["drinks"]]

alcoholic_filters = [alc for alc in
                     requests.get(f"https://www.thecocktaildb.com/api/json/{KEY}/list.php?a=list").json()["drinks"]]

# Search cocktail by name
search_cocktail_by_name = f"https://www.thecocktaildb.com/api/json/{KEY}/search.php?s="

# Search cocktail by first letter
search_cocktail_by_letter = f"https://www.thecocktaildb.com/api/json/{KEY}/search.php?f="

# Lookup cocktail by id
lookup_cocktail = f"https://www.thecocktaildb.com/api/json/{KEY}/lookup.php?i="

# Look up random cocktail
lookup_random_cocktail = f"https://www.thecocktaildb.com/api/json/{KEY}/random.php"

# Look up 10 random cocktails
lookup_ten_random_cocktails = f"https://www.thecocktaildb.com/api/json/{KEY}/randomselection.php"

# Look up popular
lookup_popular = f"https://www.thecocktaildb.com/api/json/{KEY}/popular.php"

# Filter by ingredients
filter_by_ingredients = f"https://www.thecocktaildb.com/api/json/{KEY}/filter.php?i="

# Filter by alcoholic
filter_by_alcoholic = f"https://www.thecocktaildb.com/api/json/{KEY}/filter.php?a="

# Filter by category
filter_by_category = f"https://www.thecocktaildb.com/api/json/{KEY}/filter.php?c="

# Filter by glass
filter_by_glass = f"https://www.thecocktaildb.com/api/json/{KEY}/filter.php?g="
