# DevOps Mini Project

This is a mini DevOps project showcasing my skills in **containerization, cloud infrastructure, and Infrastructure as Code (IaC)**.

[![Docker CI](https://github.com/StaceyFoxx/devops-mini-project/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/StaceyFoxx/devops-mini-project/actions/workflows/docker-ci.yml)
[![Docker Image](https://img.shields.io/badge/docker-image-blue)](https://hub.docker.com/r/sfoxx/devops-mini-project)
[![Terraform](https://img.shields.io/badge/terraform-deployed-green)](#)

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

| Category                | Tool / Service   | Notes                                            |
| ----------------------- | ---------------- | ------------------------------------------------ |
| Containerization        | Docker           | Builds and runs the web app container            |
| Container Registry      | DockerHub        | Public image: `sfoxx/devops-mini-project:latest` |
| Cloud Provider          | AWS              | EC2 instance running the container               |
| Infrastructure as Code  | Terraform        | Declarative deployment of EC2 & security groups  |
| Web Server              | Nginx            | Serves the HTML mini project inside Docker       |
| CI/CD (Planned)         | GitHub Actions   | Automate Docker build & deploy                   |
| Orchestration (Planned) | Kubernetes (EKS) | Scale application using pods & services          |

---

## Repository Cleaning & Security

This repository has been **fully sanitized** to remove any sensitive information:

✅ All private keys (.pem) have been removed from Git history  
✅ Hardcoded absolute paths to local directories have been cleared  
✅ Workflows and modules verified to run safely without secrets

This demonstrates best practices in **repository hygiene and security**, ensuring safe collaboration and deployment.

## How to Run

### Run Docker, Terraform, and Kubernetes

````bash
# 1️⃣ Build & run Docker locally
docker build -t devops-mini-project:latest .
docker run -p 80:80 devops-mini-project:latest

# 2️⃣ Deploy via Terraform
terraform init
terraform apply \
  -var "ssh_key_name=YOUR_KEY_NAME" \
  -var "ssh_key_path=/path/to/YOUR_KEY.pem"
# Replace YOUR_KEY_NAME and /path/to/YOUR_KEY.pem with your own AWS key pair.

terraform output ec2_public_ip
# Example output: 18.123.45.67

Live Demo:

Terraform: Use the ec2_public_ip output
Kubernetes: Use kubectl get service output for the external IP

Live Demo: http://<ec2_public_ip>

# 3️⃣ Deploy via Kubernetes (Optional)
Kubernetes manifests are located in the k8s/ folder:
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

### 4️⃣ Run CI/CD Pipeline

This project uses **GitHub Actions** to automatically build and push Docker images to DockerHub on every push to the `main` branch.

# 1️⃣ Make sure your GitHub Secrets are set:
#   - DOCKERHUB_USERNAME = your DockerHub username
#   - DOCKERHUB_TOKEN = personal access token from DockerHub

# 2️⃣ Commit and push your code to main
git add .
git commit -m "Trigger CI/CD pipeline"
git push origin main

# 3️⃣ Check pipeline status on GitHub
# Go to your repository → Actions tab → "Docker CI Pipeline"
# You should see it running. Green ✅ means the build & push succeeded.

# 4️⃣ Verify Docker image on DockerHub
# Both commit SHA tag and "latest" tag should appear
# Example:
docker pull sfoxx/devops-mini-project:latest
docker pull sfoxx/devops-mini-project:<commit-sha>

### Pro Tip: Dynamic Tags & IPs

- **Get the latest commit SHA for Docker pull:**
```bash
git rev-parse --short HEAD
# Example output: f3a1b2c
docker pull sfoxx/devops-mini-project:f3a1b2c
````
