from rest_framework.throttling import UserRateThrottle





class LogoutRateThrottle(UserRateThrottle):
    scope = 'logout'