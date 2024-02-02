from django.db import models


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


class Profile(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    about_me = models.TextField()
    experience = models.IntegerField()
    completed_project = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='profiles',
                              default='profiles/avatar.svg')


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)


class Skills(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)


class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField()


class Testimonial(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='profiles',
                              default='testimonial/avatar.svg')
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    testimonial = models.TextField()


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)


class Project(models.Model):
    image = models.ImageField(upload_to='projetcts')
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    technology = models.CharField(max_length=10)
    url = models.CharField(max_length=10)
    image2 = models.ImageField(null=True, blank=True, upload_to='projetcts')
    link2 = models.CharField(max_length=100)


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)


class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog')
