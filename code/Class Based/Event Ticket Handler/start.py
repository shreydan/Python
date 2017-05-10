from handler import ticket_handler
import os

event = ticket_handler()

def handle():
    choice = int(input("1. SELL\n2. RESET\n3. END SESSION / GET A BREAK\n"))
    
    if choice == 1:
        
        os.system('clear')
        sale = event.sell()
        
        if sale is True:
        
            event.register()
            event.update_details()
            event.print_details()
            
        else:
            
            print ("We can't sell {} tickets. We only have {} tickets".format(event.ticketsnum,event.tickets))
            
    elif choice == 2:
        
        os.system('clear')
        event.reset()
    
    elif choice == 3:
        
        os.system('clear')
        exit()
        
    else:
        
        os.system('clear')        
        handle()
        

while True:
    handle()
