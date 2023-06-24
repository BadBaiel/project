from apps.users.models import User
from apps.mentors.models import Mentor


@receiver(post_save, sender=User)
def create_mentor(sender, instance, created, **kwargs):
    if created:
        Mentor.objects.create(user=instance, username=instance.username)