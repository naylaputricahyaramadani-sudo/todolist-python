def update_status(index, status):
    if 0 <= index < len(tasks):
        tasks[index]["status"] = status
        print("Status berhasil diupdate!")
    else:
        print("Index tidak valid.")

def delete_task(index):
    if 0 <= index < len(tasks):
        deleted_task = tasks.pop(index)
        print(f"Task '{deleted_task['title']}' berhasil dihapus!")
    else:
        print("Index tidak valid.")
        
def search_task(assignee):
    found = False

    for task in tasks:
        if task["assignee"].lower() == assignee.lower():
            print(task)
            found = True

    if not found:
        print("Task tidak ditemukan.")