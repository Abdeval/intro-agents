from index import tree

def a_star_search(tree, start, goal):
    from queue import PriorityQueue
    
    # Initialize the priority queue with the start node
    open_set = PriorityQueue()
    open_set.put((0, start))  # (priority, node)
    came_from = {}  # To reconstruct the path
    g_score = {start: 0}  # Cost from start to the current node
    f_score = {start: heuristic(start, goal)}  # Estimated cost from start to goal
    visited = set()  # To keep track of visited nodes
    while not open_set.empty():
        current_priority, current_node = open_set.get()

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        if current_node not in visited:
            visited.add(current_node)
            print(current_node)

            for neighbor in tree.get(current_node, []):
                tentative_g_score = g_score[current_node] + 1  # Assuming uniform cost for edges

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    open_set.put((f_score[neighbor], neighbor))
    return None  # Goal not found

def heuristic(node, goal):
    # A simple heuristic function that returns 0 for all nodes
    # In a real scenario, this should be a meaningful estimate of the cost to reach the goal
    return 0

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()  # Reverse the path to get it from start to goal
    return total_path

if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'K'
    path = a_star_search(tree, start_node, goal_node)
    if path:
        print(f"Path from '{start_node}' to '{goal_node}': {' -> '.join(path)}")
    else:
        print(f"Goal node '{goal_node}' not found.")
        