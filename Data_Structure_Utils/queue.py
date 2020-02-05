class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) < 1:
            return None
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def showQueue(self):
        for item in self.items:
            print(item,end = ' ')

    def BankingcashCounter(self):

        cash = 50000 # money bank have
        deposit = 0 # money that user want to deposit
        withdraw = 0 # money that user want to withdraw

        while True:
            print("Select one of the following operations: ")
            print("1.Deposit Money")
            print("2.Withdraw Money")
            print("3.Exit")

            choice = int(input("Enter the choice(1 to 3)"))
            if choice == 1:
                self.enqueue(1)
                amount = int(input("Enter the amount to be deposited: "))
                if amount == 0:
                    print("Please enter the amount to be deposited: ")
                else:
                    deposit+=amount
                    cash+=amount
                    print(f"Thank You,you have deposited {amount} successfully")
                    print(f"The updated balance is : {deposit}")
                self.dequeue()

            elif choice == 2:
                self.enqueue(1)

                amount = int(input("Enter the amount to withdraw: "))

                if deposit >= amount :
                    deposit -= amount
                    cash -= amount
                    print(f"Thank you , {amount} withdraw successfully")
                    print(f"The updated balance is : {deposit}")
                    self.dequeue()
                else:
                    print("Insufficient Balance")
                    self.dequeue()

            elif choice == 3:
                quit()

            else:
                self.BankingcashCounter()
