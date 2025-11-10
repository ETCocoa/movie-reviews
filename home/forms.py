from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, i) for i in range(1, 11)],
        widget=forms.Select
    )
    body = forms.CharField(
        required=False,
        label="Comment (optional)"
    )

    class Meta:
        model = Review
        fields = ('body', 'rating')
