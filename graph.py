"""
This module provides functionality to build and display a graph matrix for scheduling tasks.
Functions:
    build_graph_matrix(tasks: dict) -> tuple:
        Constructs a graph matrix from a dictionary of tasks.
        Args:
            tasks (dict): A dictionary where keys are task IDs and values are Task objects.
        Returns:
            tuple: A tuple containing the graph matrix, total number of nodes, and a mapping from indices to task IDs.
    display_matrix(matrix, total_nodes, index_to_id):
        Displays the graph matrix in a readable format.
        Args:
            matrix (list): The graph matrix to display.
            total_nodes (int): The total number of nodes in the matrix.
            index_to_id (dict): A mapping from matrix indices to task IDs.

"""

# scheduling_project/graph.py #3

from parser import Task

def build_graph_matrix(tasks: dict):
    task_ids = sorted(tasks.keys())
    n = len(task_ids)

    id_to_index = {task_id: idx + 1 for idx, task_id in enumerate(task_ids)}  # 1-based, index 0 reserved for fictive task 0
    index_to_id = {idx + 1: task_id for idx, task_id in enumerate(task_ids)}

    total_nodes = n + 2  # include fictive start (0) and end (N+1)

    matrix = [['*' for _ in range(total_nodes)] for _ in range(total_nodes)]

    # Add arcs from fictive start (0) to tasks with no predecessors
    for task_id, task in tasks.items():
        if not task.predecessors:
            j = id_to_index[task_id]
            matrix[0][j] = 0  # duration is 0

    # Add arcs from tasks to their successors
    for task_id, task in tasks.items():
        i = id_to_index[task_id]
        for pred in task.predecessors:
            j = id_to_index[task_id]
            pred_idx = id_to_index[pred]
            matrix[pred_idx][j] = tasks[pred].duration

    # Add arcs to fictive end (N+1) from tasks with no successors
    successors = {pred for task in tasks.values() for pred in task.predecessors}
    for task_id in task_ids:
        if task_id not in successors:
            i = id_to_index[task_id]
            matrix[i][total_nodes - 1] = tasks[task_id].duration

    return matrix, total_nodes, index_to_id


# Improved matrix display with perfect alignment

def display_matrix(matrix, total_nodes, index_to_id):
    print("\nValue Matrix:\n")

    col_width = 4

    # Header
    header = " " * (col_width - 1) + "".join(f"{j:>{col_width}}" for j in range(total_nodes))
    print(header)
    print(" " * (col_width - 1) + "-" * (total_nodes * col_width))

    # Rows
    for i in range(total_nodes):
        row = f"{i:>{col_width - 1}}|"
        for j in range(total_nodes):
            val = matrix[i][j]
            if val == '*':
                row += f"{'*':>{col_width}}"
            else:
                row += f"{val:>{col_width}}"
        print(row)

def detect_cycle(matrix):
    n = len(matrix)
    remaining = set(range(n))
    in_degrees = {i: 0 for i in range(n)}

    # Calculate in-degrees
    for j in range(n):
        for i in range(n):
            if matrix[i][j] != '*':
                in_degrees[j] += 1

    print("\n* Detecting a cycle")
    print("* Method: eliminating entry points\n")

    while True:
        # Find vertices with zero in-degree
        entry_points = [v for v in remaining if in_degrees[v] == 0]

        if not entry_points:
            break

        print(f"Entry points: {entry_points}")
        print("Eliminating entry points")

        # Remove vertices and update in-degrees
        for v in entry_points:
            remaining.remove(v)
            for j in range(n):
                if matrix[v][j] != '*':
                    in_degrees[j] -= 1

        print(f"Remaining vertices: {sorted(remaining)}\n")

    if remaining:
        print("⚠️  Cycle detected! Remaining vertices:", sorted(remaining))
        return True
    else:
        print("✅ No cycle detected.")
        return False

def negative_weights(matrix):
    print("\n* Checking for negative weights")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != '*' and matrix[i][j] < 0:
                print("⚠️  Negative weight found at", (i, j))
                return True
    return False