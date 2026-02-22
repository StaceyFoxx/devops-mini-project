# terraform-aws-devops/variables.tf

variable "aws_region" {
  description = "AWS region to deploy the EC2 instance"
  default     = "eu-west-2"
}

variable "instance_type" {
  description = "EC2 instance type (free-tier eligible)"
  default     = "t3.micro"
}

variable "ami_id" {
  description = "Amazon Linux 2 AMI ID for eu-west-2"
  default     = "ami-07b22f026de539357"
}

variable "ssh_key_name" {
  description = "AWS key pair name to attach to EC2"
  default     = "devops-mini-key"
}

variable "ssh_key_path" {
  description = "Path to your SSH private key (.pem) for EC2 access"
  default     = "***REMOVED***"
}