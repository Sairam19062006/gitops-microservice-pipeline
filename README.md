# Production-Ready GitOps Microservice Pipeline

A lightweight, production-grade GitOps Continuous Integration and Continuous Delivery (CI/CD) pipeline designed with a zero-local-overhead architecture. 

This project demonstrates automated containerization, vulnerability security scanning, declarative Kubernetes deployments, and automated GitOps reconciliation using GitHub Actions, Docker Hub, Trivy, and ArgoCD.

---

## 🏗️ Architecture & Data Flow

[ Linux Mint Workstation ]
        │
        │ 1. Code / Manifest Update (git push)
        ▼
[ GitHub Repository ]
        │
        │ 2. Triggers Event Workflow
        ▼
[ GitHub Actions Cloud Runner ]
        ├─► Action A: Security Scan via Aquasecurity Trivy
        ├─► Action B: Build Multi-Stage Docker Image
        └─► Action C: Push Tagged Image to Registry
        │
        │ 3. Artifact Pushed
        ▼
[ Docker Hub Registry ]
        ▲
        │ 4. Pulls Latest Container Image
        │
[ ArgoCD GitOps Engine ]
        ▲
        │ 5. Continuously Polls Manifests for Drift
        │
[ GitHub Repository (k8s/ directory) ]
        │
        │ 6. Executes Rolling Update
        ▼
[ Kubernetes Cluster (Production Pods) ]

---

## 🛠️ Tech Stack & Key Components

* Application Layer: Lightweight Python HTTP service.
* Containerization: Multi-stage, security-hardened Dockerfile running with a non-root execution context (USER 10001).
* Version Control: GitHub.
* Continuous Integration (CI): GitHub Actions.
* Security & Vulnerability Scanning: Aquasecurity Trivy (scans base images & dependencies for CRITICAL/HIGH CVEs).
* Artifact Registry: Docker Hub.
* Continuous Delivery (CD): ArgoCD (Pull-based GitOps Engine with self-healing capabilities).
* Orchestration: Kubernetes (Deployments, Services, NodePort exposure).

---

## 📂 Repository Structure

gitops-microservice-pipeline/
├── .github/
│   └── workflows/
│       └── ci-pipeline.yml     # Automated CI & Security Scanning Pipeline
├── k8s/
│   ├── deployment.yaml         # Kubernetes Deployment Manifest
│   ├── service.yaml            # Kubernetes Service Manifest (NodePort)
│   └── argocd-app.yaml         # Declarative ArgoCD Application Specification
├── app.py                      # Application Source Code
├── Dockerfile                  # Multi-stage Container Definition
└── README.md                   # Project Documentation

---

## 🚀 Key Features

1. GitOps Single Source of Truth: All infrastructure and deployment states are version-controlled in Git.
2. Automated Security Gates: Integrated Trivy container scanning in the CI pipeline automatically flags insecure dependencies before deployment.
3. Pull-Based Continuous Deployment: ArgoCD runs inside the Kubernetes cluster and pulls updates, eliminating the need to expose cluster admin credentials to external CI runners.
4. Self-Healing Infrastructure: ArgoCD automatically detects and reverses any manual cluster configuration drift to match the Git repository state.
5. Resource-Efficient Workflow: Offloads heavy container builds and cluster execution to cloud runners and cloud sandboxes, eliminating high CPU/RAM load on the developer workstation.

---

## 🔒 Security Best Practices Implemented

* Non-Root Execution: Containers run as restricted user 10001 rather than root.
* Minimal Base Images: Built using python:3.11-slim to reduce the attack surface.
* Automated CVE Scanning: Pre-build security analysis integrated into every GitHub push.
