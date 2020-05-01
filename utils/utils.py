import inspect


class Utils:
    baseurl = "https://www.demoblaze.com/index.html"
    login_username = "saurav.sharma"
    login_password = "saurav001"

    def whoami(self):
        return inspect.stack([1][3])