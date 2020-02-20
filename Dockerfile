FROM tensorflow/tensorflow:2.0.1-py3
COPY . /app
WORKDIR /app
RUN pip install -r docker_requirements.txt
EXPOSE 5050
CMD python3 ./main.py
