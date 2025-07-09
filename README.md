# Task Manager - FastAPI + React

A modern task management application built with FastAPI backend and React frontend, featuring a clean and intuitive user interface for managing your daily tasks.

## 🚀 Features

### Backend (FastAPI)
- **RESTful API**: Complete CRUD operations for tasks
- **Pydantic Models**: Type-safe data validation
- **In-Memory Storage**: Simple and fast task storage
- **Auto-generated Documentation**: Interactive API docs at `/docs`

### Frontend (React)
- **Modern UI**: Clean, responsive design
- **Real-time Updates**: Instant task creation, updates, and deletion
- **Form Validation**: Client-side validation for better UX
- **Error Handling**: User-friendly error messages
- **Loading States**: Visual feedback during API calls

### Task Management Features
- ✅ Create new tasks with title and description
- ✅ Mark tasks as complete/incomplete
- ✅ Delete tasks
- ✅ View all tasks in a clean list
- ✅ Task count display
- ✅ Visual indicators for completed tasks

## 🛠️ Technology Stack

- **Backend**: FastAPI, Pydantic, Python 3.7+
- **Frontend**: React 18, Babel (CDN)
- **Styling**: CSS3 with modern design
- **Development**: Uvicorn server

## 📁 Project Structure

```
task_management/
├── main.py              # FastAPI backend application
├── static/
│   └── index.html       # React frontend application
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd task_management
   ```

2. **Install dependencies**
   ```bash
   pip install fastapi uvicorn
   ```

3. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

4. **Open your browser**
   Navigate to `http://localhost:8000`

## 📖 API Documentation

### Interactive API Docs
Visit `http://localhost:8000/docs` for interactive API documentation powered by Swagger UI.

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve the React frontend |
| `GET` | `/tasks` | Get all tasks |
| `POST` | `/tasks` | Create a new task |
| `PUT` | `/tasks/{task_id}` | Update an existing task |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

### Task Model
```python
{
    "id": int,           # Auto-generated unique identifier
    "title": str,        # Task title (required)
    "description": str,  # Task description (optional)
    "completed": bool    # Completion status (default: false)
}
```

## 💻 Usage

### Creating Tasks
1. Enter a task title (required)
2. Optionally add a description
3. Click "Add Task"

### Managing Tasks
- **Complete/Incomplete**: Click the green button to toggle task status
- **Delete**: Click the red "Delete" button to remove a task
- **View**: All tasks are displayed in a clean list format

### Visual Indicators
- ✅ **Completed tasks**: Strikethrough text and reduced opacity
- 📝 **Active tasks**: Normal appearance
- 🔢 **Task counter**: Shows total number of tasks

## 🔧 Development

### Backend Development
- **File**: `main.py`
- **Hot Reload**: Server automatically restarts on code changes
- **API Testing**: Use the interactive docs at `/docs`

### Frontend Development
- **File**: `static/index.html`
- **React CDN**: No build process required
- **Live Editing**: Modify the HTML file and refresh browser

### Adding New Features
1. **Backend**: Add new endpoints in `main.py`
2. **Frontend**: Update React components in `static/index.html`
3. **Styling**: Modify CSS within the `<style>` tag

## 🎨 Customization

### Styling
The application uses modern CSS with:
- Responsive design
- Clean color scheme
- Hover effects
- Smooth transitions

### Adding Static Files
Place additional files in the `static/` directory:
- CSS files: `static/style.css`
- JavaScript files: `static/script.js`
- Images: `static/images/`

## 🐛 Troubleshooting

### Common Issues

**Port already in use**
```bash
uvicorn main:app --reload --port 8001
```

**Module not found errors**
```bash
pip install -r requirements.txt
```

**Frontend not loading**
- Check browser console for errors
- Ensure all CDN links are accessible
- Verify the `static/index.html` file exists

## 📝 Requirements

Create a `requirements.txt` file:
```
fastapi>=0.68.0
uvicorn>=0.15.0
pydantic>=1.8.0
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- React team for the powerful frontend library
- The open-source community for inspiration

---

**Happy Task Managing! 🎉** 