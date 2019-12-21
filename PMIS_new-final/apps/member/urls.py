from django.urls import path

from .views import MemberSearch, Piechart

app_name = "member"

urlpatterns = [
    path('search/', MemberSearch.as_view(), name='search'),
    path('piechart/', Piechart.as_view(), name='piechart')
    # path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]
