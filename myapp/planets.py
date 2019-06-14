nquery = """
{
  planet(id: "ID_PLANETA") {
    name
    diameter
    rotationPeriod
    orbitalPeriod
    gravity
    population
    climates
    terrains
    surfaceWater
    residentConnection{
      edges{
        node{
          id
          name
        }
      }
    }
    filmConnection {
      edges {
        node {
          id
          title
        }
      }
    }
    created
    edited
    id
    }
}
"""

data = {
  "data": {
    "planet": {
      "name": "Tatooine",
      "diameter": 10465,
      "rotationPeriod": 23,
      "orbitalPeriod": 304,
      "gravity": "1 standard",
      "population": 200000,
      "climates": [
        "arid"
      ],
      "terrains": [
        "desert"
      ],
      "surfaceWater": 1,
      "residentConnection": {
        "edges": [
          {
            "node": {
              "id": "cGVvcGxlOjE=",
              "name": "Luke Skywalker"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjI=",
              "name": "C-3PO"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjQ=",
              "name": "Darth Vader"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjY=",
              "name": "Owen Lars"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjc=",
              "name": "Beru Whitesun lars"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjg=",
              "name": "R5-D4"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjk=",
              "name": "Biggs Darklighter"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjEx",
              "name": "Anakin Skywalker"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjQz",
              "name": "Shmi Skywalker"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjYy",
              "name": "Cliegg Lars"
            }
          }
        ]
      },
      "filmConnection": {
        "edges": [
          {
            "node": {
              "id": "ZmlsbXM6MQ==",
              "title": "A New Hope"
            }
          },
          {
            "node": {
              "id": "ZmlsbXM6Mw==",
              "title": "Return of the Jedi"
            }
          },
          {
            "node": {
              "id": "ZmlsbXM6NA==",
              "title": "The Phantom Menace"
            }
          },
          {
            "node": {
              "id": "ZmlsbXM6NQ==",
              "title": "Attack of the Clones"
            }
          },
          {
            "node": {
              "id": "ZmlsbXM6Ng==",
              "title": "Revenge of the Sith"
            }
          }
        ]
      },
      "created": "2014-12-09T13:50:49.641000Z",
      "edited": "2014-12-21T20:48:04.175778Z",
      "id": "cGxhbmV0czox"
    }
  }
}


query = nquery.replace("ID_PLANETA","cGxhbmV0czox")
# print(query)
dict_planet = data["data"]["planet"]

# dict_persons = {dict_planet["residentConnection"]["id"]:dict_planet["homeworld"]["name"]}

dict_persona = {}
for dict in dict_planet["residentConnection"]["edges"]:
    dict_persona[dict["node"]["id"]] = dict["node"]["name"]

dict_pelicula = {}
for dict in dict_planet["filmConnection"]["edges"]:
    dict_pelicula[dict["node"]["id"]] = dict["node"]["title"]


dict_planet["residentConnection"] = dict_persona
dict_planet["filmConnection"] = dict_pelicula

print(dict_planet)
