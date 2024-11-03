from django.db import models

# Create your models here.


class ServiceTitle(models.Model):
    title =  models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.title
    


class Service(models.Model):
    service = models.ForeignKey(ServiceTitle, on_delete=models.CASCADE, blank=True, null=True)
    # name = models.CharField(max_length=150) 
    icon = models.ImageField(upload_to='icon/', blank=True, null=True)
    icon2 = models.ImageField(upload_to='icon2/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # return f"{self.service.title}
        return self.service.title
    
class Team(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)   
    designation = models.CharField(max_length=200, blank=True, null=True)    
    bio = models.TextField(blank=True, null=True) 
    # qrcode = models.ImageField(upload_to="qrcode", blank=True, null=True) 
    barcode = models.ImageField(upload_to="barcode", blank=True, null=True) 
    photo = models.ImageField(upload_to="team", blank=True, null=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)       

    # class Meta:
    #     ordering = ['member_name']     
        
    def __str__(self):
        return self.name      

