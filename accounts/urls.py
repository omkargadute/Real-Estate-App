from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup, name = 'signup'),
    path('login/',views.lgin, name = 'login'),
    path('logout/',views.lgout, name = 'logout'),
    path('profile/agents',views.AgentListView.as_view(), name = 'agents'),
    path('profile/agent/<slug:slug>/',views.AgentDetailView.as_view(), name = 'agent'),
    path('profile/create/',views.AgentCreateView.as_view(), name = 'create_agent'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)