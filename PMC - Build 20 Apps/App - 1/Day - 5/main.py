todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: \n")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: \n")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print("\n")
                print(f"{index+1} - {item}\n")
        case "edit":
            print("Enter the todo number for which you want to edit from below: \n")
            for index, item in enumerate(todos):
                print("\n")
                print(f"{index+1} - {item}\n")
            number = int(input())
            number = number - 1
            print(f"Enter the todo that you want to replace with - \"{todos[number]}\"\n")
            new_todo = input()
            todos[number] = new_todo.strip()
            print("Removed Successfully !! Your New Todos are: ")
            for index, item in enumerate(todos):
                print("\n")
                print(f"{index+1} - {item}\n")
        case "complete":
            print("Enter the todo number for which you want to complete the task from below: \n")
            for index, item in enumerate(todos):
                print("\n")
                print(f"{index+1} - {item}\n")
            com_num = int(input())
            todos.pop(com_num - 1)
            print("Removed Successfully !! Your New Todos are: \n")
            for index, item in enumerate(todos):
                print("\n")
                print(f"{index+1} - {item}\n")
        case "exit":
            break

print("\n Bye!!")