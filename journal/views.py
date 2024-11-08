from django.shortcuts import render, redirect, get_object_or_404
from .models import Trade
from .forms import TradeForm

def trade_list(request):
    trades = Trade.objects.all()
    return render(request, 'journal/trade_list.html', {'trades': trades})

def trade_add(request):
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trade_list')
    else:
        form = TradeForm()
    return render(request, 'journal/trade_form.html', {'form': form})

def trade_edit(request, id):
    trade = get_object_or_404(Trade, id=id)
    if request.method == 'POST':
        form = TradeForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('trade_list')
    else:
        form = TradeForm(instance=trade)
    return render(request, 'journal/trade_form.html', {'form': form})

def trade_delete(request, id):
    trade = get_object_or_404(Trade, id=id)
    if request.method == 'POST':
        trade.delete()
        return redirect('trade_list')
    return render(request, 'journal/trade_confirm_delete.html', {'trade': trade})
