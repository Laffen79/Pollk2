from django.shortcuts import render, get_object_or_404
from importer_automater.models import VendanorNode, VendanorNodesInventory, VendanorProduct
from greenfuels_noder.models import GreenFuelsNodes
from django.http import HttpResponse
from hent_produkt.views import get_node_inventory

def kart(request):
    vendanor_nodes = VendanorNode.objects.all()
    greenfuels_nodes = GreenFuelsNodes.objects.all()

    # Bruk en liste til å samle alle nodene
    nodes = []
    vendanor_node_ids = []
    for node in vendanor_nodes:
        if node.id not in vendanor_node_ids:
            vendanor_node_ids.append(node.id)
            nodes.append({
                'location': node.location,
                'serialno': node.serialno,
                'address1': node.address1,
                'postcode': node.postcode,
                'postcity': node.postcity,
                'geo_lat': node.geo_lat,
                'geo_lng': node.geo_lng,
                'retailer_id': node.retailer_id,
                'source': 'Vendanor'
            })

    for node in greenfuels_nodes:
        nodes.append({
            'location': node.location,
            'address1': node.address1,
            'postcode': node.postcode,
            'postcity': node.postcity,
            'geo_lat': node.geo_lat,
            'geo_lng': node.geo_lng,
            'source': 'GreenFuels'
        })

    # Opprett en ny liste med URL-er for hvert node-ID
    return render(request, 'forhandlere/kart.html', {'nodes': nodes})



def node_produkter(request, node_id):
    try:
        node = get_object_or_404(VendanorNode, serialno=node_serialno)
        inventory = VendanorNodesInventory.objects.filter(node=node, product_id=-2).values('product_id', 'count')
        products_with_counts = []
        for item in inventory:
            product = VendanorProduct.objects.get(id=item['product_id'])
            products_with_counts.append({
                'name': product.name,
                'count': item['count'],
                'picture_url': product.get_picture_url()
            })
        return render(request, 'forhandlere/node_produkter.html', {'node': node, 'inventory': products_with_counts})
    except Exception as e:
        return HttpResponse(f"En feil oppstod: {e}")