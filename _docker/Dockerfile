FROM python:3.9

WORKDIR /certmon

COPY requirements.txt /certmon/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]