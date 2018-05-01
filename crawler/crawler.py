import requests
from bs4 import BeautifulSoup
from collections import Counter

class Crawler:
    """ Class To Implement The Page Scraping & Text Extraction Logic """

    @staticmethod
    def getText(url):
        """ 
        Function to fetch HTML from provided URL and scrape text contents
        from it.
        """
        pageHTML = requests.get(url)
        parsedContent = BeautifulSoup(pageHTML.content, 'html.parser')

        # Extract script and style tags right off the bat.
        for script in parsedContent(["script", "style"]):
            script.extract()

        textInPage = parsedContent.body.get_text()
        lines = (line.strip() for line in textInPage.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        formattedText = '\n'.join(chunk for chunk in chunks if chunk)

        return formattedText

    def getMostFrequentWords(text):
        pass