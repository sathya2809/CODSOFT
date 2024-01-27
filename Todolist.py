class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def show_tasks(self):
        if self.tasks:
            print('\nTasks:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')
        else:
            print('No tasks yet.')

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print(f'Task {index} updated.')
        else:
            print('Invalid task index.')

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            print(f'Task {index} deleted: "{deleted_task}"')
        else:
            print('Invalid task index.')


def main():
    todo_list = TodoList()

    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. Show Tasks')
        print('3. Update Task')
        print('4. Delete Task')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.show_tasks()
        elif choice == '3':
            index = int(input('Enter the task index to update: '))
            new_task = input('Enter the new task: ')
            todo_list.update_task(index, new_task)
        elif choice == '4':
            index = int(input('Enter the task index to delete: '))
            todo_list.delete_task(index)
        elif choice == '5':
            print('Exiting the To-Do List application. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')


if __name__ == "__main__":
    main()
    