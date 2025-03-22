from parser import parse_constraint_file
from graph import *

if __name__ == "__main__":
    filepath = "data/1.txt"
    tasks = parse_constraint_file(filepath)

    matrix, total_nodes, index_to_id = build_graph_matrix(tasks)
    display_matrix(matrix, total_nodes, index_to_id)
    detect_cycle(matrix)