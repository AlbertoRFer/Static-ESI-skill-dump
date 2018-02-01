from esipy import App
from esipy import EsiClient
import json

app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")
client = EsiClient(
    retry_requests=True,
    header={'User-Agent': 'DumpSkills'},
    raw_body_only=False,
)

fields = app.op['get_universe_categories_category_id'](
    category_id=16,
)

response = client.request(fields)
groups = response.data['groups']

gral = {}

for group in groups:
    g = app.op['get_universe_groups_group_id'](
        group_id=group
    )
    response = client.request(g)
    group_name = response.data['name']
    skills = response.data['types']
    group_dict = {}

    for skill in skills:
        s = app.op['get_universe_types_type_id'](
            type_id=skill
        )
        response = client.request(s)
        group_dict[skill] = response.data['name']
    gral[group_name] = [{'Category ID': group}, group_dict]

with open("skills.txt", 'w') as f:
    json.dump(gral, fp=f, indent=4, sort_keys=True)



