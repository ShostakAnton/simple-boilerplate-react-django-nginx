FROM python:3.10

# -- Install Pipenv stable
RUN pip install pipenv==2022.5.2 --upgrade pip  

RUN pip install psycopg2

# -- Install dependencies:
ADD ./Pipfile ./tmp/Pipfile
ADD ./Pipfile.lock ./tmp/Pipfile.lock
RUN cd /tmp &&  pipenv install --system --deploy 

# -- Update system
RUN apt-get update
RUN apt-get install binutils libproj-dev gdal-bin -y