resource "aws_instance" "filmslog_ec2" {
  ami                    = "ami-0d6a47b74c05f9c89"
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.filmslog_sg.id]
  iam_instance_profile   = aws_iam_instance_profile.ec2_profile.name

  user_data = <<-EOF
    #!bin/bash
    yum update -y
    yum install -y docker
    service docker start
    usermod -a -G docker ec2-user
    aws ecr get-login-password --region ap-southeast-1 | docker login --username AWS --password-stdin ${aws_ecr_repository.filmslog_ecr.repository_url}
  EOF

  tags = {
    Name = "filmslog-ec2"
  }
}
