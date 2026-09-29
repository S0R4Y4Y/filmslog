# Filmslog

A personal movie diary web application where users can log, rate, and review films they have watched. Built as a cloud engineering portfolio project demonstrating containerization, infrastructure as code, automated CI/CD pipelines, and production-grade AWS deployment.

**Live:** https://myfilmslog.com

---

## Overview

Filmslog allows users to maintain a personal record of films they have watched. Each entry includes a title, genre, star rating, written review, and an optional movie poster uploaded directly to AWS S3. The diary page is fully customizable — users can set their own title and background image.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| File Storage | AWS S3 |
| Containerization | Docker, Docker Compose |
| Container Registry | AWS ECR |
| Compute | AWS EC2 (Amazon Linux 2023, t3.micro) |
| Networking | AWS VPC, Subnets, Security Groups, Elastic IP |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| Reverse Proxy | Nginx |
| SSL | Let's Encrypt (Certbot) |
| DNS / CDN | Cloudflare |

---

## Architecture

```
Developer pushes to main branch
        |
        v
GitHub Actions (CI/CD Pipeline)
        |
        |-- Build Docker image (linux/amd64)
        |-- Push to AWS ECR
        |-- SSH into EC2
        |-- Pull latest image
        `-- Restart container
                |
                v
        AWS EC2 Instance
        |-- Nginx (port 80/443)
        |   `-- Proxy to Flask (port 8080)
        |-- Docker container (Flask app)
        `-- AWS S3 (image storage)

DNS: Cloudflare -> Elastic IP -> EC2
SSL: Let's Encrypt via Certbot
```

---

## AWS Infrastructure

All infrastructure is provisioned as code using Terraform. No resources are created manually through the AWS console.

| Resource | Purpose |
|---|---|
| VPC | Isolated private network |
| Public Subnet | Hosts the EC2 instance |
| Internet Gateway | Enables internet access |
| Route Table | Directs traffic through the gateway |
| Security Groups | Firewall rules (ports 22, 80, 443, 8080) |
| EC2 (t3.micro) | Runs the Dockerized Flask application |
| Elastic IP | Fixed public IP address |
| ECR | Private Docker image registry |
| S3 + Versioning | Stores user-uploaded movie posters and backgrounds |
| IAM Role | Grants EC2 permission to pull from ECR and access S3 |

---

## CI/CD Pipeline

Every push to `main` triggers the following pipeline via GitHub Actions:

1. Checkout repository
2. Configure AWS credentials
3. Authenticate Docker with Amazon ECR
4. Build Docker image for `linux/amd64`
5. Push image to ECR with `latest` tag
6. SSH into EC2 instance
7. Pull latest image from ECR
8. Stop and remove existing container
9. Start new container

---

## Running Locally

### Prerequisites
- Docker and Docker Compose
- AWS account with S3 bucket
- AWS credentials with S3 access

### Setup

```bash
git clone https://github.com/S0R4Y4Y/filmslog.git
cd filmslog
```

Create a `.env` file in the project root:

```env
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
S3_BUCKET=your_bucket_name
AWS_DEFAULT_REGION=ap-southeast-1
```

Start the application:

```bash
docker-compose up --build
```

Access at `http://localhost:8080`

---

## Infrastructure Deployment

```bash
cd infrastructure
terraform init
terraform plan
terraform apply
```

To tear down all resources:

```bash
terraform destroy
```

---

## Project Structure

```
filmslog/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline
├── infrastructure/
│   ├── main.tf                 # Provider configuration
│   ├── vpc.tf                  # VPC, subnets, routing
│   ├── ec2.tf                  # EC2 instance
│   ├── ecr.tf                  # Container registry
│   ├── iam.tf                  # Roles and policies
│   ├── s3.tf                   # Object storage
│   ├── elastic_ip.tf           # Fixed public IP
│   ├── keypair.tf              # SSH key pair
│   └── outputs.tf              # Output values
├── website/
│   ├── templates/              # HTML templates
│   ├── static/                 # Static assets
│   ├── __init__.py             # App factory
│   ├── models.py               # Database models
│   ├── views.py                # Route handlers
│   ├── auth.py                 # Authentication
│   └── s3.py                   # S3 upload utility
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container definition
└── docker-compose.yml          # Local development setup
```

---

## Features

- User registration and authentication
- Log films with title, genre, star rating (1-10), and written review
- Upload custom movie posters stored on AWS S3
- Flip card interaction to reveal review text on hover
- Customizable diary title and hero background image per user
- Edit and delete existing reviews
- Responsive layout

---

## Notes

This project is intended as a portfolio piece demonstrating cloud engineering skills. The application itself serves as a vehicle for practising real infrastructure concepts: containerization, infrastructure as code, automated deployment pipelines, and production AWS setup with a custom domain and SSL certificate.