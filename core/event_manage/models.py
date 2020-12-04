from django.db import models
from novav1.models import Clinc , DoctorIn , pricing ,Patient ,Branch

# Create your models here.


class Events(models.Model):
    event_id        = models.AutoField(primary_key=True)
    #event_name      = models.CharField(max_length=255,null=True,blank=True)
    event_name      = models.ForeignKey("novav1.Patient",  on_delete=models.CASCADE,null=True,blank=True)
    start_date      = models.DateTimeField(null=True,blank=True)
    end_date        = models.DateTimeField(null=True,blank=True)
    event_type      = models.CharField(max_length=10,null=True,blank=True)
    allDay          = models.BooleanField(default=False)
    url             = models.URLField( max_length=200,null=True,blank=True)
    backgroundColor = models.CharField(max_length=50,null=True,blank=True)
    borderColor     = models.CharField(max_length=50,null=True,blank=True)
    arrive          = models.BooleanField(default=False)
    arrivetime      = models.DateTimeField(null=True,blank=True)  
    arrivetime2     = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    start           = models.BooleanField(default=False)
    start_session   = models.DateTimeField(null=True,blank=True)
    end             = models.BooleanField(default=False)
    session_end     = models.DateTimeField(null=True,blank=True)
    session_clinic  = models.ForeignKey("novav1.Clinc",  on_delete=models.CASCADE,blank=True, null=True)
    session_doctor  = models.ForeignKey("novav1.DoctorIn",  on_delete=models.CASCADE,blank=True, null=True)
    session_area    = models.ForeignKey("novav1.pricing",  on_delete=models.CASCADE,blank=True, null=True)
    session_used_balls= models.IntegerField(blank=True, null=True)
    session_branch= models.ForeignKey("novav1.Branch", on_delete=models.CASCADE,blank=True, null=True)
    





    def __str__(self):
        return str(self.event_name)


# class Events(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255,null=True,blank=True)
#     start = models.DateTimeField(null=True,blank=True)
#     end = models.DateTimeField(null=True,blank=True)

#     def __str__(self):
#         return self.name        




class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)




