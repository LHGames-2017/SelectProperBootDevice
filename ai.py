from flask import Flask, request
from structs import *
import json
from numpy import *
from map import *
from cases import *

app = Flask(__name__)

def create_action(action_type, target):
    actionContent = ActionContent(action_type, target.__dict__)
    return json.dumps(actionContent.__dict__)

def create_move_action(target):
    return create_action("MoveAction", target)

def create_attack_action(target):
    return create_action("AttackAction", target)

def create_collect_action(target):
    return create_action("CollectAction", target)

def create_steal_action(target):
    return create_action("StealAction", target)

def create_heal_action():
    return create_action("HealAction", "")

def create_purchase_action(item):
    return create_action("PurchaseAction", item)

def deserialize_map(serialized_map):
    """
    Fonction utilitaire pour comprendre la map
    """
    serialized_map = serialized_map[1:]
    rows = serialized_map.split('[')
    column = rows[0].split('{')
    deserialized_map = [[Tile() for x in range(20)] for y in range(20)]
    for i in range(len(rows) - 1):
        column = rows[i + 1].split('{')

        for j in range(len(column) - 1):
            infos = column[j + 1].split(',')
            end_index = infos[2].find('}')
            content = int(infos[0])
            x = int(infos[1])
            y = int(infos[2][:end_index])
            deserialized_map[i][j] = Tile(content, x, y)

    return deserialized_map

def bot():
    """
    Main de votre bot.
    """
    map_json = request.form["map"]

    # Player info

    encoded_map = map_json.encode()
    map_json = json.loads(encoded_map)
    p = map_json["Player"]
    pos = p["Position"]
    x = pos["X"]
    y = pos["Y"]
    house = p["HouseLocation"]
    point = Point(x,y)
    player = Player(p["Health"], p["MaxHealth"], point,
                    Point(house["X"], house["Y"]),
                    p["CarriedResources"], p["CarryingCapacity"])
    # Map
    serialized_map = map_json["CustomSerializedMap"]

    #map = Map(player.Position, serialized_map)

    deserialized_map = deserialize_map(serialized_map)

    otherPlayers = []

    for players in map_json["OtherPlayers"]:

        player_info = players["Value"]
        p_pos = player_info["Position"]
        player_info = PlayerInfo(player_info["Health"],
                                     player_info["MaxHealth"],
                                     Point(p_pos["X"], p_pos["Y"]))

        otherPlayers.append(player_info)
    # return decision

    ETAT = 'NONDEFINI'

    # Etat initial : maison
    if (point.X == house['X'] and point.Y == house['Y']):
        chemin.append(house['X'], house['Y'])
        ETAT = 'INITIAL'

    if (ETAT == 'INITAL'):
        ETAT = 'RECHERCHE'

    if (ETAT == 'RECHERCHE'):
        for i in range(0, 50):
            for j in range(0, 50):
                if (Map.trouverContent(house['X'] + i, house['Y'] + j, serialized_map) == 4):  # Ressource
                    ETAT = 'DEPLACEMENT'
                    ressourceCoord.__add__(house['X'], house['Y'])

    if (ETAT == 'DEPLACEMENT'):
        if (point.X != ressourceCoord.X):
            chemin.append(Point(point.X, point.Y))
            return create_move_action(Point(0, 1).__add__(point))
        if (point.Y != ressourceCoord.Y):
            return create_move_action((Point(0, 1)).__add__(point))

    return

@app.route("/", methods=["POST"])
def reponse():
    """
    Point d'entree appelle par le GameServer
    """
    return bot()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
