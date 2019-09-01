from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# base custom user class which will extends the existing user via one to one relation
class YDL_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_email_activated = models.BooleanField(default=False)
    # skill --- skill category (e.g language, programming languages, hobbies)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.is_student:
            student = YDL_Student(user=self)
            student.save()
            # delete student if the user is no student anymore
            if hasattr(self, "student"):
                self.student.delete()
        
        if self.is_teacher:
            teacher = YDL_Teacher(user=self)
            teacher.save()
            if hasattr(self, "teacher"):
                self.teacher.delete()
    
    def __str__(self):
        return self.user.username

# create signals to use if a new django user is created. This event will be used to also create a
# YDL_User Class Instance
@receiver(post_save, sender=User)
def create_user_ydl_user(sender, instance, created, **kwargs):
    if created:
        YDL_User.objects.create(user=instance)
    else:
        instance.ydl_user.save()

# a student can have courses
class YDL_Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# a teacher does not have classes the teachers get assigned to courses
class YDL_Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)