import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Signal handler to check the thread identity
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, created, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")  # Thread ID of signal handler
    print(f"Signal handler thread name: {threading.current_thread().name}")  # Thread name

# Function to create a user and check the thread identity
def create_user():
    print(f"Caller thread ID: {threading.get_ident()}")  # Thread ID of the caller
    print(f"Caller thread name: {threading.current_thread().name}")  # Thread name
    
    # Create a user (this will trigger the post_save signal)
    user = User.objects.create(username="testuser")

if __name__ == "__main__":
    create_user()
