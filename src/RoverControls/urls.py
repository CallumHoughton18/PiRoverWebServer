from django.urls import path
from RoverControls import views

urlpatterns = [
    path('initGPIO/<int:forward>/<int:backward>/<int:left>/<int:right>/', views.initGPIO),
    path('forward/<int:forward>/<int:backward>/', views.forward),
    path('backward/<int:forward>/<int:backward>/', views.backward),
    path('left/<int:left>/<int:right>/', views.left),
    path('right/<int:left>/<int:right>/', views.right),
    path('stopForwardAndBackward/<int:forward>/<int:backward>/', views.stopForwardAndBackward),
    path('stopLeftAndRight/<int:left>/<int:right>/', views.stopLeftAndRight),
    path('stopAll/<int:forward>/<int:backward>/<int:left>/<int:right>/', views.stopAll),
]