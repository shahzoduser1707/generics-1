from django.shortcuts import render
from rest_framework.response import Response
from .serializer import AuthorSerializers,BookSerializers
from .models import AuthorModel,BookModel
from rest_framework import generics
# Create your views here.

class getAuthor(generics.ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers

class getBook(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializers

class detailAuthor(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializers
