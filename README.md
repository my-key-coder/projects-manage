# Task Manager

A simple command-line Task Manager for managing projects, versions, and features. Each project can have multiple versions, and each version can have a list of features with completion status.

## Features
- Add new projects with versions and features
- Add new versions and features to existing projects
- View all projects, versions, and features
- Mark all features in a project as completed
- Mark individual features as completed
- Delete projects
- Data is persisted in a JSON file (`task_file.json`)

## Usage

1. **Run the application:**
   ```powershell
   python taskmanager.py
   ```

2. **Menu Options:**
   - `1. Add Task`: Add a new project with version and features
   - `2. View Tasks`: View all projects, versions, and features
   - `3. Mark All Features in Project as Completed`: Mark all features in a project as completed
   - `4. Mark Individual Feature as Completed`: Mark a specific feature as completed
   - `5. Delete Task`: Delete a project
   - `6. Add Version and Features to Existing Project`: Add a new version and features to an existing project
   - `7. Exit`: Exit the application

3. **Data Storage:**
   - All data is stored in `task_file.json` in the same directory as the script.

## Requirements
- Python 3.x

## Notes
- The application is interactive and runs in the terminal.
- Make sure `task_file.json` is writable in the current directory.

## License
This project is licensed under the MIT License.
