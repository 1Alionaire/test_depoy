from django.shortcuts import render

def return_main(request):
    return render(request, 'test_app/index.html')

