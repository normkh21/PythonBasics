# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as 'The Nile runs through Egypt.'
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {'nile': 'egypt', 'hudson': 'usa', 'volga': 'russia', 'mississippi': 'usa', 'thames': 'uk'}

# The Key  runs through VALUE

for river, country in rivers.items():
    # if country == 'usa' or  country == 'uk':
    if country in ['usa', 'uk']:
        print(f"the {river.title()} runs through {country.upper()} ")
    else:
        print(f"the {river.title()} runs through {country.title()} ")

# Use a loop to print the name of each river included in the dictionary.
print('\nRivers are: ')
for river in rivers.keys():
    print('\t', river.title(), end=" | ")

# Use a Loop to print the name of each country included in the dictionary
print('\ncountries are')
for country in rivers.values():
    if country in ['usa', 'uk']:
        print('\t', country.upper(), end=" | ")
    else:
        print('\t', country.title(), end=" | ")



print("\n\n************** 6-11. Cities: **********************")
cities = {'new york': {'country': 'USA', 'population': 8.4, 'fact': 'Big Apple'},
          'istanbul': {'country': 'Turkey', 'population': 15.52, 'fact': 'Constantinople'},
          'tashkent': {'country': 'Uzbekistan', 'population': 2.5, 'fact': 'Stone City'},
          'moscow': {'country': 'Russia', 'population': 12.53, 'fact': 'Kremlin'}
          }
# "CITY is very beautiful city in COUNTRY. it has POPULATION population and thr ity is also knwn as FACT

for city, info in cities.items():
    # print(city)
    # print(info)
    print(f"{city.title()} is very beautiful city in {info['country']}. "
          f"It has {info['population']} mln population and the city is also known as {info['fact']}.")


