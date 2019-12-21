from django.db import models
import math

# Create your models here.
class Material_detail(models.Model):
    name = models.CharField(max_length=30, null=True)
    year_demand = models.PositiveIntegerField(blank=True, null=True)
    holding_cost = models.PositiveIntegerField(blank=True, null=True)
    ordering_cost = models.PositiveIntegerField(blank=True, null=True)
    usage_rate = models.PositiveIntegerField(blank=True, null=True)
    lead_time = models.PositiveIntegerField(blank=True, null=True)
    eoq = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        blank=True, null=True
    )
    rop = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.eoq = math.sqrt(2 * self.year_demand * self.ordering_cost / self.holding_cost)
        self.rop = self.usage_rate * self.lead_time
        super(Material_detail, self).save(*args, **kwargs)


class Material(models.Model):
    number = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, null=True)
    inventory = models.PositiveIntegerField(blank=True, null=True)
    safety_stock =  models.PositiveIntegerField(blank=True, null=True)
    material_detail = models.ForeignKey(Material_detail, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    number = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, null=True)
    inventory = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    safety_stock =  models.PositiveIntegerField(blank=True, null=True)
    materials_required = models.ManyToManyField(Material, blank=True)
    year_demand = models.PositiveIntegerField(blank=True, null=True)
    holding_cost = models.PositiveIntegerField(blank=True, null=True)
    setup_cost = models.PositiveIntegerField(blank=True, null=True)
    produce_rate = models.PositiveIntegerField(blank=True, null=True)
    usage_rate = models.PositiveIntegerField(blank=True, null=True)
    lead_time = models.PositiveIntegerField(blank=True, null=True)
    epq = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        blank=True, null=True
    )

    def getComponents(self):
        return self.materials_required.all()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.epq = math.sqrt((2 * self.year_demand * self.setup_cost * self.produce_rate) / (self.holding_cost * (self.produce_rate - self.usage_rate)))
        super(Product, self).save(*args, **kwargs)
