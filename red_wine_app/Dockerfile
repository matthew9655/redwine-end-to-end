FROM python:3.13

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/fastapi

# Install requirements, including from Gemfury
ADD ./fastapi /opt/fastapi/
RUN pip install --upgrade pip
RUN pip install -r /opt/fastapi/requirements/requirements.txt

RUN chmod +x /opt/fastapi/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
