Basic Flask Application README
=============================

This is a basic Flask application that returns personalized HTML responses based on the client's request URL. For example, when a client requests "localhost:5000/David", the application will return an HTML file with the text "Hello World David".

How to Run
----------

1. Open a terminal and navigate to the project directory.
2. Run the command `./run.sh` to install Python, install required packages, and start the Flask application.
3. Open a web browser and navigate to `http://localhost:5000/<Name>` to see the application in action, replace `<Name>` with your desired name.

Note: Make sure you have the necessary permissions to run the script and install packages.

Dependencies
-------------

This project requires the following dependencies to be installed:

* Flask
* Jinja2

These dependencies are listed in the `requirements.txt` file and can be installed by running the `run.sh` script.

Exposes
--------

* app.py: Main entry point for the Flask application. Handles incoming requests and returns personalized HTML responses.
* templates/index.html: Jinja2 template for displaying personalized 'Hello World' messages.

Note: You can find more information about each file in the project description.