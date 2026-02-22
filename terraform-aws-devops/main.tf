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

  ingress {
    description = "Allow HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description      = "Allow HTTP IPv6"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    ipv6_cidr_blocks = ["::/0"]
  }

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
              yum update -y
              amazon-linux-extras install docker -y
              service docker start
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