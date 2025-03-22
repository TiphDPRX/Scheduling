"""
Lecture et parsing des fichiers de contraintes

This module provides functionality to read and parse constraint files.

Functions:
    

Classes:
    
"""
import os

class Task:
    def __init__(self, id, duration, predecessors=None):
        self.id = id
        self.duration = duration
        self.predecessors = predecessors or []

    def __repr__(self):
        return f"Task(id={self.id}, duration={self.duration}, predecessors={self.predecessors})"


def parse_constraint_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    tasks = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 1):
        if not line.strip():
            continue  # ignore empty lines

        parts = line.strip().split()
        if len(parts) < 2:
            raise ValueError(f"Line {line_num} is invalid: '{line.strip()}'")

        try:
            task_id = int(parts[0])
            duration = int(parts[1])
            predecessors = list(map(int, parts[2:])) if len(parts) > 2 else []
        except ValueError:
            raise ValueError(f"Line {line_num} has non-integer values: '{line.strip()}'")

        if task_id in tasks:
            raise ValueError(f"Duplicate task ID {task_id} found at line {line_num}")

        tasks[task_id] = Task(task_id, duration, predecessors)

    return tasks


def display_parsed_tasks(tasks: dict):
    print("Parsed Tasks:")
    for task_id in sorted(tasks.keys()):
        print(tasks[task_id])
