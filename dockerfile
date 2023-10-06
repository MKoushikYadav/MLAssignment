#set compatible python version
FROM python:3.11

EXPOSE 5000
# set pwd
WORKDIR /app
COPY . /app/

# install dependencies
COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the scripts to pwd


# run the ML model
CMD ["gunicorn", "--bind","0.0.0.0:5000","app:app"]