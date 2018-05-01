import requests
from bs4 import BeautifulSoup
from collections import Counter

class Crawler:
    """ Class To Implement The Page Scraping, Text Extraction & Word Frequency Calculation Logic """

    @staticmethod
    def getText(url):
        """ 
        Function to fetch HTML from provided URL and scrape text contents
        from it.
        """
        pageHTML = requests.get(url)
        parsedContent = BeautifulSoup(pageHTML.content, 'html.parser')

        # Extract script, link and style tags right off the bat.
        for script in parsedContent(["script", "style", "link"]):
            script.extract()

        textInPage = parsedContent.body.get_text()

        return textInPage

    @staticmethod
    def getMostFrequentWords(text, n):
        """
        Calculate the frequency of all words in the text and return 
        the n words that occur most frequently, with their frequencies.
        """
        words = Counter()
        words.update(text.split())
        mostFrequentWords = words.most_common()
        
        return mostFrequentWords[:n]
        