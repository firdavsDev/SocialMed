from django.db import models


# Maps model
class Maps(models.Model):
    category = models.ForeignKey(
        "CategoryofMaps", on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=50)
    address_description = models.CharField(max_length=100)
    address_link = models.CharField(max_length=500)
    subway_address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "maps"
        ordering = ["-created_at"]
        verbose_name = "Map"
        verbose_name_plural = "Maps"

    def __str__(self):
        return self.name


# Choice category
class CategoryofMaps(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "category_of_maps"
        verbose_name = "Choice Category of Map"
        verbose_name_plural = "Choice Categories of Maps"

    def __str__(self):
        return self.name
