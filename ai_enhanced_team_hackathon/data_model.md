# Data Model

## Entities

### 1. User Profile
- `user_id` (UUID): Unique identifier for the user.
- `full_name` (String): The name of the user.
- `current_skills` (List): A collection of identified skills.
- `target_role` (String): The job title the user aims for.

### 2. CareerGoal
- `goal_id` (UUID): Unique identifier for the career path.
- `user_id` (FK): Reference to the User Profile.
- `roadmap_steps` (JSON): A series of AI-generated milestones.
- `status` (String): Current progress (In-progress, Completed).

### 3. Resource
- `resource_id` (UUID): Unique identifier for a learning link.
- `title` (String): Title of the course or article.
- `url` (String): The web link to the resource.
- `type` (String): Category (Video, Book, Documentation).