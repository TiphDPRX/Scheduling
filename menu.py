from parser import parse_constraint_file
from graph import *
from time import *

def main_menu():
    constraint_nb = display_menu()
    constraint = "table " + str(constraint_nb)
    filepath = "data/" + str(constraint) + ".txt"
    print("Reading file...")
    sleep(0.5)
    print("Building graph matrix...")
    tasks = parse_constraint_file(filepath)
    sleep(0.5)

    matrix, total_nodes, index_to_id = build_graph_matrix(tasks)
    print("Building graph matrix...")
    sleep(0.5)
    display_matrix(matrix, total_nodes, index_to_id)
    sleep(0.5)
    is_cycle = detect_cycle(matrix)
    sleep(0.5)
    is_negative = negative_weights(matrix)
    if not is_cycle and not is_negative:
        print("No cycle detected and there are no negative weights, this is a scheduling graph.")
        sleep(0.5)



def display_menu():
    print("This is the main menu, please enter the number of the constraint table you want to work with (1-14): ")
    constraint_nb = int(input(""))
    if constraint_nb < 1 or constraint_nb > 14:
        print("Please enter a number between 1 and 14.")
        display_menu()
    return constraint_nb