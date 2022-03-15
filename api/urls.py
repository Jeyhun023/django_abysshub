from django.urls import path
from . import views

urlpatterns = [
    path('plagiarism/check/<int:id>', views.check),
    path('search/<str:query>', views.search),
]
