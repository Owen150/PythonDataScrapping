<h1>Task</h1>
Write a Python script that scrapes data from https://kmpdc.go.ke/Registers/General_Practitioners.php and writes it into an Excel file.<br>
<h2>Prerequisite</h2>
Ensure that you have Python installed on your local machine.<br>
<h2>Libraries and Installation Steps</h2>
1. Import the requests library to fetch the HTML content of the webpage by running: pip install requests<br>
2. Import BeautifulSoup for parsing the HTML response body from the webpage by running: pip install beautifulsoup4<br>
3. For writing the parsed response to an Excel file, I used the openpyxl library by running: pip install openpyxl<br>

<h3>To replicate the project, follow these steps:</h3>

I. Clone the repository using the following command: <br>
git clone [url from github, either http or ssh] <br>
II. Change directories to your cloned project: <br>
cd PythonDataScrapping<br>
III. Open your project using your preferred IDE <br>
IV. Install the dependencies in the requirements.txt file: <br>
pip install -r requirements.txt<br>
V. Run the application by typing in the command:<br>
python3 datascrapping.py
