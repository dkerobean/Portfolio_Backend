from rest_framework import viewsets
from .serializers import ProfileSerializer, ContactSerializer
from .models import Profile, Contact


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
