# py3_flask_simple_server
 a simple flask server run with docker


### build Docker image
```bash
docker build -t py3_test -f BackendServer/Dcokerfile .
```
### run Docker container
```bash
docker run -d -p 8080:8080 --name py3 py3_test 
```

### check if it works
http://localhost:8080/

http://localhost:8080/activity/

---

### 資料夾架構
```text
 - BackendServer
  - Dockerfile
  - main.py
  - requirements.txt
 - Other
  - Activity.py
```
其中main.py中會使用Other/Activity.py

> 主要是想要測試如何複製父層資料夾的作法