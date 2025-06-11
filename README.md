# Habit Tracker

A Django-based web application for tracking habits and moods, helping you build better routines and monitor your emotional well-being.

## Features

### Habit Tracking
- Create and manage daily, weekly, or custom frequency habits
- Track habit completions with repetition counts
- View habit progress in calendar format
- Categorize habits (Health, Fitness, Learning, Personal)
- Set required repetitions for each habit
- Visual progress indicators

### Mood Tracking
- Record daily moods with intensity levels (0-10)
- Track emotional patterns over time
- Add notes to mood entries
- Modern card-based layout for mood history
- Visual intensity indicators
- Edit and delete mood entries

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/lush-is-him/habit_tracker.git
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

6. Visit `http://localhost:8000` in your browser

## Usage

### Habit Management
- Add new habits with custom frequencies and repetition requirements
- Track daily completions
- View progress in calendar format
- Edit or delete habits as needed

### Mood Tracking
- Record your daily mood with intensity level
- Add optional notes to each mood entry
- View your mood history in a clean, card-based layout
- Track emotional patterns over time
- Edit or delete previous mood entries

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 