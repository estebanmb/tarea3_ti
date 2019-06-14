nquery = """
{
  person(id: "ID_PERSONAJE") {
    name
    birthYear
    eyeColor
    gender
    hairColor
    height
    mass
    skinColor
    homeworld {
      id
      name
    }
    filmConnection {
      edges {
        node {
          id
          title
        }
      }
    }
    starshipConnection{
      edges{
        node{
          id
          name
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
    "person": {
      "name": "Luke Skywalker",
      "birthYear": "19BBY",
      "eyeColor": "blue",
      "gender": "male",
      "hairColor": "blond",
      "height": 172,
      "mass": 77,
      "skinColor": "fair",
      "homeworld": {
        "id": "cGxhbmV0czox",
        "name": "Tatooine"
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
              "id": "ZmlsbXM6Mg==",
              "title": "The Empire Strikes Back"
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
              "id": "ZmlsbXM6Ng==",
              "title": "Revenge of the Sith"
            }
          },
          {
            "node": {
              "id": "ZmlsbXM6Nw==",
              "title": "The Force Awakens"
            }
          }
        ]
      },
      "starshipConnection": {
        "edges": [
          {
            "node": {
              "id": "c3RhcnNoaXBzOjEy",
              "name": "X-wing"
            }
          },
          {
            "node": {
              "id": "c3RhcnNoaXBzOjIy",
              "name": "Imperial shuttle"
            }
          }
        ]
      },
      "created": "2014-12-09T13:50:51.644000Z",
      "edited": "2014-12-20T21:17:56.891000Z",
      "id": "cGVvcGxlOjE="
    }
  }
}

query = nquery.replace("ID_PERSONAJE","cGVvcGxlOjE=")
# print(query)
dict_person = data["data"]["person"]

dict_homeworld = {dict_person["homeworld"]["id"]:dict_person["homeworld"]["name"]}

dict_pelicula = {}
for dict in dict_person["filmConnection"]["edges"]:
    dict_pelicula[dict["node"]["id"]] = dict["node"]["title"]

dict_starship = {}
for dict in dict_person["starshipConnection"]["edges"]:
    dict_starship[dict["node"]["id"]] = dict["node"]["name"]

dict_person["homeworld"] = dict_homeworld
dict_person["filmConnection"] = dict_pelicula
dict_person["starshipConnection"] = dict_starship

print(dict_person)

#
# data["data"]["film"]["starshipConnection"] = dict_starship
# data["data"]["film"]["characterConnection"] = dict_character
# data["data"]["film"]["planetConnection"] = dict_planet
