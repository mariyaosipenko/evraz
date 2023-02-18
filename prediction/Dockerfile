FROM python:3.7.6
WORKDIR /code
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src/ src/
CMD ["python", "-u", "src/main.py"]