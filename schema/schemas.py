def individual_serial(todo) -> dict : 
    return { 
        'id' : str(todo["_id"]),
        'name' : todo['name'],
        'decription' : todo['decription'], 
        'complete' : todo['complete']
    }

def list_serial(todos) -> list : 
    return [individual_serial(todo) for todo in todos]