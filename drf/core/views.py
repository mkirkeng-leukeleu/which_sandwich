from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.serializers import OrderSerializer
from django.utils import timezone
from rest_framework import generics
from sandwiches.models import Sandwich
from django_filters.rest_framework import DjangoFilterBackend
from core.serializers import SandwichSerializer

class IndexView(APIView):
    def get(self, request):
        content = {'message': 'Welcome the which sandwhich backend!'}
        return Response(content)

class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': request.user.username}
        return Response(content)

class OrderList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["order_date"]

    def get_queryset(self):
        return self.request.user.orders.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        # expand sandwich representation for each order
        for index, order in enumerate(response.data):
            serializer = SandwichSerializer(Sandwich.objects.get(pk=order['sandwich']))
            response.data[index]['sandwich'] = serializer.data

        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # expand sandwich representation
        serializer = SandwichSerializer(Sandwich.objects.get(pk=response.data['sandwich']))
        response.data['sandwich'] = serializer.data

        return response

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
