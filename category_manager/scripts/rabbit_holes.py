import requests


def get_all_similarity_records():
    # Get all similarities
    response = requests.get(
        'http://127.0.0.1:8000/api/getallsimilarities/',
        headers={"Content-Type": "application/json"}
    )

    return response.json()


def build_graph(data):
    graph = {}
    for item in data:
        category_a = item['category_a_name']
        category_b = item['category_b_name']
        if category_a not in graph:
            graph[category_a] = []
        if category_b not in graph:
            graph[category_b] = []
        graph[category_a].append(category_b)
        graph[category_b].append(category_a)
    return graph


def print_graph(graph):
    # Print the adjacency list
    print("Graph Representation:")
    for key, value in graph.items():
        print(f"{key}:")
        for v in value:
            print(f"  -> {v}")


def find_rabbit_islands(graph):
    def bfs(start_node):
        queue = [start_node]
        visited = set([start_node])
        island = []
        while queue:
            node = queue.pop(0)
            island.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return island

    visited = set()
    islands = []
    for node in graph:
        if node not in visited:
            island = bfs(node)
            islands.append(island)
            visited.update(island)
    return islands


def find_rabbit_hole(graph, start, end):
    if start not in graph or end not in graph:
        return None  # If start or end category does not exist

    queue = [(start, [start])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        if current == end:
            return path
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                visited.add(neighbor)
    return None  # If no path is found


if __name__ == "__main__":

    data = get_all_similarity_records()
    graph = build_graph(data)
    print_graph(graph)

    # Define start and end categories
    start_category = 'A'
    end_category = 'C'

    # Find the rabbit hole (shortest path) between start and end categories
    rabbit_hole = find_rabbit_hole(graph, start_category, end_category)
    if rabbit_hole:
        print("Rabbit Hole from {} to {}: {}".format(start_category, end_category, " -> ".join(rabbit_hole)))
    else:
        print("No rabbit hole found from {} to {}".format(start_category, end_category))


    # Find rabbit islands
    rabbit_islands = find_rabbit_islands(graph)
    print("Rabbit Islands:")
    for island in rabbit_islands:
        print(", ".join(island))
