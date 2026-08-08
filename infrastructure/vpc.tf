resource "aws_vpc" "filmslog_vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "filmslog-vpc"
  }
}

resource "aws_subnet" "public_subnet" {
  vpc_id = aws_vpc.filmslog_vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "ap-southeast-1a" 
  map_public_ip_on_launch = true

  tags = {
    Name = "filmslog-public-subnet"
  }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.filmslog_vpc.id

  tags = {
    Name = "filmslog-igw"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.filmslog_vpc.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "filmslog-public-rt"
  }
}

resource "aws_route_table_association" "public_assoc" {
  subnet_id = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

