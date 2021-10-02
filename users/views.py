from django.db.models.query_utils import select_related_descend
from django.shortcuts import render
from django.contrib.auth import get_user_model
from accounts.models import User
from django.views.generic import ListView

# Create your views here.

User = get_user_model()

def profiles(request):
    return render(request, 'users/profiles.html')

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
    

