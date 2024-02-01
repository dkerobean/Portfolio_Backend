from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    about_me = models.TextField()
    experience = models.IntegerField()
    completed_project = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='profiles',
                              default='profiles/avatar.svg')


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    availability = models.CharField(max_length=100)
    twitter = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    github = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    google_location = models.CharField(max_length=150)


class Skills(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)


class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField()


class Tesimonial(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='profiles',
                              default='testimonial/avatar.svg')
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    testimonial = models.TextField()
