from phonestore.models import PhoneStore
from .serializers import PhoneStoreSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, list_route, api_view, permission_classes
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie, csrf_exempt
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny

class PhoneStoreViewSet(viewsets.ModelViewSet):
    queryset = PhoneStore.objects.all()
    serializer_class = PhoneStoreSerializer

    @action(methods=['post'], detail=False, url_path='products')
    def get_product_list(self, request):
        # print "request==>",request.data
        dataset = PhoneStore.objects.values()
        response = [
            {
                'id': 1,
                'title': "Realme 3",
                'img': "img/realme-3.png",
                'price': 9999,
                'company': "Realme",
                'info': "Information about Realme 3.",
                'inCart': False,
                'count': 0,
                'total': 0,
                'tax': 99,
            },
            {
                'id': 2,
                'title': "Redmi Note 7",
                'img': "img/redmi-note-7.png",
                'price': 11999,
                'company': "Xiaomi",
                'info': "Information about Redmi Note 7.",
                'inCart': False,
                'count': 0,
                'total': 0,
                'tax': 199,
            },
            {
                'id': 3,
                'title': "Samsung GalaxyA50",
                'img': "img/samsung-galaxy-a50.png",
                'price': 22990,
                'company': "Samsung",
                'info': "Information about Samsung Galaxy A50.",
                'inCart': False,
                'count': 0,
                'total': 0,
                'tax': 499,
            },
            {
                'id': 4,
                'title': "One Plus 6T",
                'img': "img/one-plus-6t.png",
                'price': 32999,
                'company': "One Plus",
                'info': "Information about One Plus 6T.",
                'inCart': False,
                'count': 0,
                'total': 0,
                'tax': 999,
            },
        ]
        new_list = response + list(dataset)
        return Response(new_list, status=status.HTTP_200_OK)
