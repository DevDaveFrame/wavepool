from django import forms
from django.contrib import admin, messages
from news.models import NewsPost


class NewsPostForm(forms.ModelForm):
    model = NewsPost
    fields = '__all__'


class NewsPostAdmin(admin.ModelAdmin):
    form = NewsPostForm
    list_display = ['title', 'source_divesite', 'is_cover_story', 'active']
    list_editable = ['is_cover_story', 'active']

    def save_model(self, request, obj, form, change):
        if 'is_cover_story' in form.changed_data:
            obj.save()
            if not NewsPost.objects.filter(is_cover_story=True).exists():
                messages.add_message(request, messages.ERROR, 'Warning! There is no cover story!')
        super().save_model(request, obj, form, change)


admin.site.register(NewsPost, NewsPostAdmin)
