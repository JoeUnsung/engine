## 환경세팅 정리

### Python version: 
3.10.4
### 커맨드정리:
pyenv로 버전 세팅(brew install pyenv)

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

--버전 프리즈시
--pip freeze > requirements.txt

파이참 내에서 인터프리터 설정시 existing 선택 후 특정버전 python 선택
(new 선택시 새로운 폴더를 생성하여 해당 경로에 라이브러리를 설치하기 때문에 terminal과 pycharm interpreter에서 설치하는 라이브러리가 달라짐)

