import datetime
class PurchaseModel:
    amount = ""
    purchase_details = []
    
    def __init__(self, purchase_data):
        for key, value in purchase_data.items():
            if key == "amount":
                self.amount = value
            if key == "purchase":
                self.purchase_details = value
            
    def Validatepurchase(self, purchase):
        if purchase.amount == "" or purchase.amount <= 0:
            raise Exception ('Name is invalid')
        if purchase.purchase_details == None or len(purchase.purchase_details) <= 0:
            raise Exception ('Name is invalid')
        return True

    
