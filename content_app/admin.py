from django.contrib import admin
from content_app.models import Content, StreamPlatform, Review

# Register your models here.
admin.site.register(Content)
admin.site.register(StreamPlatform)
admin.site.register(Review)
