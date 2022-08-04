import json
from random import randrange

json_data = {}

with open('reddit.json') as f:
    json_data = json.load(f)

sigma_data = {'nodes': [], 'edges': []}

counter = 0

for subreddit in json_data:
    sigma_data['nodes'].append({'id': subreddit['name'], 'label': subreddit['name'], 'x': randrange(10), 'y': randrange(10), 'size': 5})
    for child in subreddit:
        sigma_data['edges'].append({'id': counter, 'source': subreddit['name'], 'target': child})
        counter += 1

with open('reddit_sigma.json', 'w') as f:
    json.dump(sigma_data, f, indent=4)
