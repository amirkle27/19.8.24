oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
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













