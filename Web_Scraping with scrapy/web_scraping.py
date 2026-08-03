# Using a programming language to access a website, download it's content & parse the relevant data.
# The scrapy module in Python is used. To install, pip install scrapy

# To validate if scrapy has been installed properly, run "scrapy" in the terminal.
# To create a scrap project: scrapy startproject <project_name>

# A folder with the project_name is created within the same parent directory where the above command is executed.
# The folder contains several configuration files (__init__, items, middlewares, pipelines, settings, scrapy.cfg),
# also a sub-folder /spiders having another __init__.py file.

# A spider folder in a scrapy project is the specific directory where you store all your individual Python spider files.
# It acts as the central workspace for defining how different websites are crawled and parsed.

# scrapy crawl <spider_name_specified_in_the_class> - To crawl / extract the data from a website.

# scrapy shell <website_url> - To fetch the contents of the website's HTML.

# In [1]: response
# Out[1]: <200 http://books.toscrape.com>

# In [2]: type(response)
# Out[2]: scrapy.http.response.html.HtmlResponse

# In [3]: response.css("a")
# Out[3]: [<Selector query='descendant-or-self::a' data='<a href="index.html">Books to Scrape</a>'>,
#  <Selector query='descendant-or-self::a' data='<a href="index.html">Home</a>'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books_1/i...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/tra...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/mys...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/his...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/seq...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/cla...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/phi...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/rom...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/wom...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/fic...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/chi...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/rel...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/non...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/mus...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/def...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/sci...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/spo...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/add...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/fan...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/new...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/you...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/sci...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/poe...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/par...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/art...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/psy...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/aut...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/par...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/adu...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/hum...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/hor...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/his...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/foo...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/chr...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/bus...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/bio...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/thr...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/con...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/spi...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/aca...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/sel...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/his...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/chr...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/sus...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/sho...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/nov...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/hea...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/pol...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/cul...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/ero...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/category/books/cri...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/a-light-in-the-att...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/a-light-in-the-att...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/tipping-the-velvet...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/tipping-the-velvet...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/soumission_998/ind...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/soumission_998/ind...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/sharp-objects_997/...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/sharp-objects_997/...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/sapiens-a-brief-hi...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/sapiens-a-brief-hi...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-requiem-red_99...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-requiem-red_99...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-dirty-little-s...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-dirty-little-s...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-coming-woman-a...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-coming-woman-a...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-boys-in-the-bo...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-boys-in-the-bo...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-black-maria_99...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/the-black-maria_99...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/starving-hearts-tr...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/starving-hearts-tr...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/shakespeares-sonne...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/shakespeares-sonne...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/set-me-free_988/in...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/set-me-free_988/in...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/scott-pilgrims-pre...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/scott-pilgrims-pre...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/rip-it-up-and-star...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/rip-it-up-and-star...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/our-band-could-be-...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/our-band-could-be-...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/olio_984/index.htm...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/olio_984/index.htm...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/mesaerion-the-best...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/mesaerion-the-best...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/libertarianism-for...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/libertarianism-for...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/its-only-the-himal...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/its-only-the-himal...'>,
#  <Selector query='descendant-or-self::a' data='<a href="catalogue/page-2.html">next</a>'>]

# In [4]: type(response.css("a"))
# Out[4]: scrapy.selector.unified.SelectorList

# In [6]: len(response.css("a"))
# Out[6]: 94

# In [7]: response.css("article")
# Out[7]: To get all the "article" tags

# In [9]: len(response.css("article"))
# Out[9]: 20

# In [7]: response.css("article.product_pod")
# Out[7]: To get all the elements within the article > product_pod class
# The name of the class given should be accurate, even a single change will ruin the output. 

# To get all the child, keep a space between the element.class and the child's element name: article.product_pod h3
# In [13]: response.css("article.product_pod h3")
# Out[13]: [<Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/a-light-in-the...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/tipping-the-ve...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/soumission_998...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/sharp-objects_...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/sapiens-a-brie...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/the-requiem-re...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/the-dirty-litt...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/the-coming-wom...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/the-boys-in-th...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/the-black-mari...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/starving-heart...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/shakespeares-s...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/set-me-free_98...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/scott-pilgrims...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/rip-it-up-and-...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/our-band-could...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/olio_984/index...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/mesaerion-the-...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/libertarianism...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3" data='<h3><a href="catalogue/its-only-the-h...'>]

# To extract all the a tags within the h3 tag, which are within the article tag with class as "product_pod"
# In [14]: response.css("article.product_pod h3 a")
# Out[14]: [<Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/a-light-in-the-att...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/tipping-the-velvet...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/soumission_998/ind...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/sharp-objects_997/...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/sapiens-a-brief-hi...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/the-requiem-red_99...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/the-dirty-little-s...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/the-coming-woman-a...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/the-boys-in-the-bo...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/the-black-maria_99...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/starving-hearts-tr...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/shakespeares-sonne...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/set-me-free_988/in...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/scott-pilgrims-pre...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/rip-it-up-and-star...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/our-band-could-be-...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/olio_984/index.htm...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/mesaerion-the-best...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/libertarianism-for...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a" data='<a href="catalogue/its-only-the-himal...'>]

# To extract the text from the a tag, use ::text
# In [15]: response.css("article.product_pod h3 a::text")
# Out[15]: [<Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='A Light in the ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Tipping the Velvet'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Soumission'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Sharp Objects'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Sapiens: A Brief History ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='The Requiem Red'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='The Dirty Little Secrets ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='The Coming Woman: A ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='The Boys in the ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='The Black Maria'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Starving Hearts (Triangular Trade ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data="Shakespeare's Sonnets">,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Set Me Free'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data="Scott Pilgrim's Precious Little ...">,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Rip it Up and ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Our Band Could Be ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Olio'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Mesaerion: The Best Science ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data='Libertarianism for Beginners'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/text()" data="It's Only the Himalayas">]

# To extract the first record, get() method is to be used.
# In [17]: response.css("article.product_pod h3 a::text").get()
# Out[17]: 'A Light in the ...'

# To extract all the records, getall() is used.
# In [18]: response.css("article.product_pod h3 a::text").getall()
# Out[18]: ['A Light in the ...',
#  'Tipping the Velvet',
#  'Soumission',
#  'Sharp Objects',
#  'Sapiens: A Brief History ...',
#  'The Requiem Red',
#  'The Dirty Little Secrets ...',
#  'The Coming Woman: A ...',
#  'The Boys in the ...',
#  'The Black Maria',
#  'Starving Hearts (Triangular Trade ...',
#  "Shakespeare's Sonnets",
#  'Set Me Free',
#  "Scott Pilgrim's Precious Little ...",
#  'Rip it Up and ...',
#  'Our Band Could Be ...',
#  'Olio',
#  'Mesaerion: The Best Science ...',
#  'Libertarianism for Beginners',
#  "It's Only the Himalayas"]

# In the above one, the names are not being displayed completely, so to avoid this, attr() needs to be used.
# In [21]: response.css("article.product_pod h3 a::attr(title)")
# Out[21]: [<Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='A Light in the Attic'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Tipping the Velvet'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Soumission'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Sharp Objects'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Sapiens: A Brief History of Humankind'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='The Requiem Red'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='The Dirty Little Secrets of Getting Y...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='The Coming Woman: A Novel Based on th...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='The Boys in the Boat: Nine Americans ...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='The Black Maria'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Starving Hearts (Triangular Trade Tri...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data="Shakespeare's Sonnets">,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Set Me Free'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data="Scott Pilgrim's Precious Little Life ...">,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Rip it Up and Start Again'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Our Band Could Be Your Life: Scenes f...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Olio'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Mesaerion: The Best Science Fiction S...'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data='Libertarianism for Beginners'>,
#  <Selector query="descendant-or-self::article[@class and contains(concat(' ', normalize-space(@class), ' '), ' product_pod ')]/descendant-or-self::*/h3/descendant-or-self::*/a/@title" data="It's Only the Himalayas">]

# In [22]: response.css("article.product_pod h3 a::attr(title)").get()
# Out[22]: 'A Light in the Attic'

# In [23]: response.css("article.product_pod h3 a::attr(title)").getall()
# Out[23]: ['A Light in the Attic',
#  'Tipping the Velvet',
#  'Soumission',
#  'Sharp Objects',
#  'Sapiens: A Brief History of Humankind',
#  'The Requiem Red',
#  'The Dirty Little Secrets of Getting Your Dream Job',
#  'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull',
#  'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics',
#  'The Black Maria',
#  'Starving Hearts (Triangular Trade Trilogy, #1)',
#  "Shakespeare's Sonnets",
#  'Set Me Free',
#  "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)",
#  'Rip it Up and Start Again',
#  'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991',
#  'Olio',
#  'Mesaerion: The Best Science Fiction Stories 1800-1849',
#  'Libertarianism for Beginners',
#  "It's Only the Himalayas"]


