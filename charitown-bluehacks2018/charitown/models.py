from django.db import models

# Create your models here.


class Member(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fullName = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    aboutMe = models.CharField(max_length=200)
    birthdate = models.DateTimeField()
    totalAmountDonated = models.FloatField(default=0)


class Community(models.Model):
    publicMessage = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    establishedOn = models.DateTimeField()
    totalAmountDonated = models.FloatField(default=0)
    iconID = models.IntegerField(default=1)
    members = models.ManyToManyField(Member)


class Project(models.Model):
    iconID = models.IntegerField(default=1)
    totalAmountDonated = models.FloatField(default=0)
    maximumAmount = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    charity = models.CharField(max_length=200)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)


class ProjectDonation(models.Model):
    donor = models.ForeignKey(Member, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    totalAMountDonated = models.FloatField(default=0)










