from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('addorder/', views.addOrder, name = "addorder"),
    path('ordersview/', views.ordersView, name = "ordersview"),
    path('view_order/<int:id>', views.viewOrder, name = "vieworder"),
    path('choose_order/<int:id>', views.chooseOrder, name = "chooseorder"),
]