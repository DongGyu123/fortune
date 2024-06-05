FROM python:3.10.12-slim

# 작업 디렉터리 설정
WORKDIR /front

# 현재 디렉터리의 모든 파일을 이미지의 /app 디렉터리로 복사
COPY . /front


# 기본 명령어 설정
CMD ["python", "app.py"]