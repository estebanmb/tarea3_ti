query = """
{
      allFilms {
        edges {
          node {
            title
            releaseDate
            director
            producers
            episodeID
            id
          }
        }
      }
    }
"""

data = {
  "data": {
    "allFilms": {
      "edges": [
        {
          "node": {
            "title": "A New Hope",
            "releaseDate": "1977-05-25",
            "director": "George Lucas",
            "producers": [
              "Gary Kurtz",
              "Rick McCallum"
            ],
            "episodeID": 4,
            "id": "ZmlsbXM6MQ=="
          }
        },
        {
          "node": {
            "title": "The Empire Strikes Back",
            "releaseDate": "1980-05-17",
            "director": "Irvin Kershner",
            "producers": [
              "Gary Kurtz",
              "Rick McCallum"
            ],
            "episodeID": 5,
            "id": "ZmlsbXM6Mg=="
          }
        },
        {
          "node": {
            "title": "Return of the Jedi",
            "releaseDate": "1983-05-25",
            "director": "Richard Marquand",
            "producers": [
              "Howard G. Kazanjian",
              "George Lucas",
              "Rick McCallum"
            ],
            "episodeID": 6,
            "id": "ZmlsbXM6Mw=="
          }
        },
        {
          "node": {
            "title": "The Phantom Menace",
            "releaseDate": "1999-05-19",
            "director": "George Lucas",
            "producers": [
              "Rick McCallum"
            ],
            "episodeID": 1,
            "id": "ZmlsbXM6NA=="
          }
        },
        {
          "node": {
            "title": "Attack of the Clones",
            "releaseDate": "2002-05-16",
            "director": "George Lucas",
            "producers": [
              "Rick McCallum"
            ],
            "episodeID": 2,
            "id": "ZmlsbXM6NQ=="
          }
        },
        {
          "node": {
            "title": "Revenge of the Sith",
            "releaseDate": "2005-05-19",
            "director": "George Lucas",
            "producers": [
              "Rick McCallum"
            ],
            "episodeID": 3,
            "id": "ZmlsbXM6Ng=="
          }
        },
        {
          "node": {
            "title": "The Force Awakens",
            "releaseDate": "2015-12-11",
            "director": "J. J. Abrams",
            "producers": [
              "Kathleen Kennedy",
              "J. J. Abrams",
              "Bryan Burk"
            ],
            "episodeID": 7,
            "id": "ZmlsbXM6Nw=="
          }
        }
      ]
    }
  }
}

lista_peliculas = [pelicula["node"] for pelicula in data["data"]["allFilms"]["edges"]]
peliculas = []
for i in lista_peliculas:
    peliculas.append({"title": i['title'], "id": i['episodeID'],
     "year": i["releaseDate"][:4], "director": i["director"], "productor": i["producers"],
     "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/1200px-Star_Wars_Logo.svg.png"})

print(peliculas[0])
dictionary = {'peliculas': peliculas}
print(dictionary)


a = {"x":"gato","b":12}
b = str(a)
print(a)
print(b)

# para pedir lo que se tiene de una pelicula dado el id
q = """
{
  film(id: "ZmlsbXM6MQ==") {
    title
    episodeID
    openingCrawl
    director
    producers
    releaseDate
    created
    edited
    id
    }
}
"""

# para saber los tipos de atributos:
# {
#   __type(name: "Film") {
#     name
#     fields {
#       name
#     }
#   }
# }
