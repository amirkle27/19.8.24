oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
{"Christian Bale", "Michael Caine", "Gary Oldman",
"Tom Hardy", "Joseph Gordon-Levitt"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

#1.a

print(" 1.a ".center(50,"="))

oscar_winners.add("emma watson")

#1.b

print(" 1.b ".center(50,"="))

oscar_winners.clear()

#1.c

print(" 1.c ".center(50,"="))
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}

OW = oscar_winners.copy()

#1.d

print(" 1.d ".center(50,"="))

oscar_winners.discard("Meryl Streep")

#1.e

print(" 1.e ".center(50,"="))

same_titanic_knight = titanic_actors.intersection(dark_knight_actors)
if same_titanic_knight:
    print(f"Actors that have appeared both in Titanic and The Dark Knight are: {same_titanic_knight} ")
else:
    print("Titanic and The Dark Knight have no common actors")


#1.f

print(" 1.f ".center(50,"="))

same_iron_avengers = iron_man_actors.intersection(avengers_actors)
if same_iron_avengers:
    print(f"Actors that have appeared both in Iron Man and Avengers are: {same_iron_avengers} ")
else:
    print("Iron Man and Avengers have no common actors")

#1.g

print(" 1.g ".center(50,"="))

print(f"Have all the actors in the Actors List won the Oscar? {actor_list.issuperset(oscar_winners)}")

#1.h

print(" 1.h ".center(50,"="))

print(f"Does the 'Actors List' list contain all the actors from Avengers? {actor_list.issuperset(avengers_actors)} ")

#1.i

print(" 1.i ".center(50,"="))

import random
random_actor = random.choice(list(movie_cast))
movie_cast.discard(random_actor)

#1.j

print(" 1.j ".center(50,"="))

movie_cast.discard("Will Smith")

#1.k

print(" 1.k ".center(50,"="))

titanic_no_oscar =  titanic_actors.difference(oscar_winners)
print(f"Actors in 'Titanic' that didn't win the Oscar are: {titanic_no_oscar}")

#1.l

print(" 1.l ".center(50,"="))

titanic_or_knight = titanic_actors.symmetric_difference(dark_knight_actors)
print(f"Actors that have appeared in Titanic or The Dark Knight, but not in both are: {titanic_or_knight}")

#1.m

print(" 1.m ".center(50,"="))

oscar_winners.update ({"Blanchett Cate", "Lewis-Day Daniel"})

#1.n

print(" 1.n ".center(50,"="))

titanic_and_knight = titanic_actors.union(dark_knight_actors)
print(f"All the actors from Titanic and The Dark Knight are: {titanic_and_knight}")

#1.o

print(" 1.o ".center(50,"="))

dark_knight_rises_actors = {"Christian Bale", "Michael Caine", "Gary Oldman",
"Tom Hardy", "Joseph Gordon-Levitt"}
print(f"Have all the actors from 'The Dark Knight' appeared in 'Dark Knight Rises? {dark_knight_actors <= dark_knight_rises_actors}")


#1.p

print(" 1.p ".center(50,"="))


print(f"Have all the Legendary Actors won the Oscar? {legendary_actors>=oscar_winners} ")


#1.q

print(" 1.q ".center(50,"="))

print(f"These actors from 'Avengers' didn't appear in 'Iron man: {avengers_actors-iron_man_actors}")

#1.r

print(" 1.r ".center(50,"="))

print(f"These actors have appeared only in 'The Dark Knight' or 'Avengers': {dark_knight_actors^avengers_actors}")

#1.s

print(" 1.s ".center(50,"="))

print(f"All the actors from 'The Dark Knight' and 'Iron Man' are: {dark_knight_actors | iron_man_actors}")

#1.t

print(" 1.t ".center(50,"="))

legendary_actors_frozen = frozenset(legendary_actors)

#2

print(" 2 ".center(50,"="))

print("You can't use an index no. in sets because the elements don't keep their original position and are not position-based.")

#3

print(" 3 ".center(50,"="))

print("Sets and dicts are similar in the way that there could be no duplicacy. \nIn dictionaries there couldn't be more than one key with the same way, and that makes the entry unique and specipic. \nBecause Sets can't have duplicate values, all the elements kept in them are unique and specific too, by nature. ")

#4

print(" 4 ".center(50,"="))

one_to_hundred = set (i for i in range (1, 101) )

#5

print(" 5 ".center(50,"="))

import random
r_num = [random.randint (100, 500) for _ in range (50)]
r_num_set = set(r_num)
print(f"In a random list of 50 numbers from 100 to 500, there were {len(r_num_set)} unique numbers")
