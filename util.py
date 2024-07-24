import requests
import yaml

# FastAPI 서버 URL
url = "http://127.0.0.1:8000/openapi.json"

# JSON 데이터 요청
response = requests.get(url)

# JSON 데이터를 YAML로 변환
swagger_json = response.json()
with open("swagger.yaml", "w") as yaml_file:
    yaml.dump(swagger_json, yaml_file, default_flow_style=False)

print("swagger.yaml 파일이 생성되었습니다.")
