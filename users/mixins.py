from django.contrib.auth.mixins import UserPassesTestMixin


class LoggedOutOnlyView(UserPassesTestMixin):

    pass
