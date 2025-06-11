import scrapy
from task2.items import AnimalItem


class AnimalsSpider(scrapy.Spider):
    name = "animals"
    allowed_domains = ["ru.wikipedia.org"]
    start_urls = [
        "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    ]

    def parse(self, response):
        # 1) собрать все имена из блоков mw-category-group
        for text in response.css(
            "div.mw-category-group ul li a::text"
        ).getall():
            yield AnimalItem(name=text.strip())

        # 2) найти ссылку «Следующая страница» и спарсить дальше
        next_href = response.xpath(
            '//div[@id="mw-pages"]//a[contains(text(),"Следующая страница")]/@href'
        ).get()
        if next_href:
            yield response.follow(next_href, callback=self.parse)
