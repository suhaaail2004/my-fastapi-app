# My FastAPI Application

A lightweight REST API application built using **Python, FastAPI, and Uvicorn**. This project demonstrates API development, containerization using Docker, and deployment using Kubernetes.

## Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic
- Docker
- Jenkins
- SonarQube
- Kubernetes

## Project Structure

```text
my_fastapi_app/
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── .env.example
├── .gitignore
├── Dockerfile
├── Jenkinsfile
├── README.md
├── main.py
└── requirements.txt
```

## Application Features

- Welcome endpoint
- Retrieve items using path and query parameters
- Create items using POST requests
- Request body validation using Pydantic
- Automatic API documentation

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd my_fastapi_app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Access the application:

- Application: http://localhost:8000
- Interactive API documentation: http://localhost:8000/docs
- Alternative API documentation: http://localhost:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/items/{item_id}` | Retrieve item information |
| POST | `/items/` | Create a new item |

## Docker

Build the Docker image:

```bash
docker build -t my-fastapi-app .
```

Run the Docker container:

```bash
docker run -d -p 8000:8000 --name fastapi-container my-fastapi-app
```

Access the API at:

```text
http://localhost:8000/docs
```

## Kubernetes Deployment

Apply the Kubernetes Deployment:

```bash
kubectl apply -f k8s/deployment.yaml
```

Apply the Kubernetes Service:

```bash
kubectl apply -f k8s/service.yaml
```

Check running pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get services
```

## CI/CD Pipeline

The Jenkins pipeline automates the following stages:

1. Source code checkout from GitHub.
2. Code analysis using SonarQube.
3. Docker image building.
4. Docker image pushing to Docker Hub.
5. Kubernetes deployment manifest update.

## Author

Developed as a DevOps pipeline practice project.