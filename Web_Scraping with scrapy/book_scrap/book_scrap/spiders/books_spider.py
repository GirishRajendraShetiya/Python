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
        for entry in response.css("article.product_pod"):
            book_title = entry.css("h3 a::attr(title)").get()
            book_price = entry.css("div.product_price p.price_color::text").get()
            yield {"title": book_title, "price": book_price}

        
        # book_titles = response.css("article.product_pod h3 a::attr(title)").getall()  # Got it using the scrapy shell <website_url> command > response > response.css
        # book_price  = response.css("article.product_pod div.product_price p.price_color::text").getall()

        # for title in book_titles:
        #     yield {"title": title}  # To get the output in sections, instead of whole, hence "yield" is used.
            

        # with open("books.html", "wb") as file:  # The .html will be accessed in write and binary mode.
        #     file.write(response.body)
        
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url = next_page_url, callback = self.parse)
