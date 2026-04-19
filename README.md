# Two-Tier Web Application with Docker and Jenkins

## Overview

This project demonstrates a two-tier containerized web application using Flask and MySQL. Docker Compose is used to orchestrate services, and Jenkins can be integrated for CI/CD automation.

## Architecture

Flask Web Application ↔ MySQL Database

## Tech Stack

* Python Flask
* MySQL
* Docker
* Docker Compose
* Jenkins
* GitHub

## Features

* Multi-container deployment
* Database initialization with SQL script
* Service communication using Docker networking
* Easy local setup
* CI/CD ready structure

## Project Structure

app/ - Flask source code
db/ - SQL initialization script
Dockerfile - Build app image
docker-compose.yml - Multi-container orchestration

## Run Locally

docker compose up --build

## Access Application

http://localhost:5000

## Future Enhancements

* Jenkins pipeline automation
* Nginx reverse proxy
* AWS EC2 deployment
* Monitoring with Prometheus
