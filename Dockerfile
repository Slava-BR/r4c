
FROM python
#рабочая директория внутри контейнера
WORKDIR /usr/src/app

COPY requirements.txt ./


RUN pip install -r requirements.txt