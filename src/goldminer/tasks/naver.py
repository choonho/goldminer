import requests
import os

# Naver 개발자 포털에서 발급받은 API 키
#api_key = os.envion.get("NAVER_API_KEY")
naver_client_id = os.environ.get("NAVER_CLIENT_ID")
naver_client_secret = os.environ.get("NAVER_CLIENT_SECRET")

# Naver 뉴스 검색 API 엔드포인트
api_endpoint = "https://openapi.naver.com/v1/search/news.json"

# 검색어 설정
query = "국내증시"

# API 요청 헤더 설정
headers = {
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret": naver_client_secret
}

def search_news(query, display=10):
    # 요청 파라미터 설정
    params = {
        "query": query,
        "display": display,  # 가져올 뉴스 아이템 수 (최대 100까지 가능)
    }

    # API 요청 보내기
    response = requests.get(api_endpoint, params=params, headers=headers)

    result = []
    # 응답 확인
    if response.status_code == 200:
        data = response.json()
        # 검색 결과 출력
        for item in data["items"]:
            title = item["title"].replace("<b>", "").replace("</b>", "")
            link = item["link"]
            description = item["description"].replace("<b>", "").replace("</b>", "")
            result.append({"title": title, "link": link, "description": description})
    else:
        print("API 요청에 실패했습니다. 상태 코드:", response.status_code)
    return result

if __name__ == "__main__":
    result = search_news("국내증시", 5)
    for news in result:
        print(news['title'])

