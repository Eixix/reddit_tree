import networkx as nx
import json

G = nx.Graph()

json_data = {}

with open('reddit.json') as f:
    json_data = json.load(f)

all_subreddit_names = [x['name'] for x in json_data]
sigma_data = {'nodes': [], 'edges': []}

G.add_nodes_from(all_subreddit_names)

for subreddit in json_data:
    for child in subreddit['children']:
        if child in all_subreddit_names:
            G.add_edge(subreddit['name'], child)


nx.write_gexf(G, "reddit.gexf")
