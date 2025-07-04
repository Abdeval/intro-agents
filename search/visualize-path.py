import networkx as nx
import matplotlib.pyplot as plt
from a_star import a_star_search
from index import tree

def visualize_tree_and_path(tree, path=None):
    G = nx.DiGraph()

    # Add all edges in the tree
    for parent, children in tree.items():
        for child in children:
            G.add_edge(parent, child)

    pos = nx.nx_pydot.graphviz_layout(G, prog="dot")  # hierarchical layout

    # Draw all nodes and edges
    nx.draw(G, pos, with_labels=True, arrows=True, node_size=800, node_color="lightblue", font_size=10)

    # If a path was found, highlight it
    if path:
        # Build edges in the path
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="red")

    plt.title("Decision Tree Visualization")
    plt.show()

if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'K'
    path = a_star_search(tree, start_node, goal_node)
    if path:
        print(f"Path from '{start_node}' to '{goal_node}': {' -> '.join(path)}")
    else:
        print(f"Goal node '{goal_node}' not found.")

    # Call visualization with the discovered path
    visualize_tree_and_path(tree, path)
