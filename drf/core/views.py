from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.serializers import OrderSerializer
from rest_framework import status
from django.utils import timezone
from rest_framework import generics

class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': request.user.username}
        return Response(content)

class OrderList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    # TODO: use django filters for today filter

    def get_queryset(self):
        if 'today' in self.request.query_params: # /?today
            return self.request.user.orders.filter(order_date__date=timezone.now().date())

        return self.request.user.orders.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
