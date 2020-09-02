import json

"""
This Python implementation is hypothesized to be very inefficient and 
impractical! Feel free to suggest a much simpler implementation.
"""


# Our scientist info is stored in this format:
scientists = {
    "e3d46de8c7194cb1a32275195c15dc07": {
        "id": "e3d46de8c7194cb1a32275195c15dc07",
        "name": "Niels Bohr",
        "specialization": "Quantum Mechanics",
        "known_for": ["Wave/Particle Duality", "Uncertainty"],
    },
    "7064c3f9c99743b2838bbd8eacafe0d6": {
        "id": "7064c3f9c99743b2838bbd8eacafe0d6",
        "name": "Max Planck",
        "known_for": "Planck's constant",
    },
    "b19e575a0d3f4151a1391452d8a47a44": {
        "id": "b19e575a0d3f4151a1391452d8a47a44",
        "name": "Jane Goodall",
        "specialization": "Apes",
    },
    "17d9d0908f454253b5337e8c1ef4b564": {
        "id": "17d9d0908f454253b5337e8c1ef4b564",
        "name": "Caroline Herschel",
        "specialization": "Stars",
    },
}


def get_scientist_info(id):
    for scientist_id, scientist_info in scientists.items():
        if scientist_info["id"] == id:
            return scientist_info
        else:
            pass
# 1. Given a scientist's `id`, a function that returns a JSON serialization
#    of the information we have on that particular scientist.


def json_stringify_scientist_info(id):
    scientist_json_template = """{
    'id': '%s',
    'name': '%s',
    'specialization': '%s',
    'known_for': '%s',
}"""
    return scientist_json_template % (
        get_scientist_info(id).get("id"),
        get_scientist_info(id).get("name"),
        get_scientist_info(id).get("specialization"),
        get_scientist_info(id).get("known_for"),
    )
# 2. Given an object containing info on multiple scientists, a function
#    that dumps a JSON serialization of that information.


def json_stringify_scientists_info(scientists):
    d = {}
    data = {}

    d['scientists'] = data

    for scientist_id in scientists.keys():
        data[scientist_id] = get_scientist_info(scientist_id)

    return json.dumps(d, indent=4)
