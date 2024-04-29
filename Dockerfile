# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12-slim

EXPOSE 8000

# Install Gunicorn
RUN pip install gunicorn

#Keeps Python from generating .pyc files in the container

ENV PYTHONDONTWRITEBYTECODE=1

ENV MONGO_URL= mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test

ENV secret = 2668fc01978a735803b1643ae8cfd70b
ENV algorithm = HS256


# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
