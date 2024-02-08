from django.urls import path
from . import views
import init_image.views

urlpatterns = [
    path("", views.upload_image, name="upload_image"),
    path("gray/", views.page_gray, name="page_gray"),
    path("black&white/", views.black_white, name="black_white"),
    path("resize/", views.resize_picture, name="resize_picture"),
    path("align_v/", views.alignement_vertical, name="alignement_vertical"),
    path("align_h/", views.alignement_horizontal, name="alignement_horizontal"),
    path("fusion/", views.fusion, name="fusion"),
    path("animation/", views.animation, name="animation"),
]