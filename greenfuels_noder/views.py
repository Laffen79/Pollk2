from django.shortcuts import render, redirect, get_object_or_404
from .models import GreenFuelsNodes
from .forms import GreenFuelsNodesForm


def greenfuels_noder_view(request):
    greenfuelsnoder = GreenFuelsNodes.objects.all()
    return redirect('greenfuels_noder:greenfuels_noder')

def add_greenfuelsnode(request):
    if request.method == 'POST':
        form = GreenFuelsNodesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('greenfuels_noder:greenfuels_noder')
    else:
        form = GreenFuelsNodesForm()
    return render(request, 'greenfuels_noder/greenfuels_noder_add.html', {'form': form})


def edit_greenfuelsnode(request, id):
    greenfuelsnode = get_object_or_404(GreenFuelsNodes, id=id)
    form = GreenFuelsNodesForm(instance=greenfuelsnode)
    if request.method == 'POST':
        form = GreenFuelsNodesForm(request.POST, instance=greenfuelsnode)
        if form.is_valid():
            form.save()
            return redirect('greenfuels_noder:greenfuels_noder')
    return render(request, 'greenfuels_noder/greenfuels_noder_edit.html', {'form': form, 'greenfuelsnode': greenfuelsnode})


def delete_greenfuelsnode(request, id):
    greenfuelsnode = get_object_or_404(GreenFuelsNodes, id=id)
    if request.method == 'POST':
        greenfuelsnode.delete()
        return redirect('greenfuels_noder:greenfuels_noder')
    return render(request, 'greenfuels_noder/greenfuels_noder_delete.html', {'greenfuelsnode': greenfuelsnode})
