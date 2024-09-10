from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from myapp.models import Profile

# Signal handler
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("Signal triggered: Creating profile...")
        Profile.objects.create(user=instance)  # This action should be rolled back if transaction fails

# Function to create a user and trigger signal
def create_user_with_transaction():
    try:
        with transaction.atomic():  # Begin a transaction
            print("Creating user inside transaction...")
            user = User.objects.create(username="testuser")
            # Simulate an error to trigger transaction rollback
            raise Exception("Something went wrong!")  # This will roll back the transaction
    except Exception as e:
        print(f"Transaction failed: {e}")

if __name__ == "__main__":
    create_user_with_transaction()
    
    # Check if the Profile was created
    profiles = Profile.objects.filter(user__username="testuser")
    print(f"Profiles created: {len(profiles)}")  # Should print 0 if rolled back
