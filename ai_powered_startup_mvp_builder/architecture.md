# System Architecture

## High-Level System Diagram
```mermaid
graph TD
    A[User Interface - React] -->|Submits Requirements| B[API Gateway]
    B -->|Forwards Task| C[AI Engine - LLM]
    C -->|Returns Structure| D[Code Generator Service]
    D -->|Saves Metadata| E[(PostgreSQL Database)]
    D -->|Provides ZIP| A