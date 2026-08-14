# Написать функцию, которая получает на вход список словарей, содержащих информацию о фильмах (например, название, жанр, режиссер и т. д.), и возвращает новый список, содержащий только те фильмы, которые относятся к заданному жанру.
# Пример ввода:
# [{title: 'The Shawshank Redemption', genre: 'Drama', director: 'Frank Darabont'}, {title: 'The Godfather', genre: 'Crime', director: 'Francis Ford Coppola'}, {title: 'The Dark Knight', genre: 'Action', director: 'Christopher Nolan'}], 'Drama'
#
# Пример вывода:
# [{title: 'The Shawshank Redemption', genre: C, director: 'Frank Darabont'}]


def filter_film_by_genre(my_list, my_genre):
    # new_list = []
    # for i in my_list:
    #     if my_genre == i['genre']:
    #         new_list.append(i)
    # return new_list
    return [i for i in my_list if i["genre"] == my_genre]


list = [
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "director": "Frank Darabont",
    },
    {"title": "The Godfather", "genre": "Crime", "director": "Francis Ford Coppola"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"},
]

genre = "Drama"

print(filter_film_by_genre(list, genre))
