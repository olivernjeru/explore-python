user_input = ''
tasks = []

def show_menu():
    print('Welcome to My To-Do List!')
    print('Enter only the digits below to access My To-Do List functionalities')
    print('1. Add Tasks')
    print('2. View Available Tasks')
    print('3. Remove a Task')
    print('4. Exit')

while user_input != '4':
    show_menu()
    user_input = input('Enter your selection: ')
    if user_input == '1':
        item = input('Add a task: ')
        tasks.append(item)
        print(item, 'was added to your to-do list!')
    elif user_input == '2':
        if tasks != []:
            print('These is your list of tasks: ')
            for item in tasks:
                print(item)
        else:
            print('You have no tasks yet!')
    elif user_input == '3':
        item = input('Please enter the task you want to remove: ')
        if item in tasks:
            tasks.remove(item)
            print(item, 'has been removed from your to-do list!')
        else:
            print(item, 'could not be found in your to-do list')
    elif user_input =='4':
        print('Goodbye!')
    else:
        print('Please enter either 1, 2, 3 or 4.')
