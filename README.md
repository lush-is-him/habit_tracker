# Habit Tracker

A Django-based web application for tracking daily and weekly habits, with mood tracking features.

## Features

- Track daily and weekly habits
- Visual progress tracking with animated progress bars
- Mood tracking with detailed emotion categories
- Responsive design for all devices
- Local storage for habit completions
- Server-side persistence of habit data

## Technologies Used

- Django 5.2
- Python
- HTML5/CSS3
- JavaScript
- SQLite (development)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/habit_tracker.git
cd habit_tracker
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

6. Visit http://127.0.0.1:8000/ in your browser

## Usage

1. Add new habits with specific frequencies (daily or weekly)
2. Track habit completions using the interactive interface
3. Monitor progress with visual progress bars
4. Record your mood and track emotional patterns
5. View your habit and mood history

## Contributing

Feel free to submit issues and enhancement requests! 