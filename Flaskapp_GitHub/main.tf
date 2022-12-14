terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}
provider "aws" {
  region = "eu-north-1"
}
resource "aws_key_pair" "deployer" {
  key_name   = "aws-key"
  public_key = file("/Users/pavlo/.ssh/aws-key.pub")
}
resource "aws_instance" "terraform_ubuntu" {
  ami = "ami-092cce4a19b438926" # Ubuntu Server 20.04 LTS ami
  instance_type = "t3.micro"
  key_name = "aws-key"
  vpc_security_group_ids = [aws_security_group.flask.id]
  tags = {
    "Name" = "terraform_ubuntu"
  }
}

resource "aws_default_vpc" "main" {
  tags = {
    Name = "main"
  }
}

resource "aws_security_group" "flask" {
  name        = "flask"
  description = "Security policies for ubuntu instance"
  vpc_id      = aws_default_vpc.main.id
  
    ingress {
    description      = "for Flaskapp"
    from_port        = 5000
    to_port          = 5000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
   }

   ingress {
    description      = "SSH from host to EC2"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
   }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}
  

output "ip" {
  value = aws_instance.terraform_ubuntu.public_ip
}


resource "local_file" "public_ip_for_deploy" {
   content = <<EOT
    [terraform_ubuntu]
    ${aws_instance.terraform_ubuntu.public_ip}
      EOT
      filename = "./ansible/serverIP.txt"
      }
