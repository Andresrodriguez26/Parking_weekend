class Parking_garage:
    def __init__(self, max_tickets, max_spaces):
        self.tickets = list(range(1, max_tickets + 1))
        self.parkingspaces = list(range(1, max_spaces + 1))
        self.actualticket = {}

    def takeTicket(self):
        if len(self.tickets) > 0 and len(self.parkingspaces) > 0:
            ticket = self.tickets.pop(0)
            parkingspace = self.parkingspaces.pop(0)
            self.actualticket = {"ticket": ticket, "parkingspaces": parkingspace, "paid": False }
            print(f"Please take your ticket #{ticket}. Your parking space is #{parkingspace}. ")

    def payForParking(self):
        if "ticket" in self.actualticket and not self.actualticket["paid"]:
            payment = input("Please pay for this ticket: ")
            if payment:
                self.actualticket["paid"] = True
                print("Thank you for your payment. Please be advice you have 10 mintues to leave the garage. ")
            else:
                print("Payment is required to exit. Please make sure you pay for your parking")

        
