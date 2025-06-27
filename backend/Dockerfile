FROM python:3.9-slim
LABEL authors="aw.ahmed.werghi@gmail.com"

# set the working directory in the container
WORKDIR /app

# Copy the dependencies
COPY requirements.txt .

#Install the needed requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .


# Expose 8000
Expose 8000

CMD ["uvicorn", "app.main:app","--host", "0.0.0.0" , "--port", "8000"]