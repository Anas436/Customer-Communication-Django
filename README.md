# Customer-Communication-Django

Customer360 is a Django web application for managing customer information and interactions. It allows users to create new customers, record interactions, and view summaries of recent interactions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer360.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations to set up the database:
   ```bash
   python manage.py migrate
   ```
4. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the application at http://localhost:8000/ and the admin panel at http://localhost:8000/admin/.


## Demo

![](https://github.com/Anas436/Customer-Communication-Django/blob/main/photos/1.launch.png)
<hr>

![](https://github.com/Anas436/Customer-Communication-Django/blob/main/photos/2.add-new-customer.png)
<hr>

![](https://github.com/Anas436/Customer-Communication-Django/blob/main/photos/3.landing-page.png)
<hr>

![](https://github.com/Anas436/Customer-Communication-Django/blob/main/photos/4.interaction-details.png)
<hr>

![](https://github.com/Anas436/Customer-Communication-Django/blob/main/photos/5.summary.png)
   
## Usage

### Admin Panel
- Use the Django admin panel to manage customers and interactions.
- Create new customers, record interactions, and view summary reports.

### URLs
- Home: `/ `- Displays a list of customers with the option to interact with them.
- New Customer: `/create/` - Form to add a new customer.
- Interact: `/interact/<customer_id>/` - Form to interact with a specific customer.
- Summary: `/summary/` - View recent interaction summaries.
  
### Project Structure
- `customer360/`: Django project directory.
  - `settings.py`: Django settings for the project.
  - `urls.py`: URL configurations for routing.
- `customers/`: Django app for customer management.
  - `models.py`: Defines Customer and Interaction models.
  - `views.py`: Contains view functions for handling requests.
  - `templates/`: HTML templates for rendering pages.
  - `static/`: Static files (CSS, JS, etc.).
- `manage.py`: Django's command-line utility for administrative tasks.

## Models

### Customer
- Represents a customer with basic information.
- Fields:
  - `id`: Auto-generated primary key.
  - `name`: Name of the customer.
  - `email`: Email address of the customer.
  - `phone`: Phone number of the customer.
  - `address`: Address of the customer.
  - `social_media`: (Added in migration) Social media handle of the customer.
    
### Interaction
- Represents an interaction with a customer.
- Fields:
  - `id`: Auto-generated primary key.
  - `customer`: ForeignKey to Customer model.
  - `channel`: Communication channel (phone, sms, email, letter, social media).
  - `direction`: Direction of interaction (inbound, outbound).
  - `interaction_date`: Date of the interaction.
  - `summary`: Summary of the interaction. 
