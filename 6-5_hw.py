#Exercise #1
#Filter out all of the empty strings from the list below
#Output: ['Argentina', 'San Diego', 'Boston', 'New York']
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]
print(list(filter(lambda place: place.strip() != "", places)))
print()


#Exercise #2
#Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"
#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 
# 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']
author = ["Joel Carter", "Victor aNisimov", 
          "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
print(sorted(author, key=lambda x: x.split()[-1].lower()))
print()


#Exercise #3
#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
print(list(map(lambda x: (x[0], (9/5)* x[-1] + 32), places)))
print()



#Exercise #4
#Create a generator function that individually returns each movie genre back from the list
genres = ["adventure", "drama", "horror", "comedy", "action", "romance"]
def exercise_4(cinema):
    for i in cinema:
        yield i

gen_genres = exercise_4(genres)

def try_catch():
    try:
        print(next(gen_genres))
    except:
        print("End of the list")