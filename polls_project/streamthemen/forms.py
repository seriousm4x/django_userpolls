from django import forms
from .models import Topic


class AddTopicForm(forms.Form):
    class Meta:
        model = Topic
        fields = []
    topic_input = forms.CharField(label="topic_input", required=False)


class EditTopicForm(forms.Form):
    class Meta:
        model = Topic
        fields = []
    topic_input = forms.CharField(label="topic_input", required=False)
    topic_id = forms.CharField(label="topic_id", required=False)


class DeleteTopicForm(forms.Form):
    class Meta:
        model = Topic
        fields = []
    topic_id = forms.CharField(label="topic_id", required=False)
