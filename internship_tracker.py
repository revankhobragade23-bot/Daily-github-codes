
from datetime import datetime

tasks = [
    {
        "date": "2026-10-25",
        "task": "Follow up with AI + IoT project respondents",
        "status": "In Progress"
    },
    {
        "date": "2026-10-25",
        "task": "Prepare student internship offer letter",
        "status": "Completed"
    },
    {
        "date": "2026-10-26",
        "task": "Create and email the database",
        "status": "Completed"
    },
    {
        "date": "2026-10-26",
        "task": "Follow up on internship certificate format",
        "status": "In Progress"
    },
    {
        "date": "2026-10-26",
        "task": "Contact project respondents",
        "status": "In Progress"
    }
]

def display_tasks():
    print("\n===== INTERNSHIP TASK TRACKER =====")
    print("Report generated:", datetime.now().strftime("%d-%m-%Y %H:%M"))
    print("-" * 65)

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. Date: {task['date']}")
        print(f"   Task: {task['task']}")
        print(f"   Status: {task['status']}")
        print("-" * 65)

    completed = sum(
        1 for task in tasks
        if task["status"] == "Completed"
    )

    print(f"Total tasks: {len(tasks)}")
    print(f"Completed: {completed}")
    print(f"Pending/In progress: {len(tasks) - completed}")

if __name__ == "__main__":
    display_tasks()

