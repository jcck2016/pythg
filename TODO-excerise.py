Headerr = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/

"""

print(Headerr)

todos = []
while True:
    for i in range(len(todos)):
        print(f"{i+1}) {todos[i]}")

    print("____________________________________")
    print("Enter a command. Type h for help")
    command = input(">>  ")
    if command == 'q':
        break
    elif command.isnumeric():
        indx = int(command) - 1
        if indx >= len(todos):
            print(
                "***Entry Error*** ...There is no such item in the TODO list ... PLEASE TRY AGAIN")
        if indx == len(todos):
            print("There are no more items in the TODO list ... Please add more item(s)")
        else:
            todos.pop(indx)
    else:
        todos.append(command)

print("Goodbye................\n")
