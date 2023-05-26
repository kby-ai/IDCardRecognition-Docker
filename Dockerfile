FROM python:3.8-slim
RUN apt-get update -y
RUN apt-get install -y libpcsclite-dev psmisc    
RUN mkdir -p /root/kby-ai-idcard
WORKDIR /root/kby-ai-idcard
COPY ./libidsdk.so .
COPY ./idsdk.py .
COPY ./app.py .
COPY ./requirements.txt .
COPY ./data ./data
RUN pip3 install -r requirements.txt
CMD [ "python3", "app.py"]
EXPOSE 8080