# Microservices Architecture

- **API Gateway**: Single entry point for all client requests. Routes traffic to the appropriate microservice and handles rate limiting and load balancing.
- **Auth Service**: Manages user registration, login, session tokens, and GitHub OAuth authentication. Maintains its own isolated Auth DB.
- **Roadmap Service**: Handles creation, retrieval, and updates of personalized learning roadmaps. Each roadmap and its topics are stored in a dedicated Roadmap DB.
- **Progress Service**: Records daily learning activity, calculates streaks, and updates user dashboards. Publishes activity events to the Message Broker to trigger notifications.
- **AI Recommendation Service**: Analyzes user skill level and learning history to generate personalized resource suggestions. Uses a dedicated ML Model Store for inference.
- **Goal Service**: Manages user-defined learning goals, deadlines, and milestone tracking. Publishes milestone events to the Message Broker when thresholds are reached.
- **GitHub Integration Service**: Connects to the GitHub API to fetch commit history and coding activity. Stores activity summaries in a dedicated Activity DB and publishes updates to the Message Broker.
- **Notification Service**: Consumes events from the Message Broker and delivers in-app alerts, push notifications, and email reminders via an external Email/Push Provider.
- **Leaderboard Service**: Aggregates weekly activity scores across users and maintains ranked leaderboard data in its own Leaderboard DB.
- **Message Broker**: Decouples services by routing asynchronous events between Progress Service, Goal Service, GitHub Integration Service, and Notification Service.