def update_status(index, status):
    if 0 <= index < len(tasks):
        tasks[index]["status"] = status
        print("Status berhasil diupdate!")
    else:
        print("Index tidak valid.")