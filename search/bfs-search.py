from index import tree


def bfs_search(tree, start, goal):
    from collections import deque

    # Initialize the queue with the start node
    queue = deque([start])
    visited = set()  # To keep track of visited nodes

    while queue:
        current_node = queue.popleft()  # Get the first node in the queue

        if current_node == goal:
            return True  # Goal found

        if current_node not in visited:
            visited.add(current_node)  # Mark the current node as visited
            print(current_node)
            # Add all children of the current node to the queue
            for child in tree.get(current_node, []):
                queue.append(child)

    return False  # Goal not found
# Example usage

if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'K'
    found = bfs_search(tree, start_node, goal_node)
    print(f"Goal node '{goal_node}' found: {found}")
# Example usage
# If you want to test with a different goal node, you can change the goal_node variable
    goal_node = 'M'
    found = bfs_search(tree, start_node, goal_node)
    print(f"Goal node '{goal_node}' found: {found}")
# Example usage
    goal_node = 'Z'  # A node that does not exist in the tree
    found = bfs_search(tree, start_node, goal_node)
    print(f"Goal node '{goal_node}' found: {found}")
# Example usage