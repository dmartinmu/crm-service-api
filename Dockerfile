# Parent image
FROM python:3.7

# Set the working directory in the container to /app
WORKDIR /app

# Copy requirements.txt before copying the source code
ADD ./requirements.txt /app

# Install requirements
RUN pip install pip==20.0.2 
RUN pip install -r requirements.txt

ARG test=FALSE

ADD ./requirements_test.txt /app
RUN if [ "$test" = "TRUE" ]; then \
     pip install -r requirements_test.txt; \
    fi

ADD ./entrypoint.sh /app

# Set the pythonpath
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

# Add the current directory to the container as /app
ADD ./src /app/src
ADD ./test /app/test

RUN mkdir /app/results

ENTRYPOINT ["./entrypoint.sh"]

CMD ["develop"]
