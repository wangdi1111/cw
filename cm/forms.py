from django.forms import ModelForm

from web import models


class AddBook(ModelForm):
    class Meta:
        model = models.Books
        fields = "__all__"
