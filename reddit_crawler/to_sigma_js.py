import json
from random import randrange

json_data = {}

with open('reddit.json') as f:
    json_data = json.load(f)

sigma_data = {'nodes': [], 'edges': []}

for subreddit in json_data:
    sigma_data['nodes'].append(
        {"id": subreddit['name'], "label": subreddit['name'], "subscribers": subreddit['subscribers']})

    for child in subreddit['children']:
        sigma_data['edges'].append(
            {'source': subreddit['name'], 'target': child})


with open('../reddit_graph/public/reddit_sigma.json', 'w') as f:
    json.dump(sigma_data, f, indent=4)
