from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 


# CREATE TABLE user ( id INT(11) NOT NULL AUTO_INCREMENT, first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(50), user_name VARCHAR(32), password VARCHAR(32), level ENUM('Teacher', 'Student'), user_roles ENUM('Client', 'Admin'), num_feedbacks INT(12), num_invites INT(12), num_sessions INT(12), num_days_since_last_visit INT(5), num_following INT(12), num_followers INT(12), PRIMARY KEY (id));


#first_name, last_name, email, user_name, password 
LEVELCHOICES = ((1, _('Teacher')), (2, _('Student')))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(choices=LEVELCHOICES, default=2)
    user_roles = [('C', 'Client'), ('A', 'Admin')]
    num_feedbacks = models.IntegerField(null=True)
    num_invites = models.IntegerField(null=True)
    num_sessions = models.IntegerField(null=True)
    num_days_since_last_visit = models.IntegerField(null=True)
    num_followers = models.IntegerField(null=True)
    num_following = models.IntegerField(null=True)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save() 

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     user = models.IntegerField('User', blank=False)
    # postlist = OneToManyField('Post', blank=True)


#     SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
#     breed = models.CharField(max_length=30, blank=True)
#     description = models.TextField()
#     sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
#     submission_date = models.DateTimeField()
#     age = models.IntegerField(null=True)
#     vaccinations = models.ManyToManyField('Vaccine', blank=True)


# CREATE TABLE post ( id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(80), user_id INT(11), abstract TEXT, date_time DATETIME, logical FLOAT, practical FLOAT, creative FLOAT, significance FLOAT, difficulty FLOAT, num_endorses INT(12), num_shares INT(12), PRIMARY KEY (id));


# ID Title user_ID abstract attachments_list (column q) Tags_List Date Contributions List logical practical creative significance difficulty Endorse Share