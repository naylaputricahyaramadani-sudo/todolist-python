from task_manager import (
    update_status,
    delete_task,
    search_by_assignee
)

def main():
    while True:
        print("\n=== TO DO LIST ===")
        print("1. Update Status")
        print("2. Delete Task")
        print("3. Search Task")
        print("0. Exit")

        choice = input("Pilih menu: ")

        if choice == "1":
            update_status()

        elif choice == "2":
            delete_task()

        elif choice == "3":
            search_by_assignee()

        elif choice == "0":
            break

if __name__ == "__main__":
    main()