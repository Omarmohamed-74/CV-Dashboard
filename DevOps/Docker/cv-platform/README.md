# CVision — CV Processing Platform

A production-style CV processing platform built to simulate a real-world collaboration between Backend and DevOps teams.

The goal of this project is not only to build an application, but also to practice DevOps workflows including containerization, orchestration, CI/CD, monitoring, and scalable deployments.

---

# Current Features

- Upload CV files
- Store uploaded files
- Save metadata in PostgreSQL
- Dockerized FastAPI backend
- Multi-container setup with Docker Compose
- Environment variables management
- Persistent PostgreSQL volume

---

# Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL

## DevOps
- Docker
- Docker Compose

---

# Architecture

![Architecture](docs/'Untitled Diagram.drawio.png'.png)

---

# Project Structure

```text
cv-platform/
│
├── backend/
│   ├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── docker-compose.yml
├── .env
└── README.md
```

---

# Run Locally

## Clone repository

```bash
git clone <repo-url>
cd cv-platform
```

---

## Start services

```bash
docker compose up --build
```

---

# API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

---

# Next Steps

- Nginx reverse proxy
- Redis & background workers
- CI/CD pipeline using GitHub Actions
- Kubernetes deployment
- Monitoring with Prometheus & Grafana
- CV parsing & AI matching

---

# Goal

This project is being developed as a production-like system to practice real DevOps engineering workflows and infrastructure automation.
