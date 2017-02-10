### Context

This is a Demo Web Application that has a UI to visualize data about Hacker's genders & shirt sizes.

There are also 2 Http API endpoints that query data:
	1. '/hackers': Returns hacker check-in and check-out data as well as some other details. Returns a JSON object.
		- A request to the URL: '/hackers?school=school name here' will filter the data to produce JSON of only hackers from the named school
	2. '/shirts': Returns totals for hackers' genders and shirt sizes. Returns a JSON object.

This application was created using the Flask web framework. The data visualization was created using the Javascript Library Vis.js.

### Installation & Usage

1. Download the Zipped Project Folder. Unzip and extract it to desired location.

2. In terminal, proceed to the project directory.

3. The project has a Virtual Environment running Python 3.5 and Flask. While in the root directory of the project type: 'source venv/bin/activate'
	- Type 'deactivate' to deactivate the virtual environment.

4. Even though the project is created using a Virtual Environment, I always install all the dependencies just in case: 'pip install -r requirements.txt'

5. Everything should be ready now, so type: 'python run.py' to start the web application. In your browser navigate to 'localhost:5000'
