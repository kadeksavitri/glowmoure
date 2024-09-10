from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Glowmoure',
        'price' : '30000',
        'description' : 'Glowmoure.id offers aesthetic scented candles with delightful fragrances and cute acrylic nightlights that add a cozy glow to any space. Bring charm and warmth to your home with our beautifully designed products!',
        'category' : 'scented candle',
        'stock' : '10'

    }

    return render(request, "main.html", context)