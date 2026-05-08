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