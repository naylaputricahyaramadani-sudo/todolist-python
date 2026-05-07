tasks = []

def add_task():
    task = input("Masukkan task: ")

    if task != "":
        tasks.append(task)
        print("Task berhasil ditambahkan")
    else:
        print("Task tidak boleh kosong")

add_task()

print("\nDaftar Task:")
for t in tasks:
    print("-", t)

def show_tasks():

    if len(tasks) == 0:
        print("Belum ada task.")
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")