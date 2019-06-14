from django.shortcuts import render, redirect ,render_to_response
import requests


def run_query(query):
    request = requests.post('https://swapi-graphql-integracion-t3.herokuapp.com/', json={'query': str(query)})
    return request.json()




# Create your views here.

### vista principal
def index(request):
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
    data = run_query(query)
    lista_peliculas = [pelicula["node"] for pelicula in data["data"]["allFilms"]["edges"]]
    lista_dicts_peliculas = []
    for pel in lista_peliculas:
        pelicula_dict = {"title": pel['title'],"year": pel["releaseDate"][:4], "director": pel["director"],
         "productor": pel["producers"], "episodio": pel['episodeID'],"id":str(pel["id"])
        }
        lista_dicts_peliculas.append(pelicula_dict)
    html_dict = {'peliculas': lista_dicts_peliculas}
    return render_to_response('index.html', html_dict)

### vista al clickear el titulo de una pelicula
#obtener la data a mostrar de la api
def get_data_film(query):
    data = run_query(query) # Execute the query
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

    dict_pelicula["starshipConnection"] = dict_starship
    dict_pelicula["characterConnection"] = dict_character
    dict_pelicula["planetConnection"] = dict_planet
    return dict_pelicula

#vista pelicula
def films(request,id):
    nquery = """
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
    query = nquery.replace("ID_PELICULA",str(id))
    data = get_data_film(query)
    html_dict = {'Peliculas': data}
    return render_to_response('films.html', html_dict)


### vista al clickear el nombre de un personaje
#obtener la data a mostrar de la api
def get_data_person(query):
    data = run_query(query) # Execute the query
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
    return dict_person

#vista del personaje
def characters(request,id):
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
    query = nquery.replace("ID_PERSONAJE",str(id))
    data = get_data_person(query)
    html_dict = {'Personajes': data}
    return render_to_response('characters.html', html_dict)



### vista al clickear el nombre de un planeta
#obtener la data a mostrar desde la api
def get_data_planet(query):
    data = run_query(query) # Execute the query
    dict_planet = data["data"]["planet"]

    dict_persona = {}
    for dict in dict_planet["residentConnection"]["edges"]:
        dict_persona[dict["node"]["id"]] = dict["node"]["name"]

    dict_pelicula = {}
    for dict in dict_planet["filmConnection"]["edges"]:
        dict_pelicula[dict["node"]["id"]] = dict["node"]["title"]


    dict_planet["residentConnection"] = dict_persona
    dict_planet["filmConnection"] = dict_pelicula

    return dict_planet

#vista del planeta
def planets(request,id):
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
    query = nquery.replace("ID_PLANETA",str(id))
    data = get_data_planet(query)
    html_dict = {'Planetas': data}
    return render_to_response('planets.html', html_dict)




### vista al clickear el nombre de una nave
#obtener la data a  dede la api
def get_data_starship(query):
    data = run_query(query) # Execute the query
    dict_starship = data["data"]["starship"]

    dict_pilotos = {}
    for dict in dict_starship["pilotConnection"]["edges"]:
        dict_pilotos[dict["node"]["id"]] = dict["node"]["name"]

    dict_pelicula = {}
    for dict in dict_starship["filmConnection"]["edges"]:
        dict_pelicula[dict["node"]["id"]] = dict["node"]["title"]


    dict_starship["pilotConnection"] = dict_pilotos
    dict_starship["filmConnection"] = dict_pelicula

    return dict_starship

#Vista de la nave
def starships(request,id):
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
    query = nquery.replace("ID_NAVE",str(id))
    data = get_data_starship(query)
    html_dict = {'Naves': data}
    return render_to_response('starships.html', html_dict)





























###############################################################
# def characters(request):
#     url = request.GET.get('url')
#     type = request.GET.get('type')
#
#     serialized_data = requests.get(url).content
#     data = json.loads(serialized_data)
#
#     if type == "character":
#         films_name_id_list = search_name_id('https://swapi.co/api/films/')
#         starships_name_id_list = search_name_id('https://swapi.co/api/starships/')
#
#         films_names = change_list(data["films"], films_name_id_list)
#         starships_names = change_list(data["starships"], starships_name_id_list)
#
#         url = data["homeworld"]
#         serialized_data = requests.get(url).content
#         data2 = json.loads(serialized_data)
#
#
#         data["homeworld"] = {"name": data2["name"], "url": data2["url"]}
#         data["starships"] = starships_names
#         data["films"] = films_names
#
#         data.update({"type" : "character"})
#
#     elif type == "planet":
#         films_name_id_list = search_name_id('https://swapi.co/api/films/')
#         residents_name_id_list = search_name_id('https://swapi.co/api/people/')
#
#         films_names = change_list(data["films"], films_name_id_list)
#         residents_names = change_list(data["residents"], residents_name_id_list)
#
#         data["residents"] = residents_names
#         data["films"] = films_names
#         data.update({"type" : "planet"})
#
#     elif type == "starship":
#         films_name_id_list = search_name_id('https://swapi.co/api/films/')
#         pilots_name_id_list = search_name_id('https://swapi.co/api/people/')
#
#         pilots_names = change_list(data["pilots"], pilots_name_id_list)
#         films_names = change_list(data["films"], films_name_id_list)
#
#         data["pilots"] = pilots_names
#         data["films"] = films_names
#
#         data.update({"type" : "starship"})
#
#     dict = {'hola': data}
#     return render_to_response('characters.html', dict)
#

# def planets(request):
#     url = request.GET.get('url')
#     type = request.GET.get('type')
#
#     serialized_data = requests.get(url).content
#     data = json.loads(serialized_data)
#
#     if type == "character":
#         films_name_id_list = search_name_id('https://swapi.co/api/films/')
#         starships_name_id_list = search_name_id('https://swapi.co/api/starships/')
#
#         films_names = change_list(data["films"], films_name_id_list)
#         starships_names = change_list(data["starships"], starships_name_id_list)
#
#         url = data["homeworld"]
#         serialized_data = requests.get(url).content
#         data2 = json.loads(serialized_data)
#
#
#         data["homeworld"] = {"name": data2["name"], "url": data2["url"]}
#         data["starships"] = starships_names
#         data["films"] = films_names
#
#         data.update({"type" : "character"})
#
#     elif type == "planet":
#         films_name_id_list = search_name_id('https://swapi.co/api/films/')
#         residents_name_id_list = search_name_id('https://swapi.co/api/people/')
#
#         films_names = change_list(data["films"], films_name_id_list)
#         residents_names = change_list(data["residents"], residents_name_id_list)
#
#         data["residents"] = residents_names
#         data["films"] = films_names
#         data.update({"type" : "planet"})
#
#     elif type == "starship":
#         films_name_id_list = search_name_id('https://swapi.co/api/films/')
#         pilots_name_id_list = search_name_id('https://swapi.co/api/people/')
#
#         pilots_names = change_list(data["pilots"], pilots_name_id_list)
#         films_names = change_list(data["films"], films_name_id_list)
#
#         data["pilots"] = pilots_names
#         data["films"] = films_names
#
#         data.update({"type" : "starship"})
#
#     dict = {'hola': data}
#     return render_to_response('characters.html', dict)


# def starships(request):
    url = request.GET.get('url')
    type = request.GET.get('type')

    serialized_data = requests.get(url).content
    data = json.loads(serialized_data)

    if type == "character":
        films_name_id_list = search_name_id('https://swapi.co/api/films/')
        starships_name_id_list = search_name_id('https://swapi.co/api/starships/')

        films_names = change_list(data["films"], films_name_id_list)
        starships_names = change_list(data["starships"], starships_name_id_list)

        url = data["homeworld"]
        serialized_data = requests.get(url).content
        data2 = json.loads(serialized_data)


        data["homeworld"] = {"name": data2["name"], "url": data2["url"]}
        data["starships"] = starships_names
        data["films"] = films_names

        data.update({"type" : "character"})

    elif type == "planet":
        films_name_id_list = search_name_id('https://swapi.co/api/films/')
        residents_name_id_list = search_name_id('https://swapi.co/api/people/')

        films_names = change_list(data["films"], films_name_id_list)
        residents_names = change_list(data["residents"], residents_name_id_list)

        data["residents"] = residents_names
        data["films"] = films_names
        data.update({"type" : "planet"})

    elif type == "starship":
        films_name_id_list = search_name_id('https://swapi.co/api/films/')
        pilots_name_id_list = search_name_id('https://swapi.co/api/people/')

        pilots_names = change_list(data["pilots"], pilots_name_id_list)
        films_names = change_list(data["films"], films_name_id_list)

        data["pilots"] = pilots_names
        data["films"] = films_names

        data.update({"type" : "starship"})

    dict = {'hola': data}
    return render_to_response('characters.html', dict)
