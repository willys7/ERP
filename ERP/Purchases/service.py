from models import Provider, Purchase
from Authentication.models import Token
from rest_framework.authtoken.models import Token
from ProviderModel import *
from PurchaseModel import *
from repository import  *
import datetime
import dateutil.parser
import urllib2
import json

def CreateNewProvider(provider):
    if provider == {}:
        raise Exception("Invalid provider")
    providerModel = ProviderModel(provider)
    token = ""
    for key, value in provider.items():
        if key == 'token':
            token = value
    
    if ValidateAuthToken(token):
        if providerModel.ValidateProvider(providerModel):
            provider_model = CreateProvider(providerModel)
            return provider_model
        else:
            raise Exception ("Invalid Store Model")
    else:
        raise Exception ("Invalid Token")
            
def HandlePurchase(purchase):
    if purchase == {}:
        raise Exception("Invalid purchase")
    try:
        purchaseModel = PurchaseModel(purchase)
        token = ""
        provider_nit = ""
        for key, value in purchase.items():
            if key == "token":
                token = value
            if key == "nit":
                provider_nit = value
                
        print provider_nit
        print token

        if ValidateAuthToken(token):
            if purchaseModel.Validatepurchase(purchaseModel):
                provider = FindProviderByNit(provider_nit)
                purchase = CreatePurchase(purchaseModel, provider)
                transactions = HandleTransactionOperations(purchaseModel.purchase_details,
                    purchase)
            if transactions:
                return purchase
            else:
                return "problem to handle a transaction"
    except Exception, e:
        raise Exception (str(e))

def HandleTransactionOperations(transactions, purchase):
    for value in transactions:
        try:
            url = "http://localhost:8008/api-inventory/transaction/"
            print "Value"
            value["purchase"] = purchase.id
            print value
            opener = urllib2.build_opener(urllib2.HTTPHandler)
            request = urllib2.Request(url, data=json.dumps(value))
            request.add_header("Content-Type", "application/json")
            response = opener.open(request)
            print response.read()
        except Exception, e:
            raise Exception(str(e))

    return True

def ValidateAuthToken(token_value): 
    try:
        token = FindIfExistAuthToken(token_value)
        date_active = token.last_activation + datetime.timedelta(hours=2)
        token_date = dateutil.parser.parse(str(date_active)).replace(tzinfo=None)
        now = datetime.datetime.utcnow()
        if token_date < now:
            return False
        else:
            return True
    except Exception, e:
        raise Exception(str(e))

