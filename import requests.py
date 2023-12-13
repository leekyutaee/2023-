import requests
import json

# JSON 파일의 경로와 서버 URL을 설정합니다.
json_file_path = 'C:\\ocr\\output.json'
server_url = 'http://127.0.0.1:5000/'

# JSON 파일을 읽어옵니다.
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 서버로 POST 요청을 보냅니다.
response = requests.post(server_url, json=data)

# 응답 확인
if response.status_code == 200:
    print("JSON 파일을 성공적으로 전송했습니다.")
else:
    print("JSON 파일 전송에 실패했습니다. 상태 코드:", response.status_code)
    print("응답 내용:", response.text)