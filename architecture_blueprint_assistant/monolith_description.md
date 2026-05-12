# Monolithic Architecture

- **Frontend App**: Mobile and web interface where students and developers interact with the platform.
- **Authentication Module**: Manages user registration, login, sessions, and OAuth integration with GitHub.
- **Learning Roadmap Module**: Handles creation, editing, and retrieval of personalized learning roadmaps for each user.
- **Progress Tracking Module**: Records daily learning activity, calculates streaks, and updates progress dashboards.
- **AI Recommendation Module**: Analyzes user skill level and activity to generate personalized resource recommendations.
- **Goal Management Module**: Manages user-defined learning goals, deadlines, milestone tracking, and alert triggers.
- **GitHub Integration Module**: Connects to the GitHub API via OAuth to fetch commit history and reflect coding activity in progress scores.
- **Notification Service**: Sends in-app and push notifications for reminders, milestone alerts, and badge awards.
- **Database**: Central relational database storing all application data including users, roadmaps, progress logs, goals, and activity records.