from django.db import models

# This is created for fetching data from already existing models
class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    user_address = models.CharField(max_length=50, db_collation='utf8mb3_general_ci', blank=True, null=True)
    user_phno = models.CharField(max_length=20, db_collation='utf8mb3_general_ci', blank=True, null=True)
    user_email = models.CharField(max_length=30, blank=True, null=True)
    userprofile = models.TextField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    #Class for accessing records from DB table (user_details)
    class Meta:
        managed = False
        db_table = 'user_details'
    