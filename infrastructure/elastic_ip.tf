resource "aws_eip" "filmslog_eip" {
  instance = aws_instance.filmslog_ec2.id
  domain   = "vpc"

  tags = {
    Name = "filmslog-eip"
  }
}

output "elastic_ip" {
  value = aws_eip.filmslog_eip.public_ip
}
