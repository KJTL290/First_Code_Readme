import os

def display_menu():
    print('\nWelcome to the Todo List!')
    print('Please choose an option:')
    print('1. View your tasks')
    print('2. Add a new task')
    print('3. Delete a task')
    print('4. Mark task as completed')
    print('5. Quit the application')


def get_choice():
    while True:
        choice = input('\nEnter your choice: ')
        valid_choices = ('1', '2', '3', '4', '5')
        if choice not in valid_choices:
            print('Invalid choice, please select again.')
            continue
        else:
            return choice


def display_tasks(tasks):
    if not tasks:
        print('No tasks in the list.')
        return
    
    print('\nYour Tasks:')
    for index, (task, completed) in enumerate(tasks, start=1):
        status = 'Completed' if completed else 'Incomplete'
        print(f'{index}. {task} - [{status}]')


def add_task(tasks):
    while True:
        task = input('Enter a new task: ').strip()
        if len(task) != 0:
            tasks.append((task, False))  # False means task is not completed
            print(f'Task "{task}" added successfully!')
            break
        else:
            print('Invalid task! Please enter a valid task.')


def remove_task(tasks):
    display_tasks(tasks)

    while True:
        if not tasks:
            break

        try:
            task_number = int(input('Enter the task number to delete: '))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f'Task "{removed_task[0]}" deleted successfully!')
                break
            else:
                raise ValueError

        except ValueError:
            print('Invalid task number! Please try again.')


def mark_task_completed(tasks):
    display_tasks(tasks)

    while True:
        if not tasks:
            break

        try:
            task_number = int(input('Enter the task number to mark as completed: '))
            if 1 <= task_number <= len(tasks):
                task, _ = tasks[task_number - 1]
                tasks[task_number - 1] = (task, True)  # Mark as completed
                print(f'Task "{task}" marked as completed!')
                break
            else:
                raise ValueError

        except ValueError:
            print('Invalid task number! Please try again.')


def load_tasks_from_file():
    tasks = []
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for line in file:
                task, completed = line.strip().rsplit(' | ', 1)
                tasks.append((task, completed == 'True'))  # Convert 'True'/'False' string back to boolean
    return tasks


def save_tasks_to_file(tasks):
    with open('tasks.txt', 'w') as file:
        for task, completed in tasks:
            file.write(f'{task} | {completed}\n')


def main():
    tasks = load_tasks_from_file()

    while True:
        display_menu()
        choice = get_choice()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            save_tasks_to_file(tasks)
            print('Tasks saved! Goodbye!')
            break


if __name__ == '__main__':
    main()
