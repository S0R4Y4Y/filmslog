# Filmslog 

A personal movie diary web app where users can log, rate, and review movies they've watched. Built as a cloud engineering portfolio project to demonstrate containerization, infrastructure as code, and CI/CD automation.

## What it does
- Log movies you've watched with title, genre, rating (1-10), and review
- Personal diary — each user has their own movie list
- User authentication (register/login)

## Tech Stack
| Layer | Technology |
|---|---|
| App | Python Flask |
| Database | SQLite |
| Containerization | Docker |
| Infrastructure | AWS (EC2, ECR, S3, VPC, IAM) |
| IaC | Terraform |
| CI/CD | GitHub Actions |

## Architecture
GitHub → GitHub Actions → Docker Build → AWS ECR → EC2  


## How to run locally
1. Clone the repo
```bash
   git clone https://github.com/S0R4Y4Y/filmslog.git
   cd filmslog
```

2. Run with Docker Compose
```bash
   docker-compose up --build
```

3. Open browser at `http://localhost:8080`

## Infrastructure (Terraform)
All AWS infrastructure is defined as code in the `infrastructure/` folder.

```bash
cd infrastructure
terraform init
terraform apply
```

Resources provisioned:
- VPC with public subnet, internet gateway, route tables
- EC2 instance (Amazon Linux 2023, t3.micro)
- ECR repository for Docker images
- S3 bucket with versioning
- IAM roles and instance profiles
- Security groups

## CI/CD Pipeline
On every push to `main`:
1. GitHub Actions triggers
2. Docker image built for `linux/amd64`
3. Image pushed to AWS ECR
4. EC2 pulls latest image and restarts container

## Why I built this
I wanted a place to remember how I felt about movies I've watched and used it as a vehicle to practice real cloud engineering: containerization, infrastructure as code, and automated deployments.
