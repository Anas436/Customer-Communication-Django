from django.db import models
# Create your models here.

class Customer(models.Model):
    """
    A Django model representing a customer in the customer360 project.

    Fields:
    - id: Auto-generated primary key for the customer.
    - name: CharField for storing the customer's name (max length 100 characters).
    - email: EmailField for storing the customer's email address (max length 100 characters).
    - phone: CharField for storing the customer's phone number (max length 20 characters).
    - address: CharField for storing the customer's address (max length 200 characters).
    - social_media: CharField for storing the customer's social media handle (max length 100 characters, optional).

    Methods:
    - __str__: Returns a string representation of the customer, using the ID.

    This model represents a customer with basic information such as name, email, phone, address, and an optional
    social media handle.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    social_media = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.id)

class Interaction(models.Model):
    """
    A Django model representing an interaction with a customer in the customer360 project.

    Fields:
    - customer: ForeignKey to the Customer model, representing the customer involved in the interaction.
    - channel: CharField with choices for different communication channels (phone, sms, email, letter, social media).
    - direction: CharField with choices for interaction direction (inbound or outbound).
    - interaction_date: DateField for storing the date of the interaction (auto-generated on creation).
    - summary: TextField for a summary or description of the interaction.

    This model tracks interactions between customers and the business, including the channel,
    direction, date, and a summary of the interaction.
    """
    CHANNEL_CHOICES = [
        ('phone', 'Phone'),
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('letter', 'Letter'),
        ('social_media', 'Social Media')
    ]

    DIRECTION_CHOICES = [
        ('inbound', 'Inbound'),
        ('outbound', 'Outbound'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    channel = models.CharField(max_length=15, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    interaction_date = models.DateField(auto_now_add=True)
    summary = models.TextField()
