import datetime
class InvoiceModel:
    amount = ""
    products = []
    
    def __init__(self, invoice):
        for key, value in invoice.items():
            if key == "amount":
                self.amount = value
            if key == "products":
                self.products = value
            
    def ValidateInvoice(self, invoice):
        if invoice.amount == "" or invoice.amount <= 0:
            raise Exception ('Invalid Amount')
        if invoice.products == None or len(invoice.products) <= 0:
            raise Exception ('Invalid products details')
        return True

    
