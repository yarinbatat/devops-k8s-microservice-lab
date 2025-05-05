
# Status Service - Kubernetes Microservice Lab

This is a simple microservice written in Flask that returns system status (uptime, CPU, memory).

## 🔧 Requirements

- Python 3.8+
- Docker
- Minikube
- kubectl
- (Optional) Helm

## 📁 Project Structure

```
devops-k8s-microservice-lab/
│
├── app.py                # Flask app
├── Dockerfile            # Build the container
├── deployment.yaml       # Kubernetes deployment
├── service.yaml          # Kubernetes service
└── README.md
```

## 🚀 Run Locally

### 1. Build Docker image

```bash
docker build -t status-service .
```

### 2. Start Minikube

```bash
minikube start
minikube addons enable ingress
```

### 3. Deploy to Kubernetes

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 4. Access the service

Get the NodePort URL:

```bash
minikube service status-service --url
```

Or use the domain if you added `status.local` to your `hosts` file:

```
http://status.local:<nodeport>/status
```

## 🐳 Dockerfile

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask psutil
CMD ["python", "app.py"]
```

## 📦 Helm Monitoring (optional)

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack
```

## 🧪 Status API Output

```json
{
  "uptime": 124556.5,
  "cpu_percent": 12.3,
  "memory": {
    "total": 17179869184,
    "available": 12563423232,
    ...
  }
}
```

---

## ✅ Author

- Yarin 🇮🇱  
