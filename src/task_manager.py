import json

DATA_FILE = "data/tasks.json"


def load_tasks():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


# FITUR UPDATE STATUS

def update_status():
    tasks = load_tasks()

    task_id = int(input("Masukkan ID task: "))
    new_status = input("Status baru: ")

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            print("Status berhasil diubah.")
            return

    print("Task tidak ditemukan.")


# FITUR DELETE TASK

def delete_task():
    tasks = load_tasks()

    task_id = int(input("Masukkan ID task yang akan dihapus: "))

    new_tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    if len(new_tasks) == len(tasks):
        print("Task tidak ditemukan.")
    else:
        save_tasks(new_tasks)
        print("Task berhasil dihapus.")



# FITUR SEARCH TASK

def search_by_assignee():
    tasks = load_tasks()

    keyword = input("Masukkan nama assignee: ").lower()

    results = [
        task for task in tasks
        if keyword in task["assignee"].lower()
    ]

    if not results:
        print("Task tidak ditemukan.")
    else:
        print("\nHasil pencarian:")
        for task in results:
            print(task)


# FUNCTION UNTUK PYTEST


def get_all_tasks():
    return load_tasks()


def add_task(title, description, priority, assignee):
    tasks = load_tasks()

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "status": "todo",
        "priority": priority,
        "assignee": assignee
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return new_task


def update_task_status(task_id, new_status):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            save_tasks(tasks)
            return task

    return None


def delete_task_by_id(task_id):
    tasks = load_tasks()

    new_tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    save_tasks(new_tasks)

    return new_tasks


def search_task_by_assignee(keyword):
    tasks = load_tasks()

    results = [
        task for task in tasks
        if keyword.lower() in task["assignee"].lower()
    ]

    return results