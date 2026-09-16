from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .forms import LivroForm


def lista_livros(request):
    livros = Livro.objects.all()  # busca no banco

    nome = request.GET.get('nome', '').strip()
    tipo = request.GET.get('tipo', '').strip()
    categoria = request.GET.get('categoria', '').strip()

    if nome:
        livros = livros.filter(
            models.Q(titulo__icontains=nome) | models.Q(autor__icontains=nome)
        )
    if tipo:
        livros = livros.filter(tipo_acervo=tipo)
    if categoria:
        livros = livros.filter(categoria=categoria)

    return render(
        request, 'acervo/lista.html',
        {
            'livros': livros,  # envia ao template
            'tipos': Livro.TipoAcervo.choices,
            'categorias': Livro.Categoria.choices,
            'filtro_nome': nome,
            'filtro_tipo': tipo,
            'filtro_categoria': categoria,
        }
    )


def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()  # grava no banco
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})


# Bônus (conteúdo da Aula 6): editar e apagar, para fechar o CRUD.
def editar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'acervo/form.html', {'form': form, 'livro': livro})


def apagar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('lista')
    return render(request, 'acervo/confirmar_exclusao.html', {'livro': livro})
