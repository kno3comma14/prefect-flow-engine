def calculate_edges_from_deps(dependency_map):
    nodes = dependency_map.keys()
    result = set()
    for n in nodes:
        aux_nodes = dependency_map[n]
        if len(aux_nodes) != 0:
            for aux_n in aux_nodes:
                result.add((aux_n, n))

    return result

def generate_belonging_order(belonging_map):
    result = {}
    node_list = belonging_map.keys()
    for node in node_list:
        result[node] = len(belonging_map[node])
    return sorted(result.items(), key=lambda x: x[1])

def generate_dependency_order(dependency_map, belonging_order):
    for i in range(len(belonging_order)):
        aux_node = belonging_order[i][0]
        for j in range(i + 1, len(belonging_order) - 1):
            pivote_node = belonging_order[j][0]
            if pivote_node in dependency_map[aux_node]:
                aux = belonging_order[i]
                belonging_order[i] = belonging_order[j]
                belonging_order[j] = aux

    return list(map(lambda x: x[0], belonging_order))


def calculate_definition_order(dependency_map, belonging_map):
    belonging_order = generate_belonging_order(belonging_map)
    return generate_dependency_order(dependency_map, belonging_order)    

def complete_graph_data(graph_map):    
    return {**graph_map, **{'edges': graph_map['dependencies']}}