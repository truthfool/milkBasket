# Steps to scrap data from milkbasket

## Installation Steps:

1. Create virtualenvironment using command `python -m venv ./milkbasketenv .`
2. Activate the virtual environment using `milkbasketenv/Scripts/activate`
3. Run `pip install -r requirements.txt`
4. Run the script using `python main.py`

## Walkthrough of code

1. I import the necessary libraries BeautifulSoup and selenium and the required modules from the selenium library: webdriver and FirefoxService.
2. I import the GeckoDriverManager module from webdriver_manager.firefox to manage the Firefox driver and set the path to the Firefox driver executable.
3. Created a Firefox service using the FirefoxService class, specifying the executable path.
4. Create a Firefox webdriver instance using the webdriver.Firefox class and passing the service.
5. Set the URL variable to "https://www.milkbasket.com/".
6. `driverFunction()` is the entry point of my code.
7. It calls scrapProductData() and this function navigates using the service driver to the products page and I store the html content in `html_doc` variable.
8. BeautifulSoup initialises object with the html content and returns it.
9. I call the getAllProducts() function to get all products in a list
10. I find all div tags which have class names as `all-products`.
11. It returns a list and I loop over all the products and extract their name,price,details,quantity,image url and append the dictionary to the list.
12. After looping over all the products I return the final list.
