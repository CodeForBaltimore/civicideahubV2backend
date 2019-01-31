from django.shortcuts import render
from rest_framework import generics
from .serializers import IdeaSerializer
from .models import Idea
from rest_framework import permissions
from .permissions import IsOwner

class CreateView(generics.ListCreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    #permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    # permission_classes = (
    #     permissions.IsAuthenticated,
    #     IsOwner
    # )