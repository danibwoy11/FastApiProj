FROM python:3.10-slim


WORKDIR /app

COPY app/requirements.txt .

#RUN pip install --no cache-dir -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app/  . 

COPY models /app/models

COPY data  /app/data

EXPOSE 8000

#CMD [ "uvicorn",'mainapi:app','--host', '0.0.0.0','--port', '8000' ]
#CMD ["uvicorn", "mainapi:app", "--host", "0.0.0.0", "--port", "8000"]

CMD uvicorn mainapi:app --host 0.0.0.0 --port 8000