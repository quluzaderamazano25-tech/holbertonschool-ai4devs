# Data Model

## Entities

### 1. Project
- `id` (UUID): Unique identifier.
- `name` (String): Project name.
- `description` (Text): Business idea.

### 2. SchemaEntity
- `id` (UUID): Unique identifier.
- `project_id` (FK): Reference to Project.
- `name` (String): Entity name.

### 3. GeneratedCode
- `id` (UUID): Unique identifier.
- `project_id` (FK): Reference to Project.
- `language` (String): Programming language.