from django.shortcuts import render
from .models import VendanorProduct, VendanorNode, VendanorNodesInventory
import requests
import os

def update_database(request):
    # Middlertidig utkommentert

    # make request and put response into response
    url = "https://app.vendanor.com/api/json/rest.getNode"
    apiKey = "a7193d2db8ca2ea198b10605f64518e8"
    request_data = {"languageCode": "no", "inventory": "true"}

    response = requests.post(
        url, 
        json={"apiKey": apiKey, "payload": request_data}, 
        headers={'Content-Type': 'application/json'}
    )

    print(response.json())
    """
    # Returnerer en enkel HTTP-response for testing
    return HttpResponse("Hello World!")
    """
#def update_database(request):
    # make request and put response into response
#    url = "https://app.vendanor.com/api/json/rest.getNode"
#    api_key = os.environ.get('VENDANOR_API_KEY')
#    request_data = {"languageCode": "no", "inventory": "true"}

#    response = requests.post(
#        url, 
#        json={"apiKey": api_key, "payload": request_data}, 
#        headers={'Content-Type': 'application/json'}
#    )

    # return response as HttpResponse
#    return HttpResponse(response.content)

    if response.status_code == 200:
        # truncate tables
        VendanorProduct.objects.all().delete()
        VendanorNode.objects.all().delete()
        VendanorNodesInventory.objects.all().delete()

        data = response.json()
        products = data['payload']['products']
        nodes = data['payload']['nodes']

        # Insert into vendanor_products
        for product in products:
            VendanorProduct.objects.create(
                id=product['id'],
                picture_id=product['picture_id'],
                name=product['name'],
                name_long=product['name_long']
            )

        # Insert into vendanor_nodes and vendanor_nodes_inventory
        for node in nodes:
            if node['geo_lat'] and node['geo_lng']:
                VendanorNode.objects.create(
                    id=node['id'],
                    retailer_id=node['retailer_id'],
                    group_id=node['group_id'],
                    serialno=node['serialno'],
                    location=node['location'],
                    address1=node['address1'],
                    address2=node['address2'],
                    postcode=node['postcode'],
                    postcity=node['postcity'],
                    state=node['state'],
                    country=node['country'],
                    geo_lat=node['geo_lat'],
                    geo_lng=node['geo_lng']
                )

                inventory = node['inventory']
                if 'count' in inventory and isinstance(inventory['count'], dict):
                    for product_id, count in inventory['count'].items():
                        node_instance = VendanorNode.objects.get(id=node['id'])
                        VendanorNodesInventory.objects.create(
                            node=node_instance,
                            product_id=product_id,
                            count=count,
                            location=node['location']
                        )

    return render(request, 'importer_automater/success.html')  # replace 'success.html' with your actual success page
