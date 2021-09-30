# from core.models import HomePageBanner, HomePageAdvert, WebsiteSetting, MenuItem,Setting,ContactPageData
# import math

from blog_app.models import NavbarModel, Footer,Settings


def header_and_footer(request):
    context = {}
    navbar_queryset = NavbarModel.objects.all()
    settings_queryset = Settings.objects.all().first()
    footer_queryset = Footer.objects.all()
    context['navbar_queryset'] = navbar_queryset
    context['settings_queryset'] = settings_queryset
    context['footer_queryset'] = footer_queryset
    return context
