"""
Module: Calculs

This module provides functions to perform various calculations related to the scheduling of tasks.

Functions:
    
"""

from time import *
from graph import *
from collections import deque

def compute_ranks(matrix, total_nodes, index_to_id):

    # Initialize ranks and queue
    ranks = {i: None for i in range(total_nodes)}
    ranks[0] = 0  # Start node rank is 0
    queue = deque([0])  # Start BFS from vertex 0

    print("\n=== Computing Ranks (Shortest Path in Edges from Vertex 0) ===")
    print("Method: Breadth-First Search (BFS)\n")

    # BFS to compute ranks
    while queue:
        current = queue.popleft()
        current_rank = ranks[current]
        print(f"Processing vertex {current} (Rank = {current_rank}):")

        # Check all possible neighbors
        print("Checking neighbors...")
        for j in range(total_nodes):
            if matrix[current][j] != '*':  # There is an edge from current to j
                if ranks[j] is None:  # If rank not yet set
                    sleep(0.5)
                    ranks[j] = current_rank + 1
                    queue.append(j)
                    print(f"  Set rank of vertex {j} to {ranks[j]} (from vertex {current})")
                else:
                    print(f"  Vertex {j} already has rank {ranks[j]}, no update needed")

        print("")  # Blank line for readability

    # Display final ranks
    print("=== Final Ranks ===")
    for i in range(total_nodes):
        sleep(0.3)
        if i == 0:
            label = "Start"
        elif i == total_nodes - 1:
            label = "End"
        else:
            label = f"Task {index_to_id[i]}"
        print(f"Vertex {i} ({label}): Rank = {ranks[i]}")

    return ranks


def compute_earliest_dates(matrix, total_nodes):
    earliest = {i: 0 for i in range(total_nodes)}  # Start with 0 for all tasks
    #exemple avec 5 tâches : earliest = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for i in range(total_nodes): #go through each task
        for j in range(total_nodes): #and its predecessors
            if matrix[i][j] != '*':
                earliest[j] = max(earliest[j], earliest[i] + matrix[i][j]) #add the earliest_date of the predecessors and its own duration


    print("\n=== Earliest Start Times ===")
    for i in range(total_nodes):
        print(f"Task {i}: Earliest start = {earliest[i]}")

    return earliest

"""
def compute_latest_dates(matrix, total_nodes, earliest):
    #initialize everything to infinity except the final task
    latest = {i: float('inf') for i in range(total_nodes)}
    latest[total_nodes - 1] = earliest[total_nodes - 1]  # Last node constraint

    for i in range(total_nodes - 1, -1, -1):  # Traverse in reverse order
        for j in range(total_nodes):
            if matrix[i][j] != '*':  # If there is an edge from i to j
                latest[i] = min(latest[i], latest[j] - matrix[i][j])

    print("\n=== Latest Start Times ===")
    for i in range(total_nodes):
        print(f"Task {i}: Latest start = {latest[i]}")

    return latest
    """



def compute_latest_dates(matrix, total_nodes, earliest, ranks):
    latest = {i: earliest[total_nodes - 1] for i in range(total_nodes)}  # Initialiser avec la latest date finale

    # On traite les sommets en ordre décroissant de rang
    sorted_nodes = sorted(range(total_nodes), key=lambda x: -ranks[x])  # Trier selon le rang décroissant

    print("\n=== Computing Latest Start Times (Using Ranks) ===\n")

    for i in sorted_nodes:
        print(f"Processing vertex {i} (Rank = {ranks[i]}):")

        for j in range(total_nodes):
            if matrix[i][j] != '*':  # Il y a une connexion entre i et j
                latest[i] = min(latest[i], latest[j] - matrix[i][j])
                print(f"  Updated latest[{i}] = {latest[i]} (from vertex {j})")

        print("")  # Ajout d'une ligne vide pour la lisibilité

    print("\n=== Latest Start Times ===")
    for i in range(total_nodes):
        print(f"Task {i}: Latest start = {latest[i]}")

    return latest


def compute_total_float(total_nodes, earliest, latest):
    float = {i: 0 for i in range(total_nodes)}
    for i in range (total_nodes):
        float[i] = latest[i]-earliest[i]

    print("\n=== Total Floats ===")
    for i in range(total_nodes):
        print(f"Task {i}: float = {float[i]}")


