from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body']  # author will be set from logged-in user

    def clean_title(self):
        title = self.cleaned_data.get('title') # title unmatched word iruntha or space iruntha remove panna cleaned_data use panranga
        if "badword" in title.lower():
            raise forms.ValidationError("Inappropriate word in title.")
        return title
