import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, created, **kwargs):
    print("Signal received. Processing...")
    time.sleep(5)  # Simulate delay of 5 seconds
    print("Signal processing complete.")

# Test function
def create_user():
    print("Creating user...")
    user = User.objects.create(username="testuser")
    print("User created.")

if __name__ == "__main__":
    create_user()
