<h1>Task Description</h1>
Write a Python script that scrapes data from https://kmpdc.go.ke/Registers/General_Practitioners.php and writes it into an Excel file.<br>
<h2>Prerequisites</h2>
Ensure that you have Python version 3 or above installed on your local PC. You can check this by running the command <b>python -v</b><br>
<h2>Libraries and Dependencies</h2>
1. Import the requests library which is used to fetch the HTML content of the webpage by running <b>pip install requests</b><br><br>
2. Import the BeautifulSoup library from the bs4 package for parsing the HTML response body from the webpage by running <b>pip install beautifulsoup4</b><br><br>
3. For writing the parsed response from beautifulsoup4 to a Work Book/Excel sheet, I used the openpyxl library by running the <b>pip install openpyxl</b> command.<br>

<h3>Installation Guide</h3>
I. Clone the github repository using the following command: <br>
<b>git clone [url from github]</b><br><br>
II. Change directories to your cloned project: <br>
cd PythonDataScrapping<br><br>
III. Open your project using your preferred IDE <br><br>
IV. Install the dependencies in the requirements.txt file: <br><br>
pip install -r requirements.txt<br><br>
V. Start the application by running the command:<br>
python3 datascrapping.py
