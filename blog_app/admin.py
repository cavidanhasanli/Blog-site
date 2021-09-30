from django.contrib import admin
from blog_app.models import Settings,NavbarModel,Footer,PostModel,PostImageModel,PostContactModel
# Register your models here.

admin.site.register(Settings)
admin.site.register(NavbarModel)
admin.site.register(Footer)

admin.site.register(PostModel)
admin.site.register(PostImageModel)
admin.site.register(PostContactModel)