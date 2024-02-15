from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.db import transaction

from carts.models import Cart, Order, OrderItem


class CartView(LoginRequiredMixin, ListView):
    template_name = 'cart.html'
    context_object_name = 'carts'
    extra_context = {'title': 'Корзина'}

    def get_queryset(self):
        queryset = Cart.objects.filter(user=self.request.user).select_related('product')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = Cart.objects.total_price()
        return context

    def post(self, request, *args, **kwargs):
        product = request.POST.get('product')
        Cart.objects.filter(user=self.request.user, product__name=product).delete()
        return super().get(request, *args, **kwargs)


@login_required
def new_order(request):
    if request.method == 'POST':
        data = request.POST
        return JsonResponse(data)

    raise Http404


class AcceptOrderView(LoginRequiredMixin, TemplateView):
    template_name = 'order.html'
    context_object_name = 'order'
    extra_context = {'title': 'Заказ'}

    def get(self, request, *args, **kwargs):
        with transaction.atomic():
            cart_items = Cart.objects.filter(user=self.request.user).select_related('product')
            if cart_items.exists():
                order = Order.objects.create(user=self.request.user)

                for cart_item in cart_items:
                    product = cart_item.product
                    name = cart_item.product.name
                    price = cart_item.product.price
                    quantity = cart_item.quantity
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        name=name,
                        price=price,
                        quantity=quantity,
                    )
                    product.quantity -= quantity
                    product.save()

                cart_items.delete()
            else:
                raise Http404

        return super().get(request, *args, **kwargs)


@login_required
def cart_update(request):
    if request.method == 'GET':
        quantity = request.GET.get('quantity')
        product = request.GET.get('product')
        Cart.objects.filter(
            user=request.user,
            product__name=product
        ).update(quantity=quantity)
        total_price = Cart.objects.total_price()
        return JsonResponse({'status': 'ok', 'total_price': total_price}, status=200)

    raise Http404


@login_required
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
