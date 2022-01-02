from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename=['products'])
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet, basename=['carts'])
router.register('customers', views.CustomerViewSet, basename=['customers'])

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemsViewSet, basename='cart-items')


urlpatterns = router.urls + products_router.urls + carts_router.urls
# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetails.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:pk>/', views.CollectionDetails.as_view(), name='collection-detail'),
# ]

