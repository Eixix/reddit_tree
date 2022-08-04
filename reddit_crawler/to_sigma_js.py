import json
from random import randrange

json_data = {}

with open('reddit.json') as f:
    json_data = json.load(f)

sigma_data = {'nodes': [], 'edges': []}
node_names = set()

counter = 0

for subreddit in json_data:
    node_names.add(subreddit['name'])

    for child in subreddit['children']:
        sigma_data['edges'].append({'source': subreddit['name'], 'target': child})
        node_names.add(child)


for node in node_names:
    sigma_data['nodes'].append({'id': node, 'label': node, 'size': 5})


with open('../reddit_graph/public/reddit_sigma.json', 'w') as f:
    json.dump(sigma_data, f, indent=4)
