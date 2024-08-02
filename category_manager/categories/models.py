from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.exceptions import ValidationError


class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    lft = models.PositiveIntegerField(default=0)
    rght = models.PositiveIntegerField(default=0)
    tree_id = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class CategorySimilarity(models.Model):
    category_a = models.ForeignKey(Category, related_name='similar_to', on_delete=models.CASCADE)
    category_b = models.ForeignKey(Category, related_name='similar_from', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('category_a', 'category_b')

    def clean(self):
        if self.category_a == self.category_b:
            raise ValidationError("Category A and Category B cannot be the same.")

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.category_a_id > self.category_b_id:
            self.category_a, self.category_b = self.category_b, self.category_a
        super().save(*args, **kwargs)
