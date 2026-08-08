output "ec2_public_ip" {
  value = aws_instance.filmslog_ec2.public_ip
}

output "ecr_repository_url" {
  value = aws_ecr_repository.filmslog_ecr.repository_url
}

output "s3_bucket_name" {
  value = aws_s3_bucket.filmslog_bucket.bucket
}
