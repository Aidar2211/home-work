from django.forms import ModelForm
from test_app.models import Product_Name, Comment


class ProductForm(ModelForm):
    class Meta:
        model = Product_Name
        fields = 'title category description'.split()


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = 'name body product'.split()


class ProdCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = 'product name body'.split()