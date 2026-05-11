from src.task_manager import (
    get_all_tasks,
    add_task,
    update_task_status,
    delete_task_by_id,
    search_task_by_assignee
)


def test_get_all_tasks():
    tasks = get_all_tasks()
    assert isinstance(tasks, list)


def test_add_task():
    result = add_task(
        "Testing Login",
        "Menguji fitur login",
        "high",
        "Karen"
    )

    assert result["title"] == "Testing Login"
    assert result["status"] == "todo"


def test_update_task_status():
    result = update_task_status(1, "done")

    assert result["status"] == "done"


def test_delete_task():
    result = delete_task_by_id(999)

    assert isinstance(result, list)


def test_search_task_by_assignee():
    result = search_task_by_assignee("Rina")

    assert isinstance(result, list)