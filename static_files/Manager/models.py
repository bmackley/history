from django.db import models
from django.conf import settings
import decimal, datetime #decimal is not float or integer.  Always import this.  Do f=decimal.Decimal(50)
from django.contrib.auth.models import AbstractUser


class Info():
	def __init__(self, key, value, edit):
		self.key = key
		self.value = value
		self.edit = edit

# Create your models here.
class stores(models.Model):
	'''A store object'''
	active = models.NullBooleanField(blank=True, null=True)
	#manager= models.ForeignKey(User, related_name="managed_stores") #this is how this is referenced in other tables.  Hence the stores that the manager manages
	locationName = models.TextField(blank=True, null=True)
	street = models.TextField(blank=True, null=True)
	city = models.TextField(blank=True, null=True)
	state = models.TextField(blank=True, null=True)
	zipcode =  models.TextField(blank=True, null=True)
	phone = models.TextField(blank=True, null=True)


	def __str__(self):
		return '%s %s %s %s %s %s %s' % (self.locationName, self.street, self.city, self.state, self.zipcode, self.phone, self.active)

class User(AbstractUser):
	#inherited from AbstractUser:
	#first_name
	#last_name
	#username
	#email
	#is_active
	#is_staff
	#date_joined
	#password?
	#lusername = models.TextField(blank = True, null=True)
	address = models.TextField(blank=True, null=True)
	city = models.TextField(blank=True, null=True)
	state = models.TextField(blank=True, null=True)
	zipcode =  models.TextField(blank=True, null=True)
	phone = models.TextField(blank=True, null=True)
	dateOfBirth = models.DateField(blank = True, null=True)
	gender = models.TextField(blank = True, null=True)
	weight = models.DecimalField(blank = True, null=True, decimal_places=2, max_digits=6)
	height = models.PositiveSmallIntegerField(blank = True, null=True)
	def __str__(self):
		return self.username

class Group(models.Model):
	'''Groups added by Users'''
	groupName = models.TextField(blank = True, null=True)
	lgroupName = models.TextField(blank = True, null=True)
	administrator = models.ForeignKey(User, null=True, blank=True)
	city = models.TextField(blank = True, null=True)
	lcity = models.TextField(blank = True, null=True)
	state = models.TextField(blank = True, null=True)
	zipcode = models.TextField(blank = True, null=True)
	phone = models.TextField(blank=True, null=True)
	members = models.ManyToManyField(User, through='Membership', related_name= 'group_member' )
	def __str__(self):
		return self.groupName

class Membership(models.Model):
	member = models.ForeignKey(User)
	group = models.ForeignKey(Group, related_name= 'user_group', null=True, blank=True,)
   	

class Weight(models.Model):
	'''Groups a User is associated with'''
	user = models.ForeignKey(User, null=True, blank=True, related_name= 'user_weigh_in')
	weight = models.DecimalField(blank = True, null=True, decimal_places=2, max_digits=6)
	dateWeighed = models.DateTimeField(auto_now_add = True)
	weightLost = models.DecimalField(blank = True, null=True, decimal_places=2, max_digits=6, default=0.00)








class catalogProductCategories(models.Model):
	'''options for catalog product dropdown'''
	active = models.NullBooleanField(blank=True, null=True)
	name = models.TextField(blank=True, null=True)
	url = models.TextField(blank=True, null=True)
	queryURL = models.TextField(blank=True, null=True)
	imagePath = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name

class catalogProduct(models.Model):
	'''Catalog Inventory Products'''
	active = models.NullBooleanField(blank=True, null=True)
	catalogProductID = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	brand = models.TextField(blank=True, null=True)
	lcatalogProductID = models.TextField(blank=True, null=True)
	ldescription = models.TextField(blank=True, null=True)
	lbrand = models.TextField(blank=True, null=True)
	category = models.ForeignKey(catalogProductCategories)
	imagePath = models.TextField(blank=True, null=True)
	price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
	rentalPrice = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
	replacementPrice = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
	def __str__(self):
		return self.catalogProductID
class serializedProduct(models.Model):
	'''Serialized Inventory Products'''
	active = models.NullBooleanField(blank=True, null=True)
	catalogProductID = models.ForeignKey(catalogProduct)
	serialNumber = models.TextField(blank=True, null=True)
	datePurchased = models.DateField(blank=True, null=True)
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	storeLocation = models.TextField(blank=True, null=True)
	isRental = models.NullBooleanField(blank=True, null=True)
	isAvailable = models.NullBooleanField(blank=True, null=True)
	isNew = models.NullBooleanField(blank=True, null=True)
	dateSold = models.DateField(blank=True, null=True)
class stockedProduct(models.Model):
	'''Stocked Products'''
	active = models.NullBooleanField(blank=True, null=True)
	catalogProductID = models.ForeignKey(catalogProduct)
	amount = models.PositiveIntegerField()
	cost = models.DecimalField(max_digits=10, decimal_places=2)
	store = models.ForeignKey(stores)



class UserShipping(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=20, blank=True, null=True)
	street = models.CharField(max_length=20, blank=True, null=True)
	city =  models.CharField(max_length=20, blank=True, null=True)
	state =  models.CharField(max_length=20, blank=True, null=True)
	zipcode =  models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.user.username + ": " + self.name

	def customer(self):
		info = []
		info.append(Info("Name", self.name, False))
		info.append(Info("Street", self.street, True))
		info.append(Info("City", self.city, True))
		info.append(Info("State", self.state, True))
		info.append(Info("Zipcode", self.zipcode, True))
		return info	

class CardType(models.Model):
	name = models.CharField(max_length=20, blank=True, null=True)
	def __str__(self):
		return self.name 
class UserBilling(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=20, blank=True, null=True)
	cardtype = models.ForeignKey(CardType)
	number = models.CharField(max_length=20, blank=True, null=True)
	security = models.CharField(max_length=20, blank=True, null=True)
	street = models.CharField(max_length=20, blank=True, null=True)
	city =  models.CharField(max_length=20, blank=True, null=True)
	state =  models.CharField(max_length=20, blank=True, null=True)
	zipcode =  models.CharField(max_length=20, blank=True, null=True)

class ShippingOption(models.Model):
	daystoarrive = models.PositiveIntegerField()
	price = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)


class TransactionType(models.Model):
	transactiontype = models.CharField(max_length=20, blank=True, null=True)
	def __str__(self):
		return self.transactiontype 

class Transaction(models.Model):
	buyer = models.ForeignKey(User)
	seller = models.ForeignKey(User, limit_choices_to={'is_staff': True}, related_name="trans_seller")
	transactiontype = models.ForeignKey(TransactionType)
	shipping = models.ForeignKey(UserShipping)
	billing = models.ForeignKey(UserBilling)
	shippingoption = models.ForeignKey(ShippingOption)
	subtotal = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
	taxAmount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return str(self.date) + " | " + self.buyer.username + " | " + self.seller.username + " | " + str(self.subtotal)

class TaxRates(models.Model):
	state =  models.CharField(max_length=20, blank=True, null=True)
	taxRate = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=3)

class JournalEntry(models.Model):
	transaction = models.ForeignKey(Transaction)
	note =  models.CharField(max_length=1000, blank=True, null=True)

class Subledger(models.Model):
	type =  models.CharField(max_length=1000, blank=True, null=True)
	def __str__(self):
		return self.type
class DebitCredit(models.Model):
	journalentry = models.ForeignKey(JournalEntry)
	subledger = models.ForeignKey(Subledger)
	isDebit = models.NullBooleanField()
	amount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)

class GeneralLedger(models.Model):
	date = models.DateTimeField(auto_now_add=True, blank=True)
	subledger = models.ForeignKey(Subledger)
	isDebit = models.NullBooleanField()
	amount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
class Commission(models.Model):
	transaction = models.ForeignKey(Transaction)
	seller = models.ForeignKey(User, limit_choices_to={'is_staff': True}, related_name="trans_seller_commission")
	amount = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
	paid = models.NullBooleanField()

