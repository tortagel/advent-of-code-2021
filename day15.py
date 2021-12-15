import networkx as nx
import numpy as np

def prepare_puzzle(puzzle):
    return [[int(n) for n in x] for x in puzzle]

def get_lowest_risk(risk_map):
    graph = nx.DiGraph()
    for y in range(len(risk_map)):
        for x in range(len(risk_map[0])):
            if x+1 < len(risk_map[0]):
                graph.add_edge((x, y), (x+1, y), weight=risk_map[y][x+1])
                graph.add_edge((x+1, y), (x, y), weight=risk_map[y][x])
            if y+1 < len(risk_map):
                graph.add_edge((x, y), (x, y+1), weight=risk_map[y+1][x])
                graph.add_edge((x, y+1), (x, y), weight=risk_map[y][x])    
    return nx.shortest_path_length(graph, source=(0, 0), target=(len(risk_map[0])-1, len(risk_map)-1), weight='weight')

def solve_part1(puzzle):
    return get_lowest_risk(puzzle)

def solve_part2(puzzle):
    last_map = extended_map = puzzle
    for _ in range(4):
        last_map = [[1 if n+1 > 9 else n+1 for n in x] for x in last_map]
        extended_map = np.concatenate([extended_map, last_map], axis=1)
    last_map = extended_map
    for _ in range(4):
        last_map = [[1 if n+1 > 9 else n+1 for n in x] for x in last_map]
        extended_map = np.concatenate([extended_map, last_map], axis=0)
    return get_lowest_risk(extended_map)
