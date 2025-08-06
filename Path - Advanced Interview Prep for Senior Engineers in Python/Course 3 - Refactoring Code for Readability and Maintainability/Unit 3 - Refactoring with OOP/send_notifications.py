# Notification class with separate methods for each notification type
class Notification:

    def send(self, message):
        pass

# Function to send notifications using specific methods based on type
def send_notifications(notifications, message):
    for notification in notifications:
        notification.send(message)

# Notification type classes just acting as placeholders for type checking
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")


class TextNotification(Notification):
    def send(self, message):
        print(f"Sending text message: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending push notification: {message}")


# List of notification objects
notifications = [
    EmailNotification(),
    TextNotification(),
    PushNotification()
]

# Sending a message through different types of notifications
send_notifications(notifications, "Your order has been shipped!")
