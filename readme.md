## **Blog App**

A full-stack blog application with **FastAPI** (Python) as the backend, **PostgreSQL** as the database, and **SvelteKit 5** as the frontend. The project is containerized using **Docker** and managed with **Docker Compose**.

---

## **Prerequisites**
Ensure your system meets the requirements for **Docker** installation.

### **Installing Docker**
#### **On Linux (Ubuntu)**
```sh
sudo apt update
sudo apt install -y docker.io
```

#### **On macOS (via Homebrew)**
```sh
brew install --cask docker
```

#### **On Windows**
Download and install **Docker Desktop** from [Docker's official website](https://www.docker.com/products/docker-desktop).

---

## **Installing Docker Compose**
```sh
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

---

## **Verify Installation**
### **Check if Docker is installed**
```sh
docker --version
```

### **Check if Docker Compose is installed**
```sh
docker-compose --version
```

### **Ensure Docker is running**
```sh
sudo systemctl start docker
```
To check the status:
```sh
sudo systemctl status docker
```

---

## **Project Structure**
```
blog-app/
│── backend/          # FastAPI backend
│   ├── app/          # Application code
│   ├── Dockerfile    # Backend Dockerfile
│   ├── requirements.txt # Python dependencies
│── frontend/         # SvelteKit 5 frontend
│   ├── src/          # Svelte app code
│   ├── Dockerfile    # Frontend Dockerfile
│── nginx/            # Reverse proxy
│   ├── nginx.conf    # Nginx config
│── docker-compose.yml  # Docker Compose file
│── README.md         # Documentation
```

---

## **Running the Project with Docker**
Navigate to the project directory and run:
```sh
docker-compose up -d
```

To check if all services are running:
```sh
docker ps
```
Ensure the following services are up:
- `nginx_proxy`
- `web-api`
- `pg_container`
- `web_frontend`

---

## **Backend (FastAPI + PostgreSQL + SQLAlchemy + Alembic)**

The backend is built using **FastAPI**, uses **PostgreSQL** as the database, and **SQLAlchemy** as the ORM. **Alembic** is used for database migrations.

### **Setting up the Backend**
#### **1. Navigate to the Backend Directory**
```sh
cd backend
```

#### **2. Create a virtual environment and install dependencies**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

#### **3. Set Up Environment Variables**
Create a `.env` file inside `backend/`:
```

POSTGRES_USER=postgres       
POSTGRES_PASSWORD=supersecret 
POSTGRES_DB=mydatabase      

POSTGRES_HOST=pg-container
POSTGRES_PORT=5432

```

#### **4. Run Alembic Migrations**
```sh
alembic upgrade head
```

#### **5. Run the Backend Locally**
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at:  
➡ **http://localhost:8000**

Swagger Docs:  
➡ **http://localhost:8000/docs**

---

## **Frontend (SvelteKit 5)**
The frontend is built using **SvelteKit 5**.

### **Setting up the Frontend**
#### **1. Navigate to the Frontend Directory**
```sh
cd frontend
```

#### **2. Install Dependencies**
```sh
npm install
```

#### **3. Run the Development Server**
```sh
npm run dev -- --host
```

The frontend will be available at:  
➡ **http://localhost:5173**

---

## **Database (PostgreSQL)**
The PostgreSQL database runs inside a Docker container.

### **Connect to the Database**
```sh
docker exec -it pg-container psql -U postgres -d blog_db
```

### **Run Queries**
```sql
SELECT * FROM blogs;
```

---

## **API Endpoints**
| Method  | Endpoint         | Description          | Auth Required |
|---------|-----------------|----------------------|--------------|
| `POST`  | `/users/register` | Register a new user | No |
| `POST`  | `/users/token`    | Login user          | No |
| `GET`   | `/blogs`         | Get all blogs       | No |
| `GET`   | `/blogs/{id}`    | Get a single blog   | No |
| `POST`  | `/blogs`         | Create a blog       | Yes |
| `PATCH` | `/blogs/{id}`    | Update a blog       | Yes |
| `DELETE`| `/blogs/{id}`    | Delete a blog       | Yes |

---

## **Deployment**
To deploy the app on a server:
1. Build the images:
   ```sh
   docker-compose build
   ```
2. Start the services:
   ```sh
   docker-compose up -d
   ```

---

### **Ready to run your own blog app?**  
Just clone this repo, start the services, and you're good to go!

