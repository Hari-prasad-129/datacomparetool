from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse,JsonResponse
# Create your views here.

@api_view(['GET'])
def home_page(request):
    if request.method == "GET":
        return render(request,'homepage.html')

@api_view(['POST'])
def storage_page(request):
    if request.method == "POST":
        qs = request.data.get('storage')
        name = 'Demodb'
        return render(request,'index.html',context={'database_name':name})
    