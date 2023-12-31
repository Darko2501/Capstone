from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer,BookingSerializer,UserSerializer
from rest_framework.decorators import api_view,parser_classes
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .forms import BookingForm
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)
class MenuItemView(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
    permission_classes=[IsAuthenticated]
class SingleMenuItemView(generics.RetrieveUpdateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]
class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
@api_view()
@parser_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})