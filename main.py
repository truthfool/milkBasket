# Link To Github URL : https://github.com/truthfool/milkBasket

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import os
import logging

load_dotenv()

_logger = logging.getLogger(__name__)

driver_path = "path/to/your/driver"
service = FirefoxService(executable_path=GeckoDriverManager().install())

driver = webdriver.Firefox(service=service)

URL = os.environ.get("URL")


def getAllProducts(soup):
    try:
        products_list = soup.find_all(
            "div", {"class": "all-products"}
        )  # Returns a list
    except BaseException as e:
        _logger.info(e)

    products = []
    for product in products_list:
        productName = product.find("div", {"class": "product-name"}).text.strip()
        productPrice = product.find("div", {"class": "price"}).text.strip()
        productDetails = product.find("div", {"class": "product-details"}).text.strip()
        productQuantity = product.find("div", {"class": "quantity"}).text.strip()
        productImage = product.find("img", {"class": "product-image"})["src"]
        products.append(
            {
                "name": productName,
                "price": productPrice,
                "details": productDetails,
                "quantity": productQuantity,
                "image": productImage,
            }
        )
    return products


def scrapProductData():
    all_products_url = URL + "products"
    try:
        service.get(all_products_url)
        # Scraping the product data
        html_doc = service.page_source
        soup = BeautifulSoup(html_doc, "html.parser")
        return soup
    except BaseException as e:
        _logger.info(e)


def driverFunction():
    soup = scrapProductData()
    try:
        productsList = getAllProducts(soup)
        return productsList
    except BaseException as e:
        _logger.info(e)


if __name__ == "__main__":
    driverFunction()
