# DevOps Mini Project

This is a mini DevOps project showcasing my skills in **containerization, cloud infrastructure, and Infrastructure as Code (IaC)**.

---

## Project Overview

This project demonstrates:

- **Docker**: Containerized a static HTML website using **Nginx**  
- **DockerHub**: Image pushed for sharing (`sfoxx/devops-mini-project:latest`)  
- **Terraform + AWS**: Deploys an EC2 instance with security groups and runs the container automatically  
- **Kubernetes & CI/CD (Planned)**: Orchestrate containers and automate deployments  

The goal is to show a **full DevOps workflow** from containerization to cloud deployment, with the ability to scale using Kubernetes and automate updates via CI/CD.

---

## Tech Stack & Tools

| Category                | Tool / Service   | Notes                                             |
| ----------------------- | --------------- | ------------------------------------------------ |
| Containerization        | Docker           | Builds and runs the web app container           |
| Container Registry      | DockerHub        | Public image: `sfoxx/devops-mini-project:latest`|
| Cloud Provider          | AWS              | EC2 instance running the container              |
| Infrastructure as Code  | Terraform        | Declarative deployment of EC2 & security groups |
| Web Server              | Nginx            | Serves the HTML mini project inside Docker      |
| CI/CD (Planned)         | GitHub Actions   | Automate Docker build & deploy                  |
| Orchestration (Planned) | Kubernetes (EKS) | Scale application using pods & services         |

---

## How to Run

### Run Docker, Terraform, and Kubernetes

```bash
# 1️⃣ Build & run Docker locally
docker build -t devops-mini-project:latest .
docker run -p 80:80 devops-mini-project:latest

# 2️⃣ Deploy via Terraform
terraform init
terraform apply \
  -var "ssh_key_name=YOUR_KEY_NAME" \
  -var "ssh_key_path=/path/to/YOUR_KEY.pem"
# Replace YOUR_KEY_NAME and /path/to/YOUR_KEY.pem with your own AWS key pair. Do not use keys from this repo.

# 3️⃣ Deploy via Kubernetes (Optional)
Kubernetes manifests are located in the k8s/ folder:
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

### Live Demo

After deploying via Terraform, the website is accessible at the public IP shown in Terraform output:

- **Terraform**: Use the `ec2_public_ip` output  
- **Kubernetes**: Use `kubectl get service` output for the external IP  

Live Demo: _http://<ec2_public_ip>_
