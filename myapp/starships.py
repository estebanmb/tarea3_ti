nquery = """
{
  starship(id: "ID_NAVE") {
    name
    model
    starshipClass
    manufacturers
    costInCredits
    length
    crew
    passengers
    maxAtmospheringSpeed
    hyperdriveRating
    MGLT
    cargoCapacity
    consumables
    pilotConnection {
      edges {
        node {
          id
          name
        }
      }
    }
    filmConnection{
      edges{
        node{
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
    "starship": {
      "name": "CR90 corvette",
      "model": "CR90 corvette",
      "starshipClass": "corvette",
      "manufacturers": [
        "Corellian Engineering Corporation"
      ],
      "costInCredits": 3500000,
      "length": 150,
      "crew": "165",
      "passengers": "600",
      "maxAtmospheringSpeed": 950,
      "hyperdriveRating": 2,
      "MGLT": 60,
      "cargoCapacity": 3000000,
      "consumables": "1 year",
      "pilotConnection": {
        "edges": []
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
              "id": "ZmlsbXM6Ng==",
              "title": "Revenge of the Sith"
            }
          }
        ]
      },
      "created": "2014-12-10T14:20:33.369000Z",
      "edited": "2014-12-22T17:35:45.408368Z",
      "id": "c3RhcnNoaXBzOjI="
    }
  }
}


query = nquery.replace("ID_NAVE","c3RhcnNoaXBzOjI=")
# print(query)
dict_starship = data["data"]["starship"]

# dict_persons = {dict_planet["residentConnection"]["id"]:dict_planet["homeworld"]["name"]}

dict_pilotos = {}
for dict in dict_starship["pilotConnection"]["edges"]:
    dict_pilotos[dict["node"]["id"]] = dict["node"]["name"]

dict_pelicula = {}
for dict in dict_starship["filmConnection"]["edges"]:
    dict_pelicula[dict["node"]["id"]] = dict["node"]["title"]


dict_starship["pilotConnection"] = dict_pilotos
dict_starship["filmConnection"] = dict_pelicula

print(dict_starship)
