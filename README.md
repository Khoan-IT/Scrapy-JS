# Scrapy-DB
# Sau khi cài Docker:
  + sudo docker pull scrapinghub/splash
  + sudo docker run -p 8050:8050 scrapinghub/splash
# Thay đổi USER_AGENT:
  + Lấy USER_AGENT tại: https://www.whatismybrowser.com/detect/what-is-my-user-agent
  + Thay đổi USER_AGENT trong file settings.py
# Thay đổi đường dẫn đến MonGoDB trong file piline
# Crawl dữ liệu
  + scrapy crawl shopee_crawl -o product.json
