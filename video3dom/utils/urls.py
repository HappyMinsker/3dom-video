from django.urls import path, re_path

from . import views

urlpatterns = [
    path("signup/", views.go_404, name="account_signup"),
    path("login/", views.go_404, name="account_login"),
    path("logout/", views.go_404, name="account_logout"),
    path("reauthenticate/", views.go_404, name="account_reauthenticate"),
    path(
        "password/change/",
        views.go_404,
        name="account_change_password",
    ),
    path("password/set/", views.go_404, name="account_set_password"),
    path("inactive/", views.go_404, name="account_inactive"),
    # Email
    path("email/", views.go_404, name="account_email"),
    path(
        "confirm-email/",
        views.go_404,
        name="account_email_verification_sent",
    ),
    re_path(
        r"^confirm-email/(?P<key>[-:\w]+)/$",
        views.go_404,
        name="account_confirm_email",
    ),
    # password reset
    path("password/reset/", views.go_404, name="account_reset_password"),
    path(
        "password/reset/done/",
        views.go_404,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.go_404,
        name="account_reset_password_from_key",
    ),
    path(
        "password/reset/key/done/",
        views.go_404,
        name="account_reset_password_from_key_done",
    ),
]
