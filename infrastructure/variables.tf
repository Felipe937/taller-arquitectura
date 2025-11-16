variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
  default     = "tu-project-id"
}

variable "region" {
  description = "Google Cloud region"
  type        = string
  default     = "us-central1"
}

variable "database_tier" {
  description = "Tier de la base de datos"
  type        = string
  default     = "db-f1-micro"
}
