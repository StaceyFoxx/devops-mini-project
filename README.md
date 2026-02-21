# DevOps Mini Project

This is a mini DevOps project showcasing my skills in **containerization, cloud infrastructure, and IaC**.

---

## Project Overview

This project demonstrates:

- **Docker**: Containerized a static HTML website using **Nginx**
- **DockerHub**: Image pushed for sharing (`sfoxx/devops-mini-project:latest`)
- **Terraform + AWS**: Deploys an EC2 instance with security groups and runs the container automatically
- **Kubernetes & CI/CD**: Planned for orchestrating the container and automating deployments

The goal is to show a **full DevOps workflow** from containerization to cloud deployment, with the ability to scale using Kubernetes and automate updates via CI/CD.

---

## Tech Stack & Tools

| Category                | Tool / Service   | Notes                                            |
| ----------------------- | ---------------- | ------------------------------------------------ |
| Containerization        | Docker           | Builds and runs the web app container            |
| Container Registry      | DockerHub        | Public image: `sfoxx/devops-mini-project:latest` |
| Cloud Provider          | AWS              | EC2 instance running the container               |
| Infrastructure as Code  | Terraform        | Declarative deployment of EC2 & Security Groups  |
| Web Server              | Nginx            | Serves the HTML mini project inside Docker       |
| CI/CD (Planned)         | GitHub Actions   | Automate Docker build & deploy                   |
| Orchestration (Planned) | Kubernetes (EKS) | Scale application using pods & services          |

---

## Live Demo

After deploying via Terraform, the website is accessible at the **public IP shown in Terraform output**:

```text
http://<ec2_public_ip>
```
