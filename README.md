# Airline Management System
Demonstration Video - https://drive.google.com/file/d/16NcQ3ho1ew5LFbIqxG4W9zlVdxccyHsO/view?usp=sharing
# Tools Required
- Python
- Django
# Steps to run the project
1. Firstly, Install Python and Django on your local machine.
2. Clone the project and navigate into the root directory of the project.
3. Open the terminal/cmd from the root directory.
4. Create a superuser for accessing the django admin panel. For that, run ```py manage.py createsuperuser``` and create an user.
5. Run ```py manage.py makemigrations``` and ```py manage.py migrate``` for updating the database with latest fields
6. Finally, Run ```py manage.py runserver``` for starting the server.
7. Open the browser and you can find the project is been served to ```localhost:8000/login/booking```
# Note
- If you get any module not found error, try installing the specific module using the command ```pip install <ModuleName>``` and restart the server again.
