import requests
from bs4 import BeautifulSoup
import openpyxl


def scrape_and_write_to_excel(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML response using BeautifulSoup4
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table containing the data
        table = soup.find('table')

        # Create a new Excel workbook and select the active sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Extract data from the table and write it to the Excel sheet
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            sheet.append([cell.get_text(strip=True) for cell in cells])

        # Save the workbook to the specified Excel file
        workbook.save("practitioners.xlsx")

        print("Data Saved")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


if __name__ == "__main__":
    # Specify the URL of the website
    website_url = "https://kmpdc.go.ke/Registers/General_Practitioners.php"
    # Call the function to scrape and write the data to Excel
    scrape_and_write_to_excel(website_url)