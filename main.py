# main.py

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def list_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for idx, task in enumerate(self.tasks, 1):
                print(f'{idx}. {task}')

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" removed.')
        else:
            print('Invalid task number.')

    def run(self):
        while True:
            command = input('Enter command (add/list/remove/exit): ').strip().lower()
            if command == 'add':
                task = input('Enter task: ').strip()
                self.add_task(task)
            elif command == 'list':
                self.list_tasks()
            elif command == 'remove':
                try:
                    task_number = int(input('Enter task number to remove: ').strip())
                    self.remove_task(task_number)
                except ValueError:
                    print('Please enter a valid number.')
            elif command == 'exit':
                print('Exiting Todo App.')
                break
            else:
                print('Unknown command.')

if __name__ == '__main__':
    app = TodoApp()
    app.run()
