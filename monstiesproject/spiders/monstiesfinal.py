#fetch('https://monsterhunterworld.wiki.fextralife.com/Monsters')
#ALTERNATE TO WRITE TO CSV IN TERMINAL -
#scrapy crawl monsties -o NAME.csv 

import scrapy
from scrapy.selector import Selector


# 'scrapy crawl monsties' in terminal when in correct directory

#Set switch to True for image grab, False for name/quote grab
switch = True

#MONSTIE
class mon_stats(scrapy.Item):
    # ... other item fields ...
    image_urls = scrapy.Field()
    images = scrapy.Field()

#MONSTIE SPIDER
class MonstiesSpider(scrapy.Spider):
    name = 'monsties'
    allowed_domains = ['monsterhunterworld.wiki.fextralife.com'] # NEEDS TO HAVE NO HTTP
    start_urls = ['https://monsterhunterworld.wiki.fextralife.com//Large+Monsters'] #https://monsterhunterworld.wiki.fextralife.com/Monsters for small monsters
                 
    #MONSTIE URL SCRAPE
    def parse(self, response):
        for link in response.css('div#tagged-pages-container > a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_bio)
    
    #RESPONSE CALLBACK
    def parse_bio(self, response):
            mon_image_urls = mon_stats()
            monsties_list = response.css('div#main-content')
            monimages = response.css('div.col-sm-6')
            #relative_imgs = monimages.xpath('//img[contains(@title, "hzv")]/@src').extract() # Needs to be absolute url
            mon_image_urls['image_urls'] =[]

                    
        #MONSTIE IMAGE GRAB
            if switch == True:
                for link in monimages.xpath('//img[contains(@title, "hzv")]/@src').extract():
                    mon_image_urls['image_urls'].append(response.urljoin(link)) #converts relative url to absolute

                    return {mon_image_urls}
        
        #MONSTIE NAME AND QUOTE GRAB
            else:
                for monstie in monsties_list:
           
                    return {
                        'name' : monstie.css('table.wiki_table h2::text').get(),
                        'quote' : monstie.css('blockquote p::text').get()
                    }
            
            #TO DO
            # . Function to write name & quote results to csv
            # . Unable to scrape images and write name/quote to csv at same time.
            
            
            
            
            
            
            
            
            
            #yield {
                   # 'image_urls' : mon_image_urls #monimages.xpath('//img[contains(@title, "hzv")]/@src').get() 
                #}           

            #IMG GRAB XPATH

            #poop = response.css('div.col-sm-6')
            #poop.xpath('//img[contains(@title, "hzv")]/@src').get()


                #yield {   
                    #'name' : monstie.css('div.lightbox-caption > a::text').getall(),
                    #'url' : monstie.css('a::attr(href)').getall()    
                    # }       
                #yield {
                    #'name' : monstie.css('a.wiki_link::text').getall()
                  #}
              
        #div_tag= response.xpath('//div')
        #div_tag.getall()
        #for tags in div_tag:
            #tag = tags.xpath('//div.lightbox-caption').get()
            
        #sel = Selector(response)
        #results = sel.xpath("//*[contains(@id, 'gallery-1']").get()
        #for result in results:
        #gallery_0 = response.css('div[id="gallery-0"]')
        #gallery_1 = response.css('div[id="gallery-1"]')
        
        #monsties_list = response.css('div.lightbox-caption')
        #for next_page in gallery_0 and gallery_1: #response.css('div.lightbox-caption'):
            #for link in response.css('a::attr(href)'):
                #yield response.follow(link.get(), callback= self.parse_bio)

        #def parse_bio(self, response):
            #monsties_list = response.css('div.tagged-pages-container')
            #for monstie in monsties_list:
            
                
                #yield {
                    #'name' : monstie.css('a.wiki_link::text').getall()
                    #}
                    #'name' : monstie.css('div.lightbox-caption > a::text').getall(),
                    #'url' : monstie.css('a::attr(href)').getall()
