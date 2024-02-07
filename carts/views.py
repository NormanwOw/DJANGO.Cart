from django.http import Http404, JsonResponse
from django.shortcuts import render

from carts.models import Cart


def cart(request):
    return render(request, 'cart.html', {'title': 'Корзина'})


def new_order(request):
    if request.method == 'POST':
        data = request.POST
        return JsonResponse(data)

    raise Http404


def cart_add(request):
    if request.method == 'POST':
        product_id = int(request.POST['product_id'])
        user_cart_list = Cart.objects.filter(
            user=request.user,
        ).select_related('product').all()
        count = user_cart_list.count()
        user_cart = None

        if user_cart_list:
            for item in user_cart_list:
                if item.product_id == product_id:
                    user_cart = item
                    print(user_cart)
                    break

        if isinstance(user_cart, Cart):
            quantity = user_cart.quantity + 1
            Cart.objects.filter(
                user=request.user,
                product__id=product_id
            ).update(quantity=quantity)
        else:
            Cart.objects.create(
                user=request.user,
                product_id=product_id,
                quantity=1
            )
            count += 1

        return JsonResponse({'product_count': count})

    raise Http404
