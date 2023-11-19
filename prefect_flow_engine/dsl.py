import json
import graph
from importlib_resources import files


def read_json_file(path):
    f = open(path)
    raw_data = f.read()
    json_data = json.loads(raw_data)
    f.close()

    return json_data


def resolve_single_flow_dependency(f1, f2):
    dependency_container = []
    if f1 in f2["dependencies"]:
        dependency_container = [f1["name"], f2["name"]]

    return dependency_container


def verify_flow_concurrency(parent_flow, child_flow1, child_flow2):
    return all(
        [
            child_flow1 in parent_flow["belonging"],
            child_flow2 in parent_flow["belonging"],
            not resolve_single_flow_dependency(child_flow1, child_flow2),
            not resolve_single_flow_dependency(child_flow2, child_flow1),
        ])



if __name__ == "__main__":
    sample_path = files('resources').joinpath('sample.json')
    data = read_json_file(sample_path)
    print(graph.calculate_definition_order(data['flows']['dependencies'], data['flows']['belonging']))
