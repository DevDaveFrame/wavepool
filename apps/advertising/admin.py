from django.contrib import admin, forms
from advertising.models import Advertisement
from news.models import NewsPost

# Register your models here.


class AdvertisementForm(forms.ModelForm):
    newspost = forms.ModelMultipleChoiceField(queryset=NewsPost.objects.all(), widget=forms.CheckboxSelectMultiple)
    model = Advertisement
    fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit)
        instance.save()
        for post in self.cleaned_data['newspost']:
            instance.newspost_set.add(post)
        return instance


class AdvertisementAdmin(admin.ModelAdmin):
    form = AdvertisementForm
    list_display = ['company_name', 'copy']


admin.site.register(Advertisement, AdvertisementAdmin)
