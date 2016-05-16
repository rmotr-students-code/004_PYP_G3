def only_int_arguments(f):
    def new_func(a, b):
        # before
        if type(a) != int or type(b) != int:
            raise AttributeError("Both args should be ints")

        original_result = f(a, b)

        # after
        return original_result

    return new_func


@only_int_arguments   # this
def add(x, y):
    "Adds two numbers"
    return x + y


new_add = only_int_arguments(add)

# Here
# result = add(2, 3)
# print(result)

# imdb/
#    actors.txt
#    movies.txt

db.actors.insert(1, 'Kevin Bacon', date(1958, 7, 8))
pyp_database.create_database('imdb')
db = pyp_database.use('imdb')
db.create_table('actors', columns=['id', 'name', 'date_of_birth'])

db.actors

db.create_table('X99', columns=['id', 'name', 'date_of_birth'])

db.X99


