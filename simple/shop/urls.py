from django.urls import path
from . import views


urlpatterns = [
    path('shop/my/', views.MyShopView.as_view()),
    path('shop/list/', views.ShopListView.as_view()),
    path('shop/detail/<int:pk>/', views.ShopDetailView.as_view()),
    path('shop/update/<int:pk>/', views.ShopUpdateView.as_view()),
    path('shop/create/', views.ShopCreateView.as_view()),
    path('shop/delete/<int:pk>/', views.ShopDeleteView.as_view()),
    path('shop-image/create/', views.ShopImageCreateView.as_view()),
    path('shop-image/delete/<int:pk>/', views.ShopImageDeleteView.as_view()),

    path('main-category/list/', views.MainCategoryListView.as_view()),
    path('main-category/detail/<int:pk>/', views.MainCategoryDetailView.as_view()),

    path('category/list/', views.CategoryListView.as_view()),
    path('category/detail/<int:pk>/', views.CategoryDetailView.as_view()),

    path('produts/list/', views.ProductListView.as_view()),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view()),
    path('product/create/', views.ProductCreateView.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view()),

    path('product-image/list/', views.ProductImagesListView.as_view()),
    path('product-image/create/', views.ProductImageCreateView.as_view()),
    path('product-image/delete/<int:pk>/', views.ProductImageDeleteView.as_view()),

    path('product-video/list/', views.ProductVideosListView.as_view()),
    path('product-video/create/', views.ProductVideoCreateView.as_view()),
    path('product-video/delete/<int:pk>/', views.ProductVideoDeleteView.as_view()),

    path('review/list/', views.ReviewListView.as_view()),
    path('review/create/', views.ReviewCreateView.as_view()),
    path('review/update/<int:pk>/', views.ReviewUpdateView.as_view()),
    path('review/delete/<int:pk>/', views.ReviewDeleteView.as_view())
]
