import requests

myobj = {
        "nom": "hello dealService3",
        "montant": 200.00,
        "code": "d198aad4-99e6-4e85-9cc5-1af525498ec8",
        "devise": "Eur",
        "zone": "Europe",
        "borower": "0",
        "lender": "Quan.Nguyen",
        "status": "Structuring"
}

url = 'http://127.0.0.1:8000/api/v1/deals/'


def fullName(personne):
    return personne["firstName"]+"."+personne["lastName"]


def post_deals_from_rabbitmq(messageList):
    for message in messageList:

        jsonResponse = message.json()
        myobj['nom'] = jsonResponse['deal']['name']
        myobj['montant'] = jsonResponse['deal']['amount']//1000
        myobj['code'] = jsonResponse['code']
        myobj['lender'] = fullName(jsonResponse['deal']['dealCreator'])
        print(requests.post(url, data=myobj))