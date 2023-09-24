"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class Salary(Employee):
    def __init__(self, name, fee, comm="", commfee=0, contracts=0):
        super().__init__(name)
        self.fee = fee
        self.comm = comm
        self.commfee = commfee
        self.contracts = contracts

    def get_pay(self):
        if self.comm == "bonus":
            return self.fee + self.commfee
        elif self.comm == "contract":
            return self.fee + self.commfee * self.contracts
        elif self.comm == "":
            return self.fee
        
    def __str__(self):
    #Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
    #Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
    #Billie works on a monthly salary of 4000. Their total pay is 4000.
        payment = self.get_pay()
        if self.comm == "bonus":
            return f"{self.name} works on a monthly salary of {self.fee} and receives a bonus commission of {self.commfee}. Their total pay is {payment}."
        elif self.comm == "contract":
            return f"{self.name} works on a monthly salary of {self.fee} and receives a commission for {self.contracts} contract(s) at {self.commfee}/contract. Their total pay is {payment}."
        elif self.comm == "":
            return f"{self.name} works on a monthly salary of {self.fee}. Their total pay is {self.fee}."

class Hourly(Employee):
    def __init__(self, name, fee, hours, comm="", commfee=0, contracts=0):
        super().__init__(name)
        self.fee = fee
        self.hours = hours
        self.comm = comm
        self.commfee = commfee
        self.contracts = contracts


    def get_pay(self):
        if self.comm == "bonus":
            return self.fee * self.hours + self.commfee
        elif self.comm == "contract":
            return self.fee * self.hours + self.commfee * self.contracts
        elif self.comm == "":
            return self.fee * self.hours


    def __str__(self):
        payment = self.get_pay()
    #Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
    #Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
    #Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
        if self.comm == "contract":
            return f"{self.name} works on a contract of {self.hours} hours at {self.fee}/hour and receives a commission for {self.contracts} contract(s) at {self.commfee}/contract. Their total pay is {payment}."
        elif self.comm == "bonus":
            return f"{self.name} works on a contract of {self.hours} hours at {self.fee}/hour and receives a bonus commission of {self.commfee}. Their total pay is {payment}."
        elif self.comm == "": 
            return f"{self.name} works on a contract of {self.hours} hours at {self.fee}/hour. Their total pay is {payment}."




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary('Billie', 4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly('Charlie', 25, 100)
print(charlie.__str__())
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary('Renee', 3000, "contract", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly('Jan', 25, 150,"contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary('Robbie', 2000, "bonus", 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly('Ariel', 30,120, 'bonus', 600)
