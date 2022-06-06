from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    service_type = models.ForeignKey(
        "ServiceCategory", on_delete=models.CASCADE, null=True, blank=True
    )
    description = RichTextField()
    requirement_dockument = RichTextField()
    orgination = models.CharField(max_length=255)
    responsible_person = models.CharField(max_length=255)
    legal_basis = models.TextField()
    contact_number = models.CharField(max_length=50)
    extra_phone_number = models.CharField(max_length=50, null=True, blank=True)
    tg_link = models.CharField(max_length=60, null=True, blank=True)
    is_free = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "service"
        ordering = ["-created_at"]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    icon = models.ImageField(upload_to="service_category/", null=True, blank=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "service_category"
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name


# class ServiceRating(models.Model):
#     service = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     status = models.BooleanField(default=True)
#     create_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.service.name
