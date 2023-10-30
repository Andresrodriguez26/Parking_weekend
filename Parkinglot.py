# Group project members: Andres, Berik & Elizabeth

class Parking_garage:
    def __init__(self, max_tickets, max_parkingspaces):
        self.tickets = list(range(1, max_tickets + 1))
        self.parking_spaces = list(range(1, max_parkingspaces + 1))
        self.actualticket = {}

    def takeTicket(self):
        if len(self.tickets) > 0 and len(self.parking_spaces) > 0:
            ticket = self.tickets.pop(0)
            parkingspaces = self.parking_spaces.pop(0)
            self.actualticket = {"ticket": ticket, "parkingspaces": parkingspaces, "paid": False }
            print(f"Please take your ticket #{ticket}. Your parking space is #{parkingspaces}. ")

    def payForParking(self):
        if "ticket" in self.actualticket and not self.actualticket["paid"]:
            payment = input("Please pay for this ticket: ")
            if payment:
                self.actualticket["paid"] = True
                print("Thank you for your payment. Please be advice you have 10 mintues to leave the garage.")
            else:
                print("Payment is required to exit. Please make sure you pay for your parking")
    
    def leaveGarage(self):
        if 'ticket' in self.actualticket:
            if self.actualticket['paid']:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(self.actualticket['parkingspaces'])
                self.tickets.append(self.actualticket['ticket'])
                self.actualticket = {}
            else:
                print("Payment is required to exit. Please pay for your parking.")

garage = Parking_garage(10, 10)
while True:
    action = input("Please pick one of the following selections: (take/pay/leave/quit): ").lower()
    if action == "take":
        garage.takeTicket()
    elif action == "pay":
        garage.payForParking()
    elif action == "leave":
        garage.leaveGarage()
    elif action == "quit":
        break
    else:
        print("INVALID selection. Please choose on of the following: 'take', 'pay', 'leave', or 'quit'.")