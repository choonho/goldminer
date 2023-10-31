# Tistory API 키와 블로그 정보

import requests
import os

blog_name = os.environ.get('BLOG_NAME')
access_token = os.environ.get('TISTORY_ACCESS_TOKEN')

# 블로그 글 작성 함수
def write_tistory_post(title, content):
    api_url = f'https://www.tistory.com/apis/post/write'
    
    data = {
        'access_token': access_token,
        'output': 'json',
        'blogName': blog_name,
        'title': title,
        'content': content,
        'visibility': '3',
        'category': '537211',
    }

    response = requests.post(api_url, data=data)
    print(response)    
    if response.status_code == 200:
        print('글 작성 성공')
    else:
        print('글 작성 실패')
        print(response.text)

def list_categories():
    api_url = f'https://www.tistory.com/apis/category/list'
    
    data = {
        'access_token': access_token,
        'output': 'json',
        'blogName': blog_name,
    }

    response = requests.get(api_url, params=data)
    print(response)    
    if response.status_code == 200:
        print('카테고리 조회 성공')
        print(response.json())
    else:
        print('카테고리 조회 실패')
        print(response.text)

# 글 작성 테스트
if __name__ == '__main__':
    title = '새로운 글 제목'
    content = '이것은 새로운 글의 내용입니다.'
    write_tistory_post(title, content)
    list_categories()
