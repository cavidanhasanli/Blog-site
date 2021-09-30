from django.urls import path
from .views import home_view,\
    post_detail_view,\
    post_contact_view,\
    post_create_view,\
    register_view,\
    login_view,\
    logout_view,send_test_mail,post_update_view,post_delete_view

urlpatterns = [
    path("", home_view, name='home_page'),
    path("post-detail/<int:post_id>/", post_detail_view, name='post_detail_page'),
    path("post-contact/", post_contact_view, name='contact_page'),
    path("post-create/", post_create_view, name='post_create_page'),
    path("post-update/<int:post_id>/", post_update_view, name='post_update_page'),
    path("post-delete/<int:post_id>/", post_delete_view, name='post_delete_page'),
    path("register/", register_view, name='register_page'),
    path("login/", login_view, name='login_page'),
    path("logout/", logout_view, name='logout_page'),
    path("mail-send/",send_test_mail, name='mail_send_page')


]