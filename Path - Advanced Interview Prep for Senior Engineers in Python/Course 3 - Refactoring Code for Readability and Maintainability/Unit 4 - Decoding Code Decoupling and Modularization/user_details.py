class Profile:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def display_profile(self):
        print(f"User: {self.username}, Email: {self.email}")
class Authentication:
    def __init__(self, password_hash):
        self.password_hash = password_hash
    def authenticate(self, attempted_password_hash):
        return self.password_hash == attempted_password_hash
class Settings:
    def __init__(self, theme, notifications_enabled):
        self.theme = theme
        self.notifications_enabled = notifications_enabled
    def update_theme(self, new_theme):
        self.theme = new_theme
    def toggle_notifications(self):
        self.notifications_enabled = not self.notifications_enabled
    def display_theme(self):
        print(f"Theme: {self.theme}")
    def display_notifications(self):
        print(f"Notifications Enabled: {self.notifications_enabled}")

class User:
    def __init__(self, username, email, password_hash, theme, notifications_enabled):
        self.profile = Profile(username, email)
        self.auth = Authentication(password_hash)
        self.settings = Settings(theme, notifications_enabled)

    def display_full_user_details(self):
        print("User Details:")
        self.profile.display_profile()
        self.settings.display_theme()
        self.settings.display_notifications()


USER_NAME = "JaneDoe"
USER_EMAIL = "jane@example.com"
USER_PASSWORD_HASH = "5f4dcc3b5aa765d61d8327deb882cf99" # placeholder hash for 'password'
USER_THEME = "Dark"
USER_NOTIFICATIONS_ENABLED = True

user = User(USER_NAME, USER_EMAIL, USER_PASSWORD_HASH, USER_THEME, USER_NOTIFICATIONS_ENABLED)
user.display_full_user_details()

attempted_password_hash = "5f4dcc3b5aa765d61d8327deb882cf99" # placeholder hash for 'password'
authentication_result = user.auth.authenticate(attempted_password_hash)
print(f"Authentication successful: {authentication_result}")
