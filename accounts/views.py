from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.views.generic import DetailView,CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Agent
from .forms import AgentForm
# Create your views here.
class AgentListView(ListView):
    model = Agent
    template_name = 'accounts/all_agents.html'
    context_object_name = 'agents'

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'accounts/detail_agent.html'

class AgentCreateView(LoginRequiredMixin,CreateView):
    model = Agent
    form_class = AgentForm
    redirect_field_name = 'accounts/detail_agent.html'
    template_name = 'accounts/create_agent.html'

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['pass']
        conpassw = request.POST['conpass']

        user = User.objects.create_user(username = username,password= passw)
        if passw != conpassw:
            print('Passwords don\'t match')
        else:
            user.save()
            print("USER CREATED.........")
            return redirect('listing:all_listing')
    return render(request, 'accounts/signup.html')

def lgin(request):
    if request.method == 'POST':
        username = request.POST['username']
        passw = request.POST['pass']

        user = auth.authenticate(username = username ,password = passw)

        if user:
            auth.login(request,user)
            messages.success(request,'Logged In')
            print("Logged In")
            return redirect('listing:all_listing')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('accounts:login')
    else:
        return render(request,'accounts/login.html')

def lgout(request):
    logout(request)
    return redirect('listing:all_listing')




             
    
