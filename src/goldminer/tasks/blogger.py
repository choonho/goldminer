import os

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 구글 클라우드 콘솔에서 받은 자격 증명 파일 경로
CLIENT_SECRETS_FILE = 'credentials.json'

# Blogger API 서비스 이름
API_SERVICE_NAME = 'blogger'
API_VERSION = 'v3'

# 인증 범위
SCOPES = ['https://www.googleapis.com/auth/blogger']

blog_id = os.environ.get("BLOGSPOT_ID")

def create_blogger_post(title, content):
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)

    service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    blog_id = blog_id  # 포스트를 게시할 블로그 ID
    body = {
        'kind': 'blogger#post',
        'title': title,
        'content': content,
    }

    posts = service.posts()
    request = posts.insert(blogId=blog_id, body=body)
    response = request.execute()
    print('포스트가 성공적으로 생성되었습니다. 포스트 ID: %s' % response['id'])

if __name__ == '__main__':
    create_blogger_post('새로운 포스트 제목', '새로운 포스트 내용')
