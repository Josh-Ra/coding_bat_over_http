from django.contrib import admin
from django.urls import path
from app.views import near_hundred_view, string_splosion_view, cat_dog_view, lone_sum_view

urlpatterns = [
    path("warmup-1/near-hundred/<int:num>", near_hundred_view),
    path("warmup-2/string-splosion/<word>", string_splosion_view),
    path("string-2/cat-dog/<word>", cat_dog_view),
    path("logic-2/lone-sum/<int:a>/<int:b>/<int:c>", lone_sum_view),
    path("admin/", admin.site.urls),
]
