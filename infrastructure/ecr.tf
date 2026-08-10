resource "aws_ecr_repository" "filmslog_ecr" {
  name                 = "filmslog"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name = "filmslog-ecr"
  }
}
