# Architecture Plan

## System Overview
The AI Career Coach is built on a modular microservices architecture to ensure scalability and ease of AI integration.

### Core Components
- **Client Application**: A responsive web interface built with React for user interactions and progress visualization.
- **Backend API**: A Python-based FastAPI server that handles logic, user authentication, and data management.
- **AI Processing Layer**: An integration with OpenAI's API to analyze resumes and generate career roadmaps.
- **Database Layer**: PostgreSQL for structured data storage (Users, Goals) and Redis for caching AI responses.



### Technology Stack
- **Frontend**: React, Tailwind CSS.
- **Backend**: Python (FastAPI).
- **Database**: PostgreSQL.
- **AI**: GPT-4 model via API.
- **Storage**: AWS S3 for hosting resumes.