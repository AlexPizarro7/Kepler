from django.db import models

# Create your models here.
class Email_Address(models.Model):
      email_address_id = models.IntegerField(primary_key = True)
      email_address = models.CharField(max_length=128)

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.BigIntegerField()
    email_address_id = models.ForeignKey(Email_Address, db_column='email_address_id', on_delete=models.PROTECT)
    password_hash = models.CharField(max_length=1024)
    active = models.BooleanField()
    time_inserted = models.DateTimeField()
    time_updated = models.DateTimeField()


class Subscription_types(models.Model):
      subscription_type_id = models.IntegerField(primary_key = True)
      subscription_type_name = models.CharField(max_length=128)
      subscription_type_description = models.CharField(max_length=1024)
      price = models.FloatField()


class Subscription(models.Model):
        subscription_id = models.IntegerField(primary_key = True)
        customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
        start_time = models.DateTimeField()
        end_time = models.DateTimeField()
        subscription_type_id = models.ForeignKey(Subscription_types
                                                 , db_column='subscription_type_id'
                                                 , on_delete=models.PROTECT
                                                 ) # This is not needed, but as an example



class Subscription_Features(models.Model):
      subscription_features_id = models.IntegerField(primary_key = True)
      subscription_type_id = models.ForeignKey(Subscription_types, db_column='subscription_type_id', on_delete=models.CASCADE)
      feature_name = models.CharField(max_length=256)
      feature_description = models.CharField(max_length=1024)



class Mailing_List(models.Model):
      email_List_id = models.IntegerField(primary_key = True)
      customer_id = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
      email_address_id = models.ForeignKey(Email_Address, on_delete=models.PROTECT)
      active = models.BooleanField()
      subscribe_date = models.DateTimeField()
      unsubscribe_date = models.DateTimeField()


class Event(models.Model):
      event_id = models.IntegerField(primary_key = True)
      event_description = models.CharField(max_length=1024)
      start_time = models.DateTimeField()
      end_time = models.DateTimeField()
      notify = models.CharField(max_length=256)

class Event_Notifications(models.Model):
      event_notification_id = models.IntegerField(primary_key = True)
      event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
      email_list_id = models.ForeignKey(Mailing_List, db_column='email_list_id', on_delete=models.CASCADE)
      notification_time = models.DateTimeField()

