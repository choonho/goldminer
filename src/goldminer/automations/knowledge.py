# Read Naver News
# Write to Tistory
import sys
from goldminer.tasks.wikipedia import search_wikipedia

def main(keyword):
  print(f"keyword: {keyword}")
  item = search_wikipedia(keyword)
  if item == False:
    print("Search failed")
    return
  content = "<h2>" + item['title'] + "</h2>" + "<br>" + item['summary'] + "<br>" + \
            "원문: <a href=\"" + item['fullurl'] + "\" target=\"_blank\">" + item['fullurl'] + "</a>" + "<br><br>"
  title = f"{keyword}"
  from goldminer.tasks.tistory import write_tistory_post
  a = write_tistory_post(title, content, "상식")
  print(a)

if __name__ == "__main__":
  args = sys.argv[1:]
  main(args[0])
