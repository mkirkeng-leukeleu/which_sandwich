from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.serializers import OrderSerializer
from rest_framework import status
from datetime import datetime as dt

class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': request.user.username}
        return Response(content)

class OrderList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # TODO: sort orders by date
        if 'today' in request.query_params:
            orders = request.user.orders.filter(order_date__date=dt.now().date())
        else:
            orders = request.user.orders.all()

        serializer = OrderSerializer(instance=orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


