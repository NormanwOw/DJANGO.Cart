from carts.models import Cart


def product_count(request):
    result = Cart.objects.filter(user=request.user)
    return {'product_count': result.count()}
