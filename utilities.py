# Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import networkx as nx

import matplotlib
matplotlib.use("agg")   # select backend
import matplotlib.pyplot as plt


def visualize_map(nodes, edges, sample, node_positions=None):
    # Set up graph
    G = nx.Graph(edges)

    lone_nodes = set(nodes) - set(G.nodes)  # nodes without edges
    for lone_node in lone_nodes:
        G.add_node(lone_node)

    # Grab the colors selected by sample
    color_labels = [k for k, v in sample.items() if v == 1]

    # Get color order to match that of the graph nodes
    for label in color_labels:
        name, color = label.split("_")
        G.nodes[name]["color"] = color
    color_map = [color for name, color in G.nodes(data="color")]

    # Draw graph
    nx.draw_networkx(G, pos=node_positions, with_labels=True,
                     node_color=color_map, font_color="w", node_size=400)

    # Save graph
    filename = "graph.png"
    plt.savefig(filename)
    print("The graph is saved in '{}'.".format(filename))
