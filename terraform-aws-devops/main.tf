##########################################################
# Terraform: DevOps Mini Project EC2 Deployment
# Stage 5 - AWS + Docker
# Author: Stacey Foxx
##########################################################

# -------------------------
# PROVIDER: AWS
# -------------------------
provider "aws" {
  region = var.aws_region
}

# -------------------------
# VARIABLES
# -------------------------
variable "aws_region" {
  description = "AWS region to deploy the EC2 instance"
  default     = "eu-west-2"  # London
}

variable "instance_type" {
  description = "EC2 instance type (free-tier eligible)"
  default     = "t3.micro"
}

variable "ami_id" {
  description = "Amazon Linux 2 AMI ID for eu-west-2"
  default     = "ami-07b22f026de539357" # Replace with latest AMI
}

variable "ssh_key_name" {
  description = "AWS key pair name to attach to EC2"
  default     = "devops-mini-key"
}

variable "ssh_key_path" {
  description = "Path to your SSH private key (.pem) for EC2 access"
  default     = "***REMOVED***"
}

# -------------------------
# DATA: Default VPC
# -------------------------
data "aws_vpc" "default" {
  default = true
}

# -------------------------
# RESOURCE: SECURITY GROUP
# -------------------------
resource "aws_security_group" "web_sg" {
  name        = "devops-mini-sg"
  description = "Allow HTTP traffic to EC2 instance"
  vpc_id      = data.aws_vpc.default.id

  # Allow HTTP from anywhere (IPv4)
  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow HTTP from anywhere (IPv6)
  ingress {
    description      = "Allow HTTP IPv6"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    ipv6_cidr_blocks = ["::/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

# -------------------------
# RESOURCE: EC2 INSTANCE
# -------------------------
resource "aws_instance" "web" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  key_name               = var.ssh_key_name
  vpc_security_group_ids = [aws_security_group.web_sg.id]

  # USER DATA: runs on first boot
  user_data = <<-EOF
              #!/bin/bash
              # Update system packages
              yum update -y
              # Install Docker
              amazon-linux-extras install docker -y
              # Start Docker service
              service docker start
              # Run your DockerHub container
              docker run -d -p 80:80 sfoxx/devops-mini-project:latest
              EOF

  tags = {
    Name = "devops-mini-project"
  }
}

# -------------------------
# OUTPUTS
# -------------------------
output "ec2_public_ip" {
  description = "Public IP of the EC2 instance running the mini project"
  value       = aws_instance.web.public_ip
}

output "ssh_command" {
  description = "SSH command to access your EC2 instance"
  value       = "ssh -i ${var.ssh_key_path} ec2-user@${aws_instance.web.public_ip}"
}