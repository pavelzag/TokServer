FROM python:2
ADD main.py /
ADD configuration.py /
ADD dbconnector.py /
ADD config.yml /
ADD query_builder.py /
ADD tags_generator.py
RUN pip install flask
RUN pip install flask_mongoalchemy
RUN pip install faker
RUN pip install Bottle
CMD [ "python", "./main.py" ]