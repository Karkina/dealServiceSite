from django.urls import path
from snippets import views

urlpatterns = [
    path('api/v1/deals/', views.snippet_list),
    path('api/v1/deal/<int:pk>/', views.snippet_detail),

    path('api/v1/deal/name=<name>/', views.snippet_detailByName),
    path('api/v1/dealsNumber/', views.snippet_numberDeal),

]