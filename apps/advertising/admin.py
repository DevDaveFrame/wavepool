from django import forms
from django.contrib import admin
from advertising.models import Advertisement
from news.models import NewsPost

# Register your models here.


class AdvertisementForm(forms.ModelForm):
    # I'm afraid the CheckboxSelectMultiple isn't very practical if there are thousands of articles, but it was quick
    newspost = forms.ModelMultipleChoiceField(queryset=NewsPost.objects.all(), widget=forms.CheckboxSelectMultiple)
    model = Advertisement
    fields = '__all__'

    def save(self, commit=True):
        # save to the db for pk purposes
        instance = super().save(commit)
        instance.save()
        # then add to selected newsposts
        for post in self.cleaned_data['newspost']:
            instance.newspost_set.add(post)
        return instance


class AdvertisementAdmin(admin.ModelAdmin):
    form = AdvertisementForm
    list_display = ['company_name', 'copy']


admin.site.register(Advertisement, AdvertisementAdmin)
