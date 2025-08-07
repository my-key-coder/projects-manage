import os
import json
from datetime import datetime


task_file = 'task_file.json'

def save_task(tasks):
    """
    Save the list of tasks to the JSON file specified by task_file.
    """
    with open(task_file, 'w') as file:
        json.dump(tasks,file, indent=4)

def load_task():
    """
    Load tasks from the JSON file if it exists, otherwise return an empty list.
    """
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            content = file.read().strip()
            if content:  # Check if the file is not empty
                data = json.loads(content)
                return data
            else:
                print("The task file is empty.")
                return []
    return []
        
def add_task(tasks):
    """
    Add a new project/task with version and features. Prompts the user for details and saves the task.
    """
    project_name = input("Enter the project name: ")
    description = input("Enter a short description of the project: ")
    version_number = input("Enter the version number for this project: ")
    features = []
    print("Enter features for this version (type 'done' when finished):")
    feature_count = 1
    while True:
        feature = input(f"Add feature #{feature_count}: ")
        if feature.lower() == 'done':
            break
        if feature.strip():
            features.append({'feature': feature.strip(), 'Completed': False})
            feature_count += 1
    version = {
        'version number': version_number,
        'features': features
    }
    # Check if project already exists
    for project in tasks:
        if project['project_name'] == project_name:
            project['versions'].append(version)
            save_task(tasks)
            print("Version and features added to existing project.")
            return
    # If not, create new project
    project = {
        'project_name': project_name,
        'description': description,
        'versions': [version]
    }
    tasks.append(project)
    save_task(tasks)
    print("Project with version and features saved.")

def add_version_and_features(tasks):
    """
    Add a new version and features to an existing project. User selects a project and enters new version info.
    """
    if not tasks:
        print("No projects found.")
        return
    print("Select a project to add a new version and features:")
    for i, project in enumerate(tasks, 1):
        print(f'{i}. {project["project_name"]}')
    try:
        index = int(input('Enter the number of the project: ')) - 1
        if 0 <= index < len(tasks):
            version_number = input("Enter the new version number: ")
            features = []
            print("Enter features for this version (type 'done' when finished):")
            feature_count = 1
            while True:
                feature = input(f"Add feature #{feature_count}: ")
                if feature.lower() == 'done':
                    break
                if feature.strip():
                    features.append({'feature': feature.strip(), 'Completed': False})
                    feature_count += 1
            version = {
                'version number': version_number,
                'features': features
            }
            tasks[index]['versions'].append(version)
            save_task(tasks)
            print("New version and features added to project.")
        else:
            print("Please enter a valid project number.")
    except ValueError:
        print("Please enter a number.")

def view_task(tasks):
    """
    Display all tasks/projects with their details, including features and completion status.
    """
    if not tasks:
        print("No projects found.")
        return
    for i, project in enumerate(tasks, 1):
        print(f'{i}. {project["project_name"]}')
        print(f'Description: {project["description"]}')
        if not project.get('versions'):
            print("No versions found.")
        else:
            for j, version in enumerate(project['versions'], 1):
                print(f'Version {j}: {version["version number"]}')
                if not version.get('features'):
                    print("No features found.")
                else:
                    print("Features:")
                    for k, feature in enumerate(version['features'], 1):
                        fstatus = '✔️' if feature.get('Completed') else '❌'
                        print(f'{k}. {feature["feature"]} [{fstatus}]')
        print()


def delete_task(tasks):
    """
    Delete a selected task/project from the list after user confirmation.
    """
    view_task(tasks)
    try:
        index = int(input('Enter the number of the task to delete: ')) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_task(tasks)
            print(f'Task "{removed["project_name"]}" and its features deleted.')
        else:
            print("Please enter a valid task number.")
            return
    except ValueError:
        print("Please enter a number.")

def completed_task(tasks):
    """
    Mark all features in all versions of a selected project as completed.
    """
    view_task(tasks)
    try:
        index = int(input('Enter the number of the project to mark as completed: ')) - 1
        if 0 <= index < len(tasks):
            project = tasks[index]
            for version in project.get('versions', []):
                for feature in version.get('features', []):
                    feature['Completed'] = True
            save_task(tasks)
            print(f'All features in all versions of project "{project["project_name"]}" marked as completed.')
        else:
            print("Please enter a valid project number.")
    except ValueError:
        print('Please enter a number.')

def complete_feature(tasks):
    """
    Mark an individual feature as completed by selecting project, version, and feature.
    """
    if not tasks:
        print("No projects found.")
        return
    for i, project in enumerate(tasks, 1):
        print(f'{i}. {project["project_name"]}')
    try:
        p_index = int(input('Enter the number of the project: ')) - 1
        if 0 <= p_index < len(tasks):
            project = tasks[p_index]
            if not project.get('versions'):
                print("No versions found for this project.")
                return
            for j, version in enumerate(project['versions'], 1):
                print(f'{j}. Version: {version["version number"]}')
            v_index = int(input('Enter the number of the version: ')) - 1
            if 0 <= v_index < len(project['versions']):
                version = project['versions'][v_index]
                if not version.get('features'):
                    print("No features found for this version.")
                    return
                for k, feature in enumerate(version['features'], 1):
                    fstatus = '✔️' if feature.get('Completed') else '❌'
                    print(f'{k}. {feature["feature"]} [{fstatus}]')
                while True:
                    f_index = input('Enter the number of the feature to mark as completed(type "done" when finished): ')
                    if f_index.isdigit() and 0 <= f_index < len(version['features']):
                        version['features'][f_index]['Completed'] = True
                        save_task(tasks)
                        print(f'Feature "{version["features"][f_index]["feature"]}" marked as completed.')
                    elif f_index.strip().lower() == "done":
                        break
                    else:
                        print("Please enter a valid feature number or type 'done'.")
            else:
                print("Please enter a valid version number.")
        else:
            print("Please enter a valid project number.")
    except ValueError:
        print("Please enter a number.")


    


   

def main():
    """
    Main loop for the Task Manager application. Handles user menu and calls appropriate functions.
    """
    tasks = load_task()

    while True:
        print("\n Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark All Features in Project as Completed")
        print("4. Mark Individual Feature as Completed")
        print("5. Delete Task")
        print("6. Add Version and Features to Existing Project")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice =="2":
            view_task(tasks)
        elif choice == '3':
            completed_task(tasks)
        elif choice == '4':
            complete_feature(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            add_version_and_features(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()