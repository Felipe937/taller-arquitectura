# Configuración del provider Google Cloud
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.80.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

# Base de datos Cloud SQL para EventFlow
resource "google_sql_database_instance" "eventflow_db" {
  name             = "eventflow-database"
  database_version = "POSTGRES_14"
  region           = var.region

  settings {
    tier = "db-f1-micro"
    
    ip_configuration {
      ipv4_enabled = true
    }
  }
}

resource "google_sql_database" "eventflow" {
  name     = "eventflow"
  instance = google_sql_database_instance.eventflow_db.name
}

# Bucket de almacenamiento para archivos estáticos
resource "google_storage_bucket" "eventflow_static" {
  name          = "${var.project_id}-eventflow-static"
  location      = var.region
  force_destroy = true
}

# Cloud Run para el servicio principal
resource "google_cloud_run_service" "eventflow_api" {
  name     = "eventflow-api"
  location = var.region

  template {
    spec {
      containers {
        image = "gcr.io/${var.project_id}/eventflow:latest"
        
        env {
          name  = "DATABASE_URL"
          value = "postgresql://${google_sql_database.eventflow.name}"
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Permitir acceso público a la API
resource "google_cloud_run_service_iam_member" "public_access" {
  service  = google_cloud_run_service.eventflow_api.name
  location = var.region
  role     = "roles/run.invoker"
  member   = "allUsers"
}

output "api_url" {
  value = google_cloud_run_service.eventflow_api.status[0].url
}
