import datetime
class TransactionModel:
    quantity = ""
    amount = ""
    date = datetime.datetime.utcnow()
    
    def __init__(self, transaction_data):
        for key, value in transaction_data.items():
            if key == "quantity":
                self.quantity = value

    def calculate_total_amout_transaction(self, cost):
        self.amount = cost* abs(self.quantity)
    