FROM python:3.8-slim
RUN apt-get update -y
RUN apt-get install -y libpcsclite-dev psmisc libcurl4-openssl-dev libssl-dev
RUN mkdir -p /root/kby-ai-idcard
WORKDIR /root/kby-ai-idcard
COPY ./libkbyai_idsdk.so .
COPY ./libimutils.so_for_ubuntu22 /usr/lib/libimutils.so
COPY ./idsdk.py .
COPY ./app.py .
COPY ./demo.py .
COPY ./requirements.txt .
COPY ./run.sh .
COPY ./idcard_examples ./idcard_examples
COPY ./data ./data
RUN pip3 install -r requirements.txt
CMD ["./run.sh"]
EXPOSE 8080 9000
