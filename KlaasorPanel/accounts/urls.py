from django.urls import path
from accounts.views import (
    CreateCustomUserView,
    UpdateCustomUSerView,
    SignInWithPasswordView,
    SendOTPView,
    VerifyOTPView,
    DetailAccountView,
    LogOutView
)


urlpatterns = [
    path("UpdateProfile/<int:pk>", UpdateCustomUSerView.as_view()),
    path("CompleteInformation/<int:pk>", CreateCustomUserView.as_view()),
    path("auth/SignInPassword/", SignInWithPasswordView.as_view()),
    path("auth/send-otp/", SendOTPView.as_view(), name="send_otp"),
    path("auth/verify-otp/", VerifyOTPView.as_view(), name="verify_otp"),
    path("account/you/", DetailAccountView.as_view(), name="view-account"),
    path("user/logout/", LogOutView.as_view(), name="logout-user")
]


