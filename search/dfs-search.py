from index import tree

def dfs_search(tree, start, goal):
    # Initialize the stack with the start node
    stack = [start]
    visited = set()
    
    while stack: 
        current_node = stack.pop()
        if current_node == goal:
            return True
        
        if current_node not in visited:
            visited.add(current_node)
            print(current_node)
            # Add all children of the current node to the stack
            for child in tree.get(current_node, []):
                stack.append(child)
        
    return False
    
    
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'K'
    found = dfs_search(tree, start_node, goal_node)
    print(f"Goal node '{goal_node} found: {found}")
    