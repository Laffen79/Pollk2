from django.shortcuts import render, get_object_or_404
from django.conf import settings
from importer_automater.models import VendanorNodesInventory, VendanorNode, VendanorProduct

def get_node_inventory(request, serialno):
    # Finn noden med den gitte serialno-en
    node = get_object_or_404(VendanorNode, serialno=serialno)

    # Hent inventory for noden
    inventory = VendanorNodesInventory.objects.filter(node=node, product_id=2).first()
    if inventory is None:
        # Returner tom respons hvis det ikke finnes inventory for noden
        return render(request, 'hent_produkt/error.html', {'message': 'Ingen produkter er tilgjengelige på denne noden'})

    # Hent produktinformasjon for hvert produkt i inventory
    products = {}
    for product_id, count in inventory.count.items():
        product = VendanorProduct.objects.filter(id=product_id).first()
        if product is not None:
            product_image = f"{product.picture_id}"
            products[product] = {
                'count': count,
                'image': product_image,
            }

    # Returner respons som HTML
    context = {
        'location': node.location,
        'address1': node.address1,
        'postcode': node.postcode,
        'postcity': node.postcity,
        'products': products
    }
    return render(request, 'hent_produkt/node_inventory.html', context)
