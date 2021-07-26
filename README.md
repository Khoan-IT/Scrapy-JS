# Scrapy-JS
# Cài Docker cho máy tính sau đó chạy 2 lệnh:
  + sudo docker pull scrapinghub/splash
  + sudo docker run -p 8050:8050 scrapinghub/splash
# Thay đổi USER_AGENT phù hợp với máy tính:
  1: Lấy USER_AGENT tại: https://www.whatismybrowser.com/detect/what-is-my-user-agent
  2: Thay đổi USER_AGENT trong file settings.py
# Crawl dữ liệu
  scrapy crawl shopee_crawl -o product.json
