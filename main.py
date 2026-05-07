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
print(tasks)