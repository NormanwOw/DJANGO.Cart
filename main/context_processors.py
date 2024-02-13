from carts.models import Cart
from django.contrib.auth.models import AnonymousUser


def product_count(request):
    count = 0
    if not isinstance(request.user, AnonymousUser):
        result = Cart.objects.filter(user=request.user)
        count = result.count()

    return {'product_count': count}
