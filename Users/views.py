from rest_framework import viewsets, status
from rest_framework.response import Response
from Users.models import CustomUser, Address
from Users.serializers import ShortUserSerializer, FullUserSerializer, AddressSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = CustomUser
    serializer_class = ShortUserSerializer

    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def list_with_address_count(self, request, *args, **kwargs):
        address_limit = self.request.GET.get('address_limit')
        if not address_limit:
            address_limit = 3
        self.queryset = CustomUser.objects.get_users_with_three_addresses(limited_address_count=int(address_limit))
        self.serializer_class = FullUserSerializer
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def get_queryset(self):
        return CustomUser.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    model = Address
    serializer_class = AddressSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return super(AddressViewSet, self).create(request, *args, **kwargs)
