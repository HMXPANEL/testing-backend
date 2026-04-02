# AI Agent Brain - Full Stack Multi-Agent Backend

A production-ready, fully asynchronous multi-agent autonomous AI backend optimized for Render deployment. This system features a continuous cognition loop, advanced multi-layer memory, and a secure tool execution environment.

## 🚀 Key Features

- **Multi-Agent Architecture**: Specialized agents (Controller, Planner, Executor, Critic, Memory) collaborating to achieve complex goals.
- **Advanced Cognition Loop**: Implements a continuous **Observe-Think-Reason-Plan-Act-Observe-Reflect-Learn** loop.
- **Hybrid Memory System**: Uses **ChromaDB** for semantic long-term memory and **SQLite** for episodic and structured data.
- **Secure Tool System**: Sandboxed execution for Web, File, Shell, and Android control tools with a built-in safety layer.
- **Real-Time Android Control**: WebSocket-based screen streaming and command execution for remote Android device control.
- **Render Optimized**: Pre-configured `requirements.txt` and environment settings for seamless deployment on Render.

## 📁 Project Structure

```text
backend/
├── app/
│   ├── api/            # FastAPI routes and WebSocket handlers
│   ├── core/           # Core agent logic and task management
│   ├── models/         # Pydantic schemas and agent state
│   ├── services/       # External service integrations (LLM, Voice)
│   ├── tools/          # Tool registry and individual tool implementations
│   ├── utils/          # Logging and utility functions
│   ├── config.py       # Application configuration
│   └── main.py         # FastAPI application entry point
├── data/               # Persistent storage for SQLite and ChromaDB
├── sandbox/            # Restricted directory for file and shell operations
├── .env.example        # Template for environment variables
├── requirements.txt    # Pinned dependencies for production
└── README.md           # Project documentation
```

## 🛠️ Deployment on Render

1.  **Create a New Web Service**: Connect your repository to Render.
2.  **Environment Variables**: Add all variables from `.env.example` to the Render dashboard.
3.  **Build Command**: `pip install -r requirements.txt`
4.  **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5.  **Disk (Optional)**: For persistent memory, attach a Render Disk and update `SQLITE_DB_PATH` and `CHROMA_DB_PATH` to point to the mount path.

## 📱 Android Integration

The system includes a dedicated WebSocket endpoint at `/ws/device` for connecting an Android device. 
- **Secret Key**: Use the `ANDROID_WEBSOCKET_SECRET` for authentication.
- **Capabilities**: Supports real-time screen streaming (base64) and remote commands (tap, swipe, type, open_app).

## 📄 License

MIT License
