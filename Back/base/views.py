from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers, status, viewsets, permissions, generics 
from rest_framework.views import APIView
from .serializers import (CustomerSerializer, ArtistSerializer, GenreSerializer, 
                        AlbumSerializer,) 
# InventorySerializer,CartSerializer, 
#                         CartItemSerializer, OrderSerializer, OrderItemSerializer, 
#                         PaymentSerializer, ReviewSerializer)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes

from .models import Customer, Artist, Genre, Album
# from .permissions import IsSuperuser


# class MyView(APIView):
#     """
#     A custom API view that requires the user to be a superuser.
#     Only authenticated users with the 'is_superuser' flag set to True are granted permission.
#     """
#     permission_classes = [IsSuperuser]


# register staff
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                #    email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = False
    user.save()
    return Response("new user born")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['email'] = user.email
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    def create(self, validated_data):
        user = self.context['user']
        print(user)
        return Customer.objects.create(**validated_data,user=user)




# Create your views here.
#################### Customer ####################

@permission_classes([IsAuthenticated])
class manageCustomers(APIView):
    def get(self, request, id=-1):  # axios.get
        if id > -1:
            my_model = Customer.objects.get(id=id)
            serializer = CustomerSerializer(my_model, many=False)
        else:
            my_model = Customer.objects.all()
            serializer = CustomerSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):  # axios.post
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):  # axios.put
        my_model = Customer.objects.get(id=id)
        serializer = CustomerSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):  # axios.delete
        my_model = Customer.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################### Artist ####################
class manageArtists(APIView):
    def get(self, request, id=-1):  # axios.get
        if id > -1:
            my_model = Artist.objects.get(id=id)
            serializer = ArtistSerializer(my_model, many=False)
        else:
            my_model = Artist.objects.all()
            serializer = ArtistSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):  # axios.post
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):  # axios.put
        my_model = Artist.objects.get(id=id)
        serializer = ArtistSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):  # axios.delete
        my_model = Artist.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################### Genre ####################
class manageGenres(APIView):
    def get(self, request, id=-1):  # axios.get
        if id > -1:
            my_model = Genre.objects.get(id=id)
            serializer = GenreSerializer(my_model, many=False)
        else:
            my_model = Genre.objects.all()
            serializer = GenreSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):  # axios.post
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):  # axios.put
        my_model = Genre.objects.get(id=id)
        serializer = GenreSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):  # axios.delete
        my_model = Genre.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################### Album ####################
class manageAlbums(APIView):
    def get(self, request, id=-1):  # axios.get
        if id > -1:
            my_model = Album.objects.get(id=id)
            serializer = AlbumSerializer(my_model, many=False)
        else:
            my_model = Album.objects.all()
            serializer = AlbumSerializer(my_model, many=True)
        return Response(serializer.data)


    def post(self, request):  # axios.post
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):  # axios.put
        my_model = Album.objects.get(id=id)
        serializer = AlbumSerializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):  # axios.delete
        my_model = Album.objects.get(id=id)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)