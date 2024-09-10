from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Kadek Savitri',
        'npm' : '2306203236'
        
    }

    return render(request, "main.html", context)