# Tistory API 키와 블로그 정보

import requests
import os

blog_name = os.environ.get('BLOG_NAME')
access_token = os.environ.get('TISTORY_ACCESS_TOKEN')

# 블로그 글 작성 함수
def write_tistory_post(title, content, category=None):
    api_url = f'https://www.tistory.com/apis/post/write'
    
    data = {
        'access_token': access_token,
        'output': 'json',
        'blogName': blog_name,
        'title': title,
        'content': content,
        'visibility': '3',
    }
    if category:
        category_id = get_category_id(category)
        if category_id:
            data['category'] = category_id
        else:
            print(f'카테고리 {category}가 존재하지 않습니다.')
            return

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
        return response.json()
    else:
        print('카테고리 조회 실패')
        print(response.text)
        return {}

def get_category_id(name):
    result = list_categories()
    try:
        categories = result['tistory']['item']['categories']
        for category in categories:
            if category['name'] == name:
                return category['id']
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    title = '새로운 글 제목'
    content = '이것은 새로운 글의 내용입니다.'
    write_tistory_post(title, content, '해외증시')
    a = list_categories()
    b = get_category_id('해외증시')
    print(b)
