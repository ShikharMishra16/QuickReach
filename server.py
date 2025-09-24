import sys
from flask_cors import CORS
from collections import defaultdict
from heapq import heappush, heappop
from flask import Flask, jsonify
allowed_origins = [
    "http://localhost:5173",                 
    "https://quickreachdeploy.vercel.app"    
]

app = Flask(__name__, static_folder='viteclient/build', static_url_path='')
cors = CORS(app, origin=allowed_origins)

# Node number → location name (FILL THESE MANUALLY)
node_names = {
    1: "IITG Main Gate", 
    2: "Market Complex Junc.", 
    3: "D Type Entrance", 
    4: "Serpentine Lake", 
    5: "F Type Junc.", 
    6: "New Guesthouse", 
    7: "Hospital Bus Stop", 
    8: "IITG Hospital", 
    9: "Turn Between IITG Hospital And Married Scholar Hostel",  
    10: "Bridge infront Of Married Scholar's Hostel",
    11: "Married Scholar hostel", 
    12: "Dhansiri Hostel", 
    13: "New Sac", 
    14: "Swimming Pool/Athletics Field", 
    15: "Sac-Gym Junction", 
    16: "Bridge to Kameng/Gaurang", 
    17: "Kameng Hostel", 
    18: "Manas Hostel", 
    19: "Bridge to Umiam/Barak", 
    20: "Barak/Umiam Hostel",
    21: "Domino's/Brahmaputra Hostel Junction", 
    22: "Khoka Gate", 
    23: "Domino's", 
    24: "Dihing Hostel", 
    25: "Turn to Brahmaputra Hostel Entrance", 
    26: "Brahmaputra Hostel Gate", 
    27: "Dibang/Kapili Main Gate", 
    28: "T-point Ahead Of Kapili/Dibang", 
    29: "Kapili Bus Stand", 
    30: "Turn To Siang Hostel Maingate",
    31: "Siang Main Gate", 
    32: "Old-Sac-Tennis Court Junction", 
    33: "Old Sac", 
    34: "Tennis Court", 
    35: "Subansiri Bus Stand", 
    36: "Subansiri Hostel", 
    37: "Old GuestHouse Bus Stand", 
    38: "Conference Hall/D Type Junction", 
    39: "ViewPoint Entrance", 
    40: "Auditorium",
    41: "Admin Building", 
    42: "Junction Near CCC/Cycle Shop", 
    43: "Junction Near Cycle Shop/Tapri", 
    44: "Library/CCC", 
    45: "ATMs/Souvenier Shops", 
    46: "Lecture Halls", 
    47: "Core 1 Front", 
    48: "Start of Outside Road Around Core 1-4", 
    49: "Core 1/Mech Hill Junction", 
    50: "Mechanical Workshop",
    51: "Classroom Complex", 
    52: "Core 2/ Core 3 Junction(Core 5 side)", 
    53: "Core 2", 
    54: "Core 3", 
    55: "Hashtag Cafe", 
    56: "Earthquake Resistant Building", 
    57: "Core 4/KV gate Junction", 
    58: "Core 4 Parking(Dept. Of Civil Engg.)", 
    59: "Core 4", 
    60: "Core 4 Parking(Dept. of Physics)",
    61: "Core 4 Extension ", 
    62: "Turn to Research Building", 
    63: "Library/CCC Junction", 
    64: "KV Gate", 
    65: ""  
}

@app.route('/')
def hello_world():
    return 'Landing!'

@app.route('/shortd/<int:a>/<int:b>')
def shortestPath(a, b):
    src, dst = a, b

    # Graph definition
    graph = {
        1: {2: 262},
        2: {1: 262, 3: 330, 39: 262},
        3: {2: 330, 4: 130},
        4: {5: 200, 3: 130},
        5: {4: 200, 6: 66, 37: 157},
        6: {5: 66, 7: 131},
        7: {6: 131, 8: 66, 37: 260},
        8: {7: 66, 9: 131},
        9: {8: 131, 10: 66},
        10: {9: 66, 11: 66},
        11: {10: 66, 12: 150},
        12: {11: 150, 13: 130},
        13: {12: 130, 14: 100},
        14: {13: 100, 15: 66},
        15: {14: 66, 32: 250, 16: 140},
        16: {15: 140, 17: 200, 18: 240},
        17: {16: 200},
        18: {16: 240, 19: 52},
        19: {18: 52, 20: 175, 21: 132},
        20: {19: 175},
        21: {19: 132, 23: 60, 22: 66},
        22: {21: 66, 64: 716},
        23: {21: 60, 24: 105, 25: 200},
        24: {23: 105},
        25: {23: 200, 26: 130, 27: 160},
        26: {25: 130},
        27: {25: 160, 28: 130},
        28: {29: 200, 64: 460, 27: 130},
        29: {28: 200, 30: 20, 43: 170},
        30: {29: 20, 31: 131, 32: 200},
        31: {30: 131},
        32: {33: 109, 15: 250, 35: 130, 30: 200},
        33: {34: 60},
        34: {33: 60},
        35: {32: 130, 36: 130, 40: 130, 38: 262},
        36: {35: 130, 37: 400},
        38: {35: 262, 39: 330, 49: 380},
        39: {38: 330, 2: 262},
        40: {35: 130, 41: 80, 42: 79},
        41: {40: 80, 45: 20},
        42: {40: 79, 44: 53, 43: 92},
        43: {42: 92, 63: 105, 29: 170},
        44: {42: 53, 45: 50},
        45: {46: 105, 44: 50, 41: 20},
        46: {45: 105, 47: 100},
        47: {48: 120, 49: 100, 46: 100},
        48: {47: 120, 63: 66, 55: 250},
        49: {38: 380, 50: 91, 47: 100},
        50: {49: 91, 52: 182},
        51: {52: 40},
        52: {53: 130, 54: 130, 51: 40, 62: 200},
        53: {52: 130, 54: 20, 55: 130},
        54: {53: 20, 52: 130, 55: 130},
        55: {48: 250, 56: 122, 53: 130, 54: 130},
        56: {55: 122, 57: 115},
        57: {56: 115, 58: 130, 64: 250},
        58: {57: 130, 59: 66, 60: 66},
        59: {58: 66, 60: 66},
        60: {58: 66, 61: 66},
        61: {60: 50, 62: 30},
        62: {52: 200, 61: 30},
        63: {48: 66, 43: 105},
        64: {57: 250, 28: 460, 22: 716}
    }

    # Build adjacency list
    g = defaultdict(list)
    for u in graph:
        for v, wt in graph[u].items():
            g[u].append([v, wt])
            g[v].append([u, wt])

    inf = float('inf')
    n = 65
    distance = [inf] * (n + 1)
    distance[src] = 0
    path = [-1] * (n + 1)

    pq = []
    heappush(pq, [0, src])

    while pq:
        dis, node = heappop(pq)
        if dis > distance[node]:
            continue
        for neigh, cost in g[node]:
            if dis + cost < distance[neigh]:
                path[neigh] = node
                distance[neigh] = dis + cost
                heappush(pq, [distance[neigh], neigh])

    if distance[dst] == inf:
        return jsonify({"error": "No path found"})

    # Reconstruct path
    current = dst
    path_nodes = []
    while current > 0:
        path_nodes.append(current)
        current = path[current]
    path_nodes.reverse()

    # Build result with names
    result = {
        "from": node_names.get(src, f"Node {src}"),
        "to": node_names.get(dst, f"Node {dst}"),
        "path": [node_names.get(n, f"Node {n}") for n in path_nodes],
        "totalDis": distance[dst]
    }
    return jsonify(result)

#if __name__ == "__main__":
 #   app.run(debug=True)
