import csv

todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    global todos
    x = title
    todos.append(x)
    return todos

def print_list():
    global todos
    for row in todos:
        print(row)
    pass

def delete_task(number_to_delete):
    # your code here
    global todos
    todos.pop(int(number_to_delete)-1)
    return todos

def save_todos():
    # your code here
    global todos
    todos_file = ""
    i = 0

    for elemento in todos:
        if i == 0:
            todos_file = todos_file + elemento 
            i=i+1
        else:
            todos_file = todos_file + ',' +  elemento 

        file_to_save = open("todos_file.csv",'w+')
        file_to_save.write(todos_file)
        file_to_save.close()
    pass

    
def load_todos():
    global todos
    file = open("todos_file.csv","r")
    csv_1 = csv.reader(file)


    for i in csv_1:
        print(i)
        for x in i:
            if x not in todos:
                print(x)
                todos.append(x)  
             
    pass        
    #return todos

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")