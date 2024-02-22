from django.shortcuts import render
from datetime import date, timedelta
from django.db.models import Count
from . models import *

# Create your views here.

def index(request):
    # Retrieve all customers
    customers = Customer.objects.all()
    context = {"customers": customers}  # Create context for rendering template
    return render(request, "index.html", context=context)  # Render index.html with customer data

def create_customer(request):
    if request.method == "POST":
        # If form is submitted
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        social_media = request.POST["social_media"]

        # Create a new Customer object
        customer = Customer.objects.create(
            name=name, email=email, phone=phone, address=address, social_media=social_media
        )
        customer.save()  # Save the new customer
        msg = "Successfully Saved a Customer"  # Success message
        return render(request, "add.html", context={"msg": msg})  # Render add.html with success message

    return render(request, "add.html")  # Render the form if it's a GET request

def summary(request):
    thirty_days_ago = date.today() - timedelta(days=30)  # Date 30 days ago
    interactions = Interaction.objects.filter(interaction_date__gte=thirty_days_ago)  # Filter interactions in the last 30 days

    count = len(interactions)  # Total count of interactions
    interactions = interactions.values("channel", "direction").annotate(count=Count('channel'))  # Group and count interactions
    context = {
        "interactions": interactions,  # Pass interaction data to template
        "count": count  # Pass total count to template
    }
    return render(request, "summary.html", context=context)  # Render summary.html with interaction data

def interact(request, cid):
    # Get choices for channels and directions
    channels = Interaction.CHANNEL_CHOICES
    directions = Interaction.DIRECTION_CHOICES
    context = {"channels": channels, "directions": directions}  # Context for rendering template

    if request.method == "POST":
        # If form is submitted
        customer = Customer.objects.get(id=cid)  # Get customer by ID
        channel = request.POST["channel"]
        direction = request.POST["direction"]
        summary = request.POST["summary"]

        # Create a new Interaction object
        interaction = Interaction.objects.create(
            customer=customer,
            channel=channel,
            direction=direction,
            summary=summary
        )
        interaction.save()  # Save the new interaction
        context["msg"] = "Interaction Success"  # Success message
        return render(request, "interact.html", context=context)  # Render interact.html with success message

    return render(request, "interact.html", context=context)  # Render interact.html with form
