from django.urls import path
from .views import books_list, book_details

app_name="books"

urlpatterns = [
    path("", books_list),
    path("<int:id>", book_details, name="details")
]