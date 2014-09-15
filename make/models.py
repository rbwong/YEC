from django.db import models


class Make(models.Model):
    first_name1 = models.CharField(max_length=50)
    middle_name1 = models.CharField(max_length=50)
    last_name1 = models.CharField(max_length=50)
    email1 = models.CharField(max_length=80)
    phone1 = models.CharField(max_length=80)
    sid1 = models.CharField(max_length=50)
    school1 = models.CharField(max_length=80)
    year_level1 = models.CharField(max_length=10)
    course1 = models.CharField(max_length=40)
    id_pic1 = models.ImageField(upload_to="photos")
    first_name2 = models.CharField(max_length=50, null=True)
    middle_name2 = models.CharField(max_length=50, null=True)
    last_name2 = models.CharField(max_length=50, null=True)
    email2 = models.CharField(max_length=80)
    phone2 = models.CharField(max_length=80)
    sid2 = models.CharField(max_length=50, null=True)
    school2 = models.CharField(max_length=80, null=True)
    year_level2 = models.CharField(max_length=10, null=True)
    course2 = models.CharField(max_length=10, null=True)
    id_pic2 = models.ImageField(upload_to="photos", null=True)

    app_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=600)
    app_market = models.CharField(max_length=100)
    concept = models.CharField(max_length=1000)


    def __unicode__(self):
        return self.id

    def admin_image1(self):
        return '<img width="100px" src="http://yec.upce.net/static/media/%s"/>' % self.id_pic1

    def admin_image2(self):
        return '<img width="100px" src="http://yec.upce.net/static/media/%s"/>' % self.id_pic2

    admin_image1.allow_tags = True
    admin_image2.allow_tags = True
