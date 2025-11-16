output "database_instance" {
  value = google_sql_database_instance.eventflow_db.name
}

output "static_bucket" {
  value = google_storage_bucket.eventflow_static.name
}

output "api_endpoint" {
  value = google_cloud_run_service.eventflow_api.status[0].url
}
