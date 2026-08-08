resource "aws_s3_bucket" "filmslog_bucket" {
  bucket = "filmslog-bucket-${random_id.bucket_id.hex}"

  tags = {
    Name = "filmslog-bucket"
  }
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

resource "aws_s3_bucket_versioning" "filmslog_versioning" {
  bucket = aws_s3_bucket.filmslog_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}
