
# por cada query obtenida en el index remplazar el id y obtener toda la informacion
query = """
{
  film(id: "ID_PELICULA") {
    title
    episodeID
    openingCrawl
    director
    producers
    releaseDate
    starshipConnection {
      edges {
        node {
          id
          name
        }
      }
    }
    characterConnection{
      edges{
        node{
          id
          name
        }
      }
    }
    planetConnection {
      edges {
        node {
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
    "film": {
      "title": "A New Hope",
      "episodeID": 4,
      "openingCrawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
      "director": "George Lucas",
      "producers": [
        "Gary Kurtz",
        "Rick McCallum"
      ],
      "releaseDate": "1977-05-25",
      "starshipConnection": {
        "edges": [
          {
            "node": {
              "id": "c3RhcnNoaXBzOjI=",
              "name": "CR90 corvette"
            }
          },
          {
            "node": {
              "id": "c3RhcnNoaXBzOjM=",
              "name": "Star Destroyer"
            }
          },
          {
            "node": {
              "id": "c3RhcnNoaXBzOjU=",
              "name": "Sentinel-class landing craft"
            }
          },
          {
            "node": {
              "id": "c3RhcnNoaXBzOjk=",
              "name": "Death Star"
            }
          },
          {
            "node": {
              "id": "c3RhcnNoaXBzOjEw",
              "name": "Millennium Falcon"
            }
          },
          {
            "node": {
              "id": "c3RhcnNoaXBzOjEx",
              "name": "Y-wing"
            }
          },
          {
            "node": {
              "id": "c3RhcnNoaXBzOjEy",
              "name": "X-wing"
            }
          },
          {
            "node": {
              "id": "c3RhcnNoaXBzOjEz",
              "name": "TIE Advanced x1"
            }
          }
        ]
      },
      "characterConnection": {
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
              "id": "cGVvcGxlOjM=",
              "name": "R2-D2"
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
              "id": "cGVvcGxlOjU=",
              "name": "Leia Organa"
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
              "id": "cGVvcGxlOjEw",
              "name": "Obi-Wan Kenobi"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjEy",
              "name": "Wilhuff Tarkin"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjEz",
              "name": "Chewbacca"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjE0",
              "name": "Han Solo"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjE1",
              "name": "Greedo"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjE2",
              "name": "Jabba Desilijic Tiure"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjE4",
              "name": "Wedge Antilles"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjE5",
              "name": "Jek Tono Porkins"
            }
          },
          {
            "node": {
              "id": "cGVvcGxlOjgx",
              "name": "Raymus Antilles"
            }
          }
        ]
      },
      "planetConnection": {
        "edges": [
          {
            "node": {
              "id": "cGxhbmV0czox",
              "name": "Tatooine"
            }
          },
          {
            "node": {
              "id": "cGxhbmV0czoy",
              "name": "Alderaan"
            }
          },
          {
            "node": {
              "id": "cGxhbmV0czoz",
              "name": "Yavin IV"
            }
          }
        ]
      },
      "created": "2014-12-10T14:23:31.880000Z",
      "edited": "2015-04-11T09:46:52.774897Z",
      "id": "ZmlsbXM6MQ=="
    }
  }
}
# nquery = query.replace("ID_PELICULA","ZmlsbXM6MQ==")
# print(nquery)
dict_pelicula = data["data"]["film"]

dict_starship = {}
for dict in dict_pelicula["starshipConnection"]["edges"]:
    dict_starship[dict["node"]["id"]] = dict["node"]["name"]

dict_character = {}
for dict in dict_pelicula["characterConnection"]["edges"]:
    dict_character[dict["node"]["id"]] = dict["node"]["name"]

dict_planet = {}
for dict in dict_pelicula["planetConnection"]["edges"]:
    dict_planet[dict["node"]["id"]] = dict["node"]["name"]

data["data"]["film"]["starshipConnection"] = dict_starship
data["data"]["film"]["characterConnection"] = dict_character
data["data"]["film"]["planetConnection"] = dict_planet
