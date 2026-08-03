import scrapy

# print(dir(scrapy))
# ['Field', 'FormRequest', 'Item', 'Request', 'Selector', 'Spider', '__all__', '__builtins__',
# '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__',
# '__spec__', '__version__', 'exceptions', 'http', 'item', 'link', 'linkextractors',
# 'selector', 'signals', 'spiders', 'utils', 'version_info']

class BooksSpider(scrapy.Spider):
    name = "books"  # The name attribute of the class should always have a unique value.
    start_urls = [
        "http://books.toscrape.com"
    ]

    # def start_requests(self):
    #     return [
    #         scrapy.Request(url = "http://books.toscrape.com", callback = self.parse)  # Here, for the callback parameter, the parse is only passed / referenced, not invoked.
    #     ]

    def parse(self, response):  # It's the response given to the user.
        book_titles = response.css("article.product_pod h3 a::attr(title)").getall()

        with open("books.html", "wb") as file:  # The .html will be accessed in write and binary mode.
            file.write(response.body)
            
