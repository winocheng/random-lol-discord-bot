import requests
from bs4 import BeautifulSoup

TIER = {
    '#E84057': 'OP',
    '#0093FF': '1',
    '#00BBA3': '2',
    '#FFB900': '3',
    '#9AA4AF': '4',
    '#A88A67': '5'
}


def getChampList(position):
    # URL of the website to scrape
    url = f'https://www.op.gg/champions?position={position}'
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Find the title of the page
        ranking_table = soup.find('caption', string='Ranking Table').find_parent('table')

        champion_list = list()
        if ranking_table:        
            # Optionally, extract and print data from the table
            headers = [th.get_text(strip=True) for th in ranking_table.find_all('th')]
            rows = ranking_table.find('tbody').find_all('tr')
            
            for row in rows:
                cells = row.find_all(['td', 'th'])
                row_data = [cell.get_text(strip=True) for cell in cells]

                if len(row_data) > 1 and row_data[1]: 
                    colorCode = row.find('g').path['fill']
                    champion_list.append([row_data[1], TIER[colorCode]]) 
            return(champion_list)
        else:
            raise Exception('Ranking Table not found.')
    else:
        raise Exception(f'Failed to retrieve the page. Status code: {response.status_code}')


