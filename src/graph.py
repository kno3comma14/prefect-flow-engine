def calculate_edges_from_deps(dependency_map):
    nodes = dependency_map.keys()
    result = set()
    for n in nodes:
        aux_nodes = dependency_map[n]
        if len(aux_nodes) != 0:
            for aux_n in aux_nodes:
                result.add((aux_n, n))

    return result

def complete_graph_data(graph_map):    
    return {**graph_map, **{'edges': graph_map['dependencies']}}