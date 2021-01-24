from .models import Post
from bootstrap_modal_forms.forms import BSModalModelForm

class TestModelForm(BSModalModelForm):
    class Meta:
        model = Post
        fields = ['title']

