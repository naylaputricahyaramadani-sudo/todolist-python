import json

DATA_FILE = "data/tasks.json"

def load_tasks():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

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