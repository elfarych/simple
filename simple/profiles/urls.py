from django.urls import path
from . import views


urlpatterns = [
    path('seller/me/', views.SellerMeView.as_view()),
    path('seller/create/', views.CreateSellerView.as_view()),
    path('seller/update/<int:pk>/', views.UpdateSellerView.as_view()),
    path('seller/document/create/', views.CreateSellerDocumentView.as_view()),
    path('seller/document/delete/<int:pk>/', views.DeleteSellerDocumentView.as_view()),

    path('buyer/me/', views.BuyerMeView.as_view()),
    path('buyer/create/', views.CreateBuyerView.as_view()),
    path('buyer/update/<int:pk>/', views.UpdateBuyerView.as_view())
]