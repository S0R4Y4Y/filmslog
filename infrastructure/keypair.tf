resource "aws_key_pair" "filmslog_key" {
  key_name   = "filmslog-key"
  public_key = file("~/.ssh/filmslog.pub")
}
