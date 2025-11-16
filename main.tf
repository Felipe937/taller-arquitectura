# Archivo: main.tf
#
# Configuración de Terraform para el Taller de Arquitectura
# ¡OJO! Esto es solo para demostración en Cloud Shell.
# No creará recursos reales a menos que se aplique (no lo haremos).

terraform {
  required_providers {
    # Usaremos el proveedor de Google Cloud
    google = {
      source  = "hashicorp/google"
      version = "5.10.0"
    }
  }
}

provider "google" {
  project = "mi-proyecto-taller" # Placeholder - se reemplaza en Cloud Shell
  region  = "us-central1"
  zone    = "us-central1-c"
}

# Definición de "infraestructura como código"
# 1. Una red virtual para nuestra app
resource "google_compute_network" "vpc_network" {
  name                    = "taller-arquitectura-vpc"
  auto_create_subnetworks = true
  description             = "VPC para la aplicación EventFlow"
}

# 2. Una regla de firewall para permitir tráfico web (HTTP)
resource "google_compute_firewall" "allow_http" {
  name    = "taller-firewall-allow-http"
  network = google_compute_network.vpc_network.name
  
  allow {
    protocol = "tcp"
    ports    = ["80", "443"] # Puertos HTTP y HTTPS
  }
  
  source_ranges = ["0.0.0.0/0"] # Permitir desde cualquier IP
  description   = "Permitir tráfico web desde internet"
}

# 3. Un servidor web (máquina virtual) para EventFlow
resource "google_compute_instance" "web_server" {
  name         = "eventflow-web-server"
  machine_type = "e2-micro" # Una máquina pequeña y barata
  zone         = "us-central1-c"
  
  tags = ["http-server", "https-server"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 10
      type  = "pd-standard"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.name
    
    access_config {
      # Asigna una IP pública automáticamente
      network_tier = "STANDARD"
    }
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y nginx
    systemctl start nginx
    systemctl enable nginx
    echo "<h1>¡EventFlow funcionando en GCP!</h1>" > /var/www/html/index.html
    echo "<p>Desplegado con Terraform e IaC</p>" >> /var/www/html/index.html
  EOF

  service_account {
    scopes = ["cloud-platform"]
  }
}

# 4. Outputs para ver información después del despliegue
output "web_server_ip" {
  value = google_compute_instance.web_server.network_interface[0].access_config[0].nat_ip
  description = "IP pública del servidor web"
}

output "vpc_network_name" {
  value = google_compute_network.vpc_network.name
  description = "Nombre de la VPC creada"
}
