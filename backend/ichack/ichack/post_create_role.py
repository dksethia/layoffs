import json
from .embedding import create_embedding


def post_create_role(json_input):
    print("OK")
    print(json_input)
    dict_input = json.loads(json_input)
    print(dict_input)
    description = dict_input["description"]

    values_list = list(dict_input.values())
    print(values_list)
    values_list.append("")  # list_people_interested_in_role
    values_list.append(create_embedding(description))

    return tuple(values_list)

