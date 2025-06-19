#!/usr/bin/python3
"""
Script to fetch and display employee TODO list progress from JSONPlaceholder API.
Usage: python3 0-gather_data_from_an_API.py <employee_id>
"""

import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetch and display employee TODO list progress.
    
    Args:
        employee_id (int): The ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        # Get employee information
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name', 'Unknown')
        
        # Get employee's TODO list
        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = [todo for todo in todos_data if todo.get('completed', False)]
        num_completed = len(completed_tasks)
        
        # Display progress summary
        print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
        
        # Display completed task titles
        for task in completed_tasks:
            title = task.get('title', '')
            print(f"\t {title}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error processing data: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>", file=sys.stderr)
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer", file=sys.stderr)
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)
