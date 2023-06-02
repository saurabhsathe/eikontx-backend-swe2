FROM python:3.9

WORKDIR /eikon-backend

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py"]