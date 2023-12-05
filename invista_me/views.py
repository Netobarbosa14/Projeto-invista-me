from django.shortcuts import render, redirect, HttpResponse
from .models import Investimento
from .forms import InvestimentoModelForm
from django.contrib.auth.decorators import login_required


def novo_investimento(request):
    return render(request, 'investimentos/novo_investimento.html')

def investimentos(request):
    dados = {
        'dados': Investimento.objects.all()
    }
    return render(request,'investimentos/investimentos.html',context=dados)

def detalhe(request,id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk= id_investimento)}
    return render(request,'investimentos/detalhe.html', dados)
@login_required
def criar(request):
    if request.method == "POST":
        investimento_form = InvestimentoModelForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
            return redirect('investimentos')
    else:
        investimento_form = InvestimentoModelForm()
        formulario = {
            'formulario': investimento_form
        }
        return render(request,'investimentos/novo_investimento.html', context=formulario)
    
@login_required
def editar(request, id_investimento):
    investimento = Investimento.objects.get(pk= id_investimento)
    # novo_investimento/1 -> GET
    if request.method == "GET":
        formulario = InvestimentoModelForm(instance=investimento)
        return render(request, 'investimentos/novo_investimento.html',{'formulario': formulario})
    # Caso requisição seja POST
    else:
        formulario = InvestimentoModelForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('investimentos')
    
@login_required
def excluir(request, id_investimento):
    investimento = Investimento.objects.get(pk= id_investimento)
    if request.method == "POST":
        investimento.delete()
        return redirect('investimentos')
    return render(request, 'investimentos/confirmar_exclusao.html',{'item': investimento})
