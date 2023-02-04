import json
from insert_into_tables import insert_into_Roles
from embedding import create_embedding


def post_create_role(json_input):
    dict_input = json.loads(json_input)

    description = dict_input["description"]

    values_list = dict_input.values()

    values_list.append("")  # list_people_interested_in_role
    values_list.append(create_embedding(description))

    return tuple(values_list)