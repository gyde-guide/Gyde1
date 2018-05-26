from django.db import models
from django.contrib.auth.models import User



CREATE TABLE user ( id INT(11) NOT NULL AUTO_INCREMENT, first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(50), user_name VARCHAR(32), password VARCHAR(32), level ENUM('Teacher', 'Student'), user_roles ENUM('Client', 'Admin'), num_feedbacks INT(12), num_invites INT(12), num_sessions INT(12), num_days_since_last_visit INT(5), num_following INT(12), num_followers INT(12), PRIMARY KEY (id));



 claas User(models.Model):

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     user = models.IntegerField('User', blank=False)


#     SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
#     breed = models.CharField(max_length=30, blank=True)
#     description = models.TextField()
#     sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
#     submission_date = models.DateTimeField()
#     age = models.IntegerField(null=True)
#     vaccinations = models.ManyToManyField('Vaccine', blank=True)


# CREATE TABLE post ( id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(80), user_id INT(11), abstract TEXT, date_time DATETIME, logical FLOAT, practical FLOAT, creative FLOAT, significance FLOAT, difficulty FLOAT, num_endorses INT(12), num_shares INT(12), PRIMARY KEY (id));


# ID Title user_ID abstract attachments_list (column q) Tags_List Date Contributions List logical practical creative significance difficulty Endorse Share