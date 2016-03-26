from django.db import models
from django.contrib import admin


class MsgPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'user')


class MsgPost(models.Model):
    user = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime']

    def __unicode__(self):
        return self.title


admin.site.register(MsgPost, MsgPostAdmin)
