from django.urls import path
from . import views

urlpatterns = [
    path('plagiarism/check/<int:id>', views.check),
    path('forum/search', views.forumSearch),
    path('products/search', views.productSearch),
    path('vectorize', views.vectorize),
]
