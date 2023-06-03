# Twitter-Data-Extraction-Project

This program is a simple data scraping tool that uses Selenium and Tkinter libraries to retrieve Twitter data. The program prompts the user to enter a Twitter username, password, and a topic. Then, it uses the entered user credentials to log in and navigate to Twitter using Selenium.

First, we initiate a Chrome session using the webdriver class of Selenium and open the login page of Twitter. Then, we use XPATH expressions to locate the necessary login input fields and buttons. While entering the username and password, Selenium checks the page to find the required fields. If the fields cannot be found, it displays an error message and terminates the program.

After the login process is completed, we start the data scraping process using the find_element and find_elements methods of Selenium. First, we enter the topic into the search area of Twitter to search for it and press the ENTER key. Then, we scroll to the end of the page to load more tweets. We achieve this using a while loop where, in each iteration, we scroll to the end of the page and check if new tweets are loaded. If no new tweets are loaded, we exit the loop.

Once all the tweets are retrieved, we save them to a text file. We create a text file with the same name as the entered topic, followed by the .txt extension. Then, while writing each tweet to the file, we number them using numbers.

Finally, we close the browser and terminate the program.

This way, the program uses the Twitter username and password entered by the user to retrieve the data and saves it to a text file.
