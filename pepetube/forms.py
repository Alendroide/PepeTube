from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'archivo_video','archivo_imagen']
    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['archivo_video'].widget.attrs['accept'] = 'video/mp4,video/x-m4v,video/*'