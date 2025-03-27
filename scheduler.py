"""
Module: Calculs

This module provides functions to perform various calculations related to the scheduling of tasks.

Functions:
    
"""

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

def compute_total_float(total_nodes, earliest, latest):
    float = {i: 0 for i in range(total_nodes)}
    for i in range (total_nodes):
        float[i] = latest[i]-earliest[i]

    print("\n=== Total Floats ===")
    for i in range(total_nodes):
        print(f"Task {i}: float = {float[i]}")


