import argparse
from src.state import load_state
from src.metrics import completion_percent, remaining_commits
from src.tasks import add_task, list_tasks, complete_task
from src.goals import set_goal


def _cmd_status(_args):
    state = load_state()
    pct = completion_percent(state)
    print(f"CommitPilot: {state['completed_commits']}/{state['goal_commits']} ({pct}%)")
    print(f"Remaining: {remaining_commits(state)}")


def _cmd_goal(args):
    set_goal(args.value)
    print(f"Goal updated: {args.value}")


def _cmd_task_add(args):
    add_task(args.title)
    print(f"Task added: {args.title}")


def _cmd_task_list(_args):
    tasks = list_tasks()
    if not tasks:
        print("No tasks yet")
        return
    for i, task in enumerate(tasks):
        mark = "✅" if task.get("done") else "⬜"
        print(f"{i}: {mark} {task.get('title')}")


def _cmd_task_done(args):
    ok = complete_task(args.index)
    print("Task completed" if ok else "Invalid task index")


def build_parser():
    parser = argparse.ArgumentParser(prog="commitpilot", description="Track daily commit goals")
    sub = parser.add_subparsers(dest="command")

    s = sub.add_parser("status", help="Show current progress")
    s.set_defaults(func=_cmd_status)

    g = sub.add_parser("goal", help="Set daily commit goal")
    g.add_argument("value", type=int)
    g.set_defaults(func=_cmd_goal)

    task = sub.add_parser("task", help="Task operations")
    task_sub = task.add_subparsers(dest="task_command")

    ta = task_sub.add_parser("add", help="Add a task")
    ta.add_argument("title")
    ta.set_defaults(func=_cmd_task_add)

    tl = task_sub.add_parser("list", help="List tasks")
    tl.set_defaults(func=_cmd_task_list)

    td = task_sub.add_parser("done", help="Mark task as done")
    td.add_argument("index", type=int)
    td.set_defaults(func=_cmd_task_done)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    if not getattr(args, "func", None):
        _cmd_status(args)
        return
    args.func(args)
