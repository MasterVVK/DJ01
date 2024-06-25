from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def data_view(request):
    return render(request, 'data.html')

def test_view(request):
    return render(request, 'test.html')
