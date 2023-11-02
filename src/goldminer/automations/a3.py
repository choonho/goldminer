# Read Naver News
# Write to Tistory

from datetime import datetime
from pytz import timezone
from goldminer.tasks.naver import search_news

today = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H")
search_key = "부동산"

result = search_news(search_key, 5)
content = ""
for item in result:
    content = content + "<h2>" + item['title'] + "</h2>" + "<br>" + item['description'] + "<br>" + \
            "원문: <a href=\"" + item['link'] + "\" target=\"_blank\">" + item['link'] + "</a>" + "<br><br>"

title = f"{search_key} {today}시 주요 뉴스"
from goldminer.tasks.tistory import write_tistory_post
write_tistory_post(title, content, search_key)

#from goldminer.tasks.blogger import create_blogger_post
#create_blogger_post(title, content)
