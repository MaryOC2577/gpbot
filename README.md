# **Project 7 - Create GrandPy Bot, the grandpa robot**

## **What does the program do ?**
The purpose of the program is to interact with Here Maps and Wikipedia APIS.
The application allows the user to display the address of a place, information about that place and its position on a map. 
Project monitoring is available [here](https://trello.com/b/xOVPbFJ8/granpy-bot).
The repository on GitHub is availiable [here](https://github.com/MaryOC2577/gpbot.git).
The application is available [here](https://gpbotoc.herokuapp.com/).

## **Requirements**
* Visual Studio Code version : 1.59.1
* Visual Studio Code dependencies : flake8, pylint, pydocstyle, black, pylance and mypy.
* Virtual environnement with venv module.
* Python version : 3.9.5
* Flask 2.0.1
* Gunicorn 20.1.0

## **Setup the program**
* Step 1
    * Open the project in Visual Studio Code.
* Step 2
    1. Create a virtual environment in the project by executing the following commands in the terminal.
    2. python -m venv .venv : 
    3. . .venv.Scripts.activate 
* Step 3
    * Run the command "flask run" on the terminal.
* Step 4
    * Open the browser with the adress : "http://localhost:5000".
* Step 5
    * the user enters his request in the text box and clicks on the button to validate it. 

## **How to use**
Enter a request in the text box and click on the button. GrandPy will display the location's address as well as information about it. GrandPy will also display the location on a map, visible with a marker. 
