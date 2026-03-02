import json


class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.done = False

    def complete(self):
        self.done = True

task1 = Task("Invata Pyton", "Sa faci ziua 1")
print(task1.title, task1.done)
task1.complete()
print(task1.done)

tasks = [{"title": "Invata Pyton", "done": False }, {"title": "Fa exercitii", "done": False }]

with open("tasks.json", "w") as f:
    json.dump(tasks, f)

with open("tasks.json", "r") as f:
    loaded_tasks = json.load(f)

print(loaded_tasks)