# 3300_Project
Semester Project for 3300 Summer Class

(c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna

## Software License
The code in this project is licensed under the GNU Affero General Public License (AGPLv3). You may obtain a copy of the AGPLv3 license at <https://www.gnu.org/licenses/agpl-3.0.en.html>.

## Data Attribution
This project uses weather data from Open-Meteo (<https://open-meteo.com/>), licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). You can view the license at <https://creativecommons.org/licenses/by/4.0/>. 

Adaptations to the data were made as follows: [describe any modifications made, if applicable].

The original data can be accessed at <https://open-meteo.com/>.

# 3300_Project
Semester Project for 3300 Summer Class

<<How to run our software on a Windows device>>
<<1. Open Command Prompt>>
•	Press Win + R, type cmd, and press Enter.

<<2. Navigate to Your Project Directory>>
•	Use the cd command to change to the directory where your Django project is located. For example:
cd path\to\your\project

<<3. Create a Virtual Environment>>
•	If you haven't already created a virtual environment, you can do so with the following command (replace “env” with whatever you wish to name your environment):
python -m venv env

<<4. Activate the Virtual Environment>>
•	Activate the virtual environment with the following command:
.\env\Scripts\activate

<<5. Install Django>>
•	If Django is not already installed in your virtual environment, install it with:
pip install django

<<6. Run the Django Development Server>>
•	Start the Django development server with:
python manage.py runserver

