# API Requirements - TaskMaster API

## Domain
AI-powered project management platform for developers and team leads to manage tasks, track progress, assign work, and collaborate efficiently through a RESTful API.

## Target Users
- **Developers**: create and manage personal tasks, update task status, and track daily progress through API integrations
- **Team Leads**: assign tasks to team members, monitor project progress, and generate performance reports
- **Admins**: manage user accounts, configure team settings, and access platform-wide analytics

## Core Operations
- Register a new user and return a JWT token
- Authenticate user and return JWT token
- Create a new task with title, description, deadline, priority, and assignee
- Get a task by ID
- Update task details including status, priority, and assignee
- Delete a task by ID
- List all tasks with optional filters by status, priority, and assignee
- Create a new project with name, description, and deadline
- Get a project by ID with all associated tasks
- Update project details including name, description, and status
- Delete a project by ID
- Assign a task to a team member by user ID
- Get all tasks assigned to a specific user
- Search tasks by keyword in title or description

## Data Rules
- Email must be unique and in valid format
- Password must be at least 8 characters with one uppercase letter and one number
- Task title must be between 3 and 100 characters and must not be empty
- Task priority must be one of: low, medium, high, or critical
- Task status must be one of: todo, in_progress, or done
- Deadline must be a valid ISO 8601 date and must not be in the past
- Project name must be unique per user account
- Assignee must reference an existing registered user in the system

## Non-Functional
- Response time under 200ms for all read endpoints under normal load
- JWT authentication required for all endpoints except register and login
- Rate limit of 100 requests per minute per authenticated user
- All data transmitted over HTTPS
- API versioning via URL prefix: /api/v1/
- Passwords must be hashed using bcrypt before storage
- All list endpoints must support pagination with default page size of 20