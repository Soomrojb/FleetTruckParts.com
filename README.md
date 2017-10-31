# Fleettruckparts Scraper
Fleettruckparts.com is a parts website with few dozen thousands parts; this script will visit all of its available brands, do pagination and finally get basic fields.

How to use the script?
- [x] `scrapy crawl fleetp`
- [x] `scrapy crawl fleetp -o products.csv -t csv`

Default fileds:
- [x] Category Title
- [x] Category Href
- [x] Product Title
- [x] Product Href
- [x] Breadcrumb
- [x] Part Number #
- [x] Price
- [x] Image URL
- [x] Product Short Descption
- [x] Product Details/Description

Expected future changes:
- [ ] Rolling Proxies support
- [ ] MySQLdb support
