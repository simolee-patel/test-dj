from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myproject.ng_dj.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer