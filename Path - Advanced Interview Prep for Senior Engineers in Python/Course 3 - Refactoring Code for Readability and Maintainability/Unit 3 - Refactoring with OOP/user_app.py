class Event:
    def __init__(self, name):
        self.name = name

class EventManager:
    def __init__(self):
        self.events = []

    def log_event(self, event):
        self.events.append(event)
        print(f"Event: {event.name}")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManager:
    def __init__(self):
        self.users = []
        self.event_manager = EventManager()

    def add_user(self, user):
        self.users.append(user)
        self.event_manager.log_event(Event(f"New user added: {user.username}"))

    def update_password(self, username, new_password):
        for user in self.users:
            if user.username == username:
                user.password = new_password
                self.event_manager.log_event(Event(f"Password change for user: {username}"))
                return
        print(f"User {username} not found")

    def display_user_info(self, username):
        for user in self.users:
            if user.username == username:
                print(f"Username: {username}")
                return
        print(f"User {username} not found")

    def remove_user(self, username):
        user_to_remove = next((user for user in self.users if user.username == username), None)
        if user_to_remove:
            self.users.remove(user_to_remove)
            self.event_manager.log_event(Event(f"User removed: {username}"))
        else:
            print(f"No user found with username: {username}")

# Example usage of the merged and non-refactored code
user_manager = UserManager()
user_manager.add_user(User("Alice123", "password1"))
user_manager.add_user(User("Bob456", "password2"))

user_manager.display_user_info("Alice123")
user_manager.update_password("Alice123", "new_password1")
user_manager.remove_user("Alice123")
user_manager.remove_user("UnknownUser")
