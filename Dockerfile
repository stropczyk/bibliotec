FROM tiangolo/meinheld-gunicorn-flask:python3.8
ADD ./app /app
COPY requirements.txt /app
WORKDIR /app

# Install dependencies:
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python3", "main.py" ]