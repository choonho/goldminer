# Read Naver News
# Write to Tistory

from datetime import datetime
from pytz import timezone
from goldminer.tasks.naver import search_news

today = datetime.now(timezone('Asia/Seoul')).strftime("%Y-%m-%d %H")

result = search_news("국내증시", 5)
content = ""
for item in result:
    content = content + "<h2>" + item['title'] + "</h2>" + "<br>" + item['description'] + "<br>" + \
            "원문: <a href=\"" + item['link'] + "\" target=\"_blank\">" + item['link'] + "</a>" + "<br><br>"

from goldminer.tasks.tistory import write_tistory_post
write_tistory_post("국내증시 " + today, content)

#from goldminer.tasks.blogger import create_blogger_post
#create_blogger_post("국내 증시 " + today, content)
