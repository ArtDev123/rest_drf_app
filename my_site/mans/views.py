from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Man
from .serializers import ManSerializer

# class ManApiView(generics.ListAPIView):
#     queryset = Man.objects.all()
#     serializer_class = ManSerializer

class ManApiView(APIView):
    def get(self, request):
        mans = Man.objects.all()
        return Response({'posts': ManSerializer(mans, many = True).data})

    def post(self, request):
        serializer = ManSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
     
        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        
        try: 
            instance = Man.objects.get(pk = pk)
        except:
            return Response({"error": "Object does not exists"})
        
        serializer = ManSerializer(data = request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})