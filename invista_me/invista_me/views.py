from django.shortcuts import render,redirect,HttpResponse
from .models import Investimento
from .forms import InvestimentoForm

# Create your views here.
def investimentos(request):
    dados = {
        'dados':Investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html', context=dados)


def detalhe(request, id):
    dados = {
        'dados':Investimento.objects.get(pk=id)
    }
    return render(request,'investimentos/detalhe.html', context=dados)    


def criar(request):
    if request.method == 'POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('investimentos')    
    else:
        investimento_form = InvestimentoForm()
        formulario = {
            'formulario': investimento_form 
        }
        return render (request, 'investimentos/novo_investimento.html', context=formulario)


def editar(request,id):
    investimento = Investimento.objects.get(pk=id)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request,'investimentos/novo_investimento.html',{'formulario': formulario})
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento) 
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos') 


def excluir(request,id):
    investimento = Investimento.objects.get(pk=id)
    if request.method == 'POST':
        investimento.delete()
        return redirect('investimentos')
    return render(request,'investimentos/confirmar_exclusao.html',{'item': investimento})
