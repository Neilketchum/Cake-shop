from django.db import models

# Create your models here.
class Product(models.Model):
	"""docstring for Products"""
	product_id = models.AutoField
	products_name  = models.CharField(max_length = 50)
	category = models.CharField(max_length = 50,default="")
	price = models.IntegerField()
	desc = models.CharField(max_length = 300)
	pub_date = models.DateField()
	image = models.ImageField(upload_to = "shop/images",default = "")

	def __str__(self):
		return self.products_name