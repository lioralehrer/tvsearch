from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143", "175", "216", "1371", "1871","2993", "305"]

def getVersion():
    return "0.0.1"

def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"

def getShowsData():
    shows = []
    for show in AVAILABE_SHOWS:
        shows.append(json.loads(getJsonFromFile(show)))
    return shows

def search(search):
    shows = getShowsData()
    list = []
    for show in shows:
        for episode in show['_embedded']['episodes']:
            if str(episode['name']).lower().find(search.lower()) > -1:
                element = {'showid': show['id'], 'episodeid': episode['id'], 'text': '{}: {}'.format(
                    show['name'], episode['name'])}
                list.append(element)
    return list