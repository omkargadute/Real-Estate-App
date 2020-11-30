from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import reverse
app_name = 'listing'

urlpatterns = [
    path('',views.ListingView.as_view(),name="all_listing"),
    path('listings/<int:pk>/',views.ListingDetailView.as_view(),name="detail_listing"),
    path('listings/add/',views.AddListingView.as_view(),name="add_listing"),
    path('listings/delete/<int:pk>',views.DeleteListingView.as_view(),name="delete_listing"),
    path('listings/update/<int:pk>',views.UpdateListingView.as_view(),name="update_listing"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)