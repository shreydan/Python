from datetime import datetime

class ticket_handler():
        
    def __init__(self):
        
        try:
            with open('event.txt','r') as f:
                event,tickets,unitprice = f.readline().rstrip().split(';')
                self.event = str(event)
                self.tickets = int(tickets)
                self.unitprice = int(unitprice)
                self.value = self.tickets * self.unitprice
                self.original_tickets = self.tickets
        
        except Exception:
            print ("ERROR: empty file OR wrong formatting OR missing values")
            exit()        
        
    def sell(self):
        
        if self.tickets > 0:
            self.buyer = input("Enter buyer's name: ").strip()
            self.ticketsnum = int(input("Enter no. of tickets to purchase ").strip())
            
            if self.ticketsnum > self.tickets:
                
                return False
                
            else:            
                self.cost = self.ticketsnum * self.unitprice
                self.tickets = self.tickets - self.ticketsnum
                
                return True
            
    def register(self):
        
        with open('tickets.txt','a') as f:
            self.ticket_info = self.buyer + " PURCHASED " + str(self.ticketsnum) + " TICKETS OF COST " + str(self.cost) + " ON " + str(datetime.now()) + "\n"
            f.write(self.ticket_info)
            
            
    def update_details(self):
        
        with open ('event.txt','w') as f:
            self.update = self.event + ';' + str(self.tickets) + ';' + str(self.unitprice)
            f.write(self.update) 
    
    def reset(self):
    
        with open ('event.txt','w') as f:
            self.resetvalue = self.event + ';' + str(self.original_tickets) + ';' + str(self.unitprice)
            f.write(self.resetvalue)     
        
        with open ('tickets.txt','w') as f:
            f.write('')
    
    def print_details(self):
        print ("Please collect ${} from {}".format(self.cost,self.buyer))
        
