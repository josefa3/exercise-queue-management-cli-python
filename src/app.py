import json
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
    
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...\n")
    x = 0
    for i in queue.get_queue():
        name_to_show = queue.get_queue()[x]["name"]
        print(f"({x+1}) {name_to_show}")
        x+=1

def add():
    name = input("Escriba su nombre: \n") 
    numb = int(input("Escriba su numero: \n"))
    cliente = {
        "name": name,
        "numb": numb,
    }
    print(f"Hola {name}, tienes {queue.enqueue(cliente)} persona/s por delante")

def dequeue():
    entrega = queue.get_queue()[0]["name"]
    print(f"{entrega}, su orden ha sido entregada")
    name_to_delete=queue.get_queue()[0]["name"]
    send("Su pedido está listo, " + entrega.upper(), queue.get_queue()[0]["numb"])
    queue.dequeue()

def save():
    def write_json(data, filename='queue.json'): ## creo la función write_json, sus parámetros son: una variable y el nombre del archivo a crear
        with open(filename,'w') as jsonFile: ## función open, le paso el nombre del archivo y writer(w), como un nombre del archivo
            json.dump(data, jsonFile, indent=2) ## dump transforma lo que le pasamos a strings, le pasamos la variable
            ## el archivo que la va a contener y indent= coloca saltos de linea 
    with open('queue.json') as json_file: 
        data = json.load(json_file) 
    write_json(queue.get_queue())  

def load():
    #import json #must be avalaible
    # Opening JSON file 
    f = open('queue.json',) ### a esta función de python se le pasan dos parámetros, el nombre del archivo y el modo de lectura
    # returns JSON object as a dictionary 
    data = json.load(f) ## meto en la variable que cree, data, el archivo que se abre en 45
    queue.get_queue().clear() ### limpio el dic
    for index in data:
        queue.get_queue().append({"name":index["name"],"numb":index["numb"]}) ## le agrego las claves y las keys al dic
    print(queue.get_queue())    
    # Closing file 
    f.close() 
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    if option == 1:
        add()
    elif option == 2:
        dequeue()
    elif option == 3:
        print_queue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
