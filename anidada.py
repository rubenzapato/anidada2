orders = {1: ["item_1", "item_2"], 2: ["item_3", "item_4"], 3: ["item_5", "item_6"]}

def orders_list(): 
    print("El número de órdenes de hoy es: " + str(len(orders)))
    
    def show_orders(): 
        for i in orders: 
            print(f"Orden no. {i}:")
            for item in orders[i]: 
                print(f"Producto: {item}")
    
    show_orders()

orders_list()