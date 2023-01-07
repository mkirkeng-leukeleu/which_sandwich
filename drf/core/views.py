from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.serializers import OrderSerializer
from django.utils import timezone
from rest_framework import generics
from sandwiches.models import Sandwich

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
    # TODO: use django filters for today filter

    def get_queryset(self):
        if 'today' in self.request.query_params: # /?today
            return self.request.user.orders.filter(order_date__date=timezone.now().date())

        return self.request.user.orders.all()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        # replace the pk for more useful data like id, name and slug
        # TODO: I wonder if there is a better way to do this, I could change
        # the serializer but I do want to keep the behavior of sending id's on POST
        for index, order in enumerate(response.data):
            sandwich_pk = order['sandwich']
            sandwich_obj = Sandwich.objects.get(pk=sandwich_pk)
            sandwich_dict = {
                'id': sandwich_pk,
                'name': sandwich_obj.name,
                'slug': sandwich_obj.slug,
            }

            response.data[index]['sandwich'] = sandwich_dict
        return response

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
