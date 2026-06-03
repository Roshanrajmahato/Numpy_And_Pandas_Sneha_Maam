# Docker Setup Guide - MediCare Hospital Management System

## Overview
This guide will help you set up the MediCare Hospital Management System using Docker with PostgreSQL database.

## Files Included
- **Dockerfile** - Container image for Django application
- **docker-compose.yml** - Orchestration for Django + PostgreSQL + Nginx
- **requirements.txt** - Python dependencies
- **nginx.conf** - Nginx reverse proxy configuration
- **.env.example** - Environment variables template
- **.dockerignore** - Files to exclude from Docker build

## Prerequisites
- Docker (v20.10+) installed
- Docker Compose (v2.0+) installed
- Git

## Setup Instructions

### 1. Clone or Download the Project
```bash
cd "d:\Roshan raj Mahato\Desktop\Data Analytics\DJANGO_RAHUL_SIR\HospitalManagmentApp"
```

### 2. Create Environment File
Copy `.env.example` to `.env` and update with your settings:
```bash
cp .env.example .env
```

Edit `.env` file:
```
DEBUG=False
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DB_PASSWORD=your-secure-password
```

### 3. Update Django Settings
Edit `learning/settings.py` and update the DATABASES section:

**Replace:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**With:**
```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.getenv('DB_NAME', 'healthcare_db'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'secure_password_123'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

Also update ALLOWED_HOSTS:
```python
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-default-key')
```

### 4. Build and Start Services
```bash
# Build images
docker-compose build
docker compose build --no-cache
# Start services in background
docker-compose up -d
docker compose down 
# View logs
docker-compose logs -f

# Wait for all services to be healthy (2-3 minutes)
```

### 5. Run Initial Commands
```bash
# Create superuser
docker-compose exec web python manage.py createsuperuser

# Or if migrations are not run
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --noinput
```

### 6. Access the Application
- **Application**: http://localhost:8000
- **Nginx Proxy**: http://localhost (port 80)
- **Admin Panel**: http://localhost:8000/admin

## Services

### PostgreSQL Database
- **Container Name**: hospital_db
- **Port**: 5432
- **Default Credentials**:
  - Username: postgres
  - Password: secure_password_123 (change in .env)
  - Database: healthcare_db

### Django Application
- **Container Name**: hospital_app
- **Port**: 8000
- **Volumes**: 
  - Static files: /app/staticfiles
  - Media files: /app/media
  - Database backups: /backups

### Nginx Reverse Proxy
- **Container Name**: hospital_nginx
- **Port**: 80
- **Serves**: Static files, media, and proxies to Django

## Useful Docker Commands

### View Running Services
```bash
docker-compose ps
```

### View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f web
docker-compose logs -f db
docker-compose logs -f nginx
```

### Access Database
```bash
docker-compose exec db psql -U postgres -d healthcare_db
```

### Run Management Commands
```bash
# Migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Collect static files
docker-compose exec web python manage.py collectstatic --noinput

# Shell
docker-compose exec web python manage.py shell

# Create backup
docker-compose exec db pg_dump -U postgres healthcare_db > backups/backup_$(date +%Y%m%d_%H%M%S).sql
```

### Stop Services
```bash
# Stop (containers remain)
docker-compose stop

# Stop and remove containers
docker-compose down

# Stop and remove everything (including volumes)
docker-compose down -v
```

### Restart Services
```bash
docker-compose restart

# Restart specific service
docker-compose restart web
```

### Rebuild After Changes
```bash
# Update requirements.txt, then:
docker-compose build --no-cache
docker-compose up -d
```




# RDS Postgrel AWS Veri

You already restored the snapshot into `database-1`.
Now you need to verify whether the snapshot actually contains your old data.

### How Snapshot Restore Works in AWS

A snapshot restore:

* creates a full database instance
* with all tables/data present at snapshot time

It does NOT merge with your current DB.

---

### Step 1 — Connect to Restored Database

Run:

```bash id="jlwmta"
psql -h database-1.c3okskggy8yy.ap-south-1.rds.amazonaws.com -U postgres
```

Then list databases:

```sql id="jlwmtb"
\l
```

You may see:

* healthcare_db
* postgres
* template0
* template1

---

### Step 2 — Connect to Your Actual Database

```sql id="jlwmtc"
\c healthcare_db
```

---

### Step 3 — Check Tables

```sql id="jlwmtd"
\dt
```

---

### Step 4 — Check Data

Example:

```sql id="jlwmte"
SELECT COUNT(*) FROM auth_user;
```

or:

```sql id="jlwmtf"
SELECT * FROM auth_user LIMIT 5;
```

For your app tables:

```sql id="jlwmtg"
SELECT COUNT(*) FROM doctors_alldoctors;
```
To see all doctor details from the table, run:

```sql id="jlwmwe"
SELECT * FROM doctors_alldoctors;
```

---

### Better Formatted View

If output is too wide:

```sql id="jlwmwf"
\x
```

Then run again:

```sql id="jlwmwg"
SELECT * FROM doctors_alldoctors;
```


---

### If Data Exists

Your snapshot restore worked correctly.

Now point Django to this DB using:

```env id="jlwmth"
DB_HOST=database-1.c3okskggy8yy.ap-south-1.rds.amazonaws.com
```

Then restart Django.

---

### If No Data Exists

Then the snapshot itself did not contain the old data.

Check:

* snapshot creation time
* whether snapshot was taken before data insertion

---

### Check Available Snapshots

Go to:

```text id="jlwmti"
RDS → Snapshots
```

You may have:

* automated snapshots
* manual snapshots
* newer backups

Restore the latest snapshot containing your data.

---

### Important AWS Note

Snapshot restore does NOT automatically:

* reconnect Django
* overwrite current DB
* merge data

It only creates a separate DB instance from that backup point.

---

### Best Way to Verify Quickly

Inside PostgreSQL:

```sql id="jlwmtj"
SELECT table_name
FROM information_schema.tables
WHERE table_schema='public';
```

If you see all your Django tables:

* restore succeeded.

Then check row counts.


# Database Backup and Restore

### Backup Database
```bash
docker-compose exec db pg_dump -U postgres healthcare_db > backups/backup_$(date +%Y%m%d_%H%M%S).sql
```

### Restore Database
```bash
docker-compose exec -T db psql -U postgres healthcare_db < backups/backup_filename.sql
```

## Troubleshooting

### Port Already in Use
If ports 8000, 5432, or 80 are already in use:
1. Update `.env` file:
```
APP_PORT=8001
DB_PORT=5433
NGINX_PORT=8080
```
2. Restart services: `docker-compose down && docker-compose up -d`

### Database Connection Error
```bash
# Check database logs
docker-compose logs db

# Verify database is healthy
docker-compose exec db pg_isready -U postgres
```

### Static Files Not Showing
```bash
# Rebuild static files
docker-compose exec web python manage.py collectstatic --noinput

# Check volumes
docker volume ls | grep hospital
```

### Permission Errors
```bash
# Fix permissions
docker-compose exec web chmod -R 755 /app/media
docker-compose exec web chown -R www-data:www-data /app/media
```

### Clear Everything and Start Fresh
```bash
docker-compose down -v
docker system prune -a
docker-compose build --no-cache
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```


# To Get ssl_certificate ssl_certificate_key from Certbot

### 1. Point Domain to EC2

In your domain provider create:

| Type | Name | Value      |
| ---- | ---- | ---------- |
| A    | @    | 65.0.6.213 |
| A    | www  | 65.0.6.213 |

For:

```text id="g7h8i9"
aidoctorpneumoniadetections.online
```

---

### 2. Wait For DNS Propagation

Usually:

* 5 minutes to 1 hour

Test:

```bash id="j0k1l2"
ping aidoctorpneumoniadetections.online
```

Should resolve to:

```text id="m3n4o5"
65.0.6.213
```

---

### 3. Install Certbot ONLY

Run:

```bash id="p6q7r8"
sudo apt update
sudo apt install certbot -y
```

---

### 4. Use Standalone SSL Mode

Because Docker nginx already uses port 80.

Stop containers temporarily:

```bash id="s9t0u1"
docker compose down
```

Then generate SSL:

```bash id="v2w3x4"
sudo certbot certonly --standalone -d aidoctorpneumoniadetections.online -d www.aidoctorpneumoniadetections.online
```

---

### 5. Certificates Location

Certs will be stored in:

```text id="y5z6a7"
/etc/letsencrypt/live/aidoctorpneumoniadetections.online/
```

Files:

```text id="b8c9d0"
fullchain.pem
privkey.pem
```

---

### 6. Update nginx.conf For HTTPS

Add:

```nginx id="e1f2g3"
server {
    listen 443 ssl;
    server_name aidoctorpneumoniadetections.online www.aidoctorpneumoniadetections.online;

    ssl_certificate /etc/letsencrypt/live/aidoctorpneumoniadetections.online/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/aidoctorpneumoniadetections.online/privkey.pem;

    location / {
        proxy_pass http://django_app;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

---

### 7. Mount SSL Certificates Into Docker

In `docker-compose.yml`:

```yaml id="h4i5j6"
volumes:
  - /etc/letsencrypt:/etc/letsencrypt:ro
```

inside nginx service.

---

### 8. Start Docker Again

```bash id="k7l8m9"
docker compose up --build -d
```

---

### 9. Access Site

```text id="n0o1p2"
https://aidoctorpneumoniadetections.online
```

---

### Important

Do NOT run:

```bash id="q3r4s5"
sudo systemctl start nginx
```

because Docker nginx already owns port 80.

---

### Best Final Production Setup

```text id="t6u7v8"
Docker Compose
 ├── nginx
 ├── django/gunicorn
 └── postgres
```

This is the correct scalable architecture.

Replace ONLY this part:

```nginx id="a1b2c3"
server {
    listen 80;
    server_name _;
```

with this:

```nginx id="d4e5f6"
# =====================================
# HTTP → HTTPS REDIRECT
# =====================================

server {
    listen 80;
    server_name aidoctorpneumoniadetections.online www.aidoctorpneumoniadetections.online;

    return 301 https://$host$request_uri;
}

# =====================================
# HTTPS SERVER
# =====================================

server {
    listen 443 ssl;
    server_name aidoctorpneumoniadetections.online www.aidoctorpneumoniadetections.online;

    ssl_certificate /etc/letsencrypt/live/aidoctorpneumoniadetections.online/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/aidoctorpneumoniadetections.online/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;

    charset utf-8;
```

So your old:

```nginx id="g7h8i9"
server {
    listen 80;
    server_name _;
```

gets removed completely.

Everything BELOW this remains SAME:

```nginx id="j0k1l2"
# Static files with explicit caching
location /static/ {
```

and continues until the end.

---

Then update docker compose.

ONLY add:

```yaml id="m3n4o5"
- "443:443"
```

inside nginx ports.

AND add:

```yaml id="p6q7r8"
- /etc/letsencrypt:/etc/letsencrypt:ro
```

inside nginx volumes.

Final nginx service becomes:

```yaml id="s9t0u1"
nginx:
  image: nginx:alpine
  container_name: hospital_nginx

  ports:
    - "80:80"
    - "443:443"

  volumes:
    - ./nginx.conf:/etc/nginx/nginx.conf:ro
    - static_volume:/app/staticfiles:ro
    - media_volume:/app/media:ro
    - /etc/letsencrypt:/etc/letsencrypt:ro
```

Then run:

```bash id="v2w3x4"
docker compose down
```

```bash id="y5z6a7"
docker compose up --build -d
```

Then:

```bash id="b8c9d0"
docker ps
```

You should see:

```text id="e1f2g3"
0.0.0.0:443->443/tcp
```

Then open:

```text id="h4i5j6"
https://aidoctorpneumoniadetections.online
```



# Linux/Ubuntu system directory in  that stores configuration files.

It is located at the root (`/`) of the filesystem.



To see it from root:

```bash
cd /
ls
```

You will see folders like:

```bash
bin  boot  dev  etc  home  lib  root  usr  var
```
You can go there using:

```bash
cd /etc
```
So your certificate path:

```bash
/etc/letsencrypt/live/aidoctorpneumoniadetections.online/
```

means:

* `/` → root directory
* `etc` → configuration folder
* `letsencrypt` → Certbot SSL files
* `live` → active certificates
* `aidoctorpneumoniadetections.online` → your domain certificate folder

To directly open it:

```bash
cd /etc/letsencrypt/live/aidoctorpneumoniadetections.online/
```

If permission is denied:

```bash
sudo su
cd /etc/letsencrypt/live/aidoctorpneumoniadetections.online/
```

