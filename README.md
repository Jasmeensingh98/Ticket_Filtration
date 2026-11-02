# AI-Powered Helpdesk Ticket Prioritization and Routing System

A full-stack academic prototype for intelligent IT support triage, classification, routing, and analytics.

## Overview

The system demonstrates an end-to-end ticket lifecycle:

- User submits a ticket
- Backend preprocesses and analyzes text
- AI service predicts category and priority
- Smart routing assigns a team and agent
- Knowledge base returns recommended troubleshooting steps
- Agent resolves tickets and updates status
- Analytics dashboard tracks SLA and workload

## Tech Stack

- Frontend: React + Vite + Tailwind CSS + Recharts
- Backend: Flask + SQLAlchemy + Flask-JWT-Extended
- Database: PostgreSQL-ready SQLAlchemy model, SQLite fallback for local demo
- ML: Demo classification and priority prediction with modular BERT/XGBoost-ready structure

## Folder Structure

- /frontend
- /backend
- /database
- /ml
- /docs
- /.env.example
- /README.md

## Environment Variables

Copy .env.example to .env and update values.

```bash
cp .env.example .env
```

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/helpdesk
JWT_SECRET=change_me
SECRET_KEY=change_me
DEMO_MODE=true
EMAIL_API_KEY=
SLACK_WEBHOOK_URL=
MODEL_API_URL=
VITE_API_BASE_URL=http://localhost:5000/api
```

## Local Setup

### 1. Clone repository

```bash
git clone <repo-url>
cd filteration
```

### 2. Install backend dependencies

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Setup PostgreSQL

Create a PostgreSQL database named `helpdesk` and update `DATABASE_URL` in `.env`.

If you want a simpler local demo, keep the default SQLite configuration in `.env`.

### 4. Run backend

```bash
cd backend
python run.py
```

The backend will be available at:

- http://localhost:5000/api/health
- http://localhost:5000/api/docs

### 5. Install frontend dependencies

```bash
cd frontend
npm install
```

### 6. Run frontend

```bash
npm run dev
```

The frontend will be available at http://localhost:5173.

## Production Deployment

The current backend is PostgreSQL-ready and should be deployed with a managed PostgreSQL database. Do not use the local SQLite fallback for production.

### Backend

Deploy the `backend` directory as a Python web service on Render or Railway.

```text
Build command: pip install -r requirements.txt
Start command: gunicorn --bind 0.0.0.0:$PORT run:app
```

Set these backend environment variables in the hosting provider:

```env
DATABASE_URL=your-managed-postgresql-connection-string
JWT_SECRET=replace-with-a-long-random-secret
SECRET_KEY=replace-with-a-different-long-random-secret
DEMO_MODE=true
CORS_ORIGINS=https://your-frontend-domain.com
DEBUG=false
MAX_CONTENT_LENGTH=12582912
```

After deployment, verify `https://your-backend-domain.com/api/health` returns a JSON response with `"status": "ok"`.

### Frontend

Deploy the `frontend` directory as a Vercel or Netlify site.

```text
Build command: npm run build
Output directory: dist
```

Set this frontend environment variable before building:

```env
VITE_API_BASE_URL=https://your-backend-domain.com/api
```

Configure the frontend host to rewrite unknown paths to `index.html` so React Router pages continue to work after a browser refresh. After the frontend has a public URL, update the backend `CORS_ORIGINS` value to that exact URL and redeploy the backend.

### Production considerations

- Keep `.env` out of source control and configure secrets in the hosting provider.
- The current attachment endpoint writes files to the local `instance/uploads` directory. Use persistent disk storage or object storage such as S3 before relying on production attachments.
- Set `DEMO_MODE=false` only after production model artifacts or `MODEL_API_URL` are configured.
- From the `backend` directory, run `python verify_app.py` against the production-style environment before switching the frontend to the live API.

## Demo credentials

- User: user@demo.com / password
- Agent: agent@demo.com / password
- Admin: admin@demo.com / password

## API Documentation

Available at:

- /api/docs

## ML Integration Notes

The prototype includes a modular, researcher-friendly ML pipeline:

- /ml/preprocessing.py
- /ml/category_model.py
- /ml/priority_model.py
- /ml/evaluate.py

The code explicitly separates the demo fallback layer from the production model integration path. When `DEMO_MODE=false`, the application is designed to load actual trained model artifacts or a remote inference API.

## Sample API Requests

### Register

```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com","password":"password","role":"user"}'
```

### Login

```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@demo.com","password":"password"}'
```

### Create ticket

```bash
curl -X POST http://localhost:5000/api/tickets \
  -H "Content-Type: application/json" \
  -d '{"title":"VPN not connecting","description":"Users cannot connect to VPN from remote locations.","email":"user@demo.com","department":"IT Support"}'
```

## Deployment

### Frontend

Deploy the React app to Vercel or Netlify.

### Backend

Deploy Flask API to Render, Railway, or AWS.

### Database

Use PostgreSQL on Supabase, Neon, or a managed PostgreSQL service.

## Academic Research Notes

This project is intentionally designed as a research prototype with modular ML components and clear demo-mode labeling. Real models can be plugged in by replacing the demo prediction modules while keeping the rest of the platform unchanged.
