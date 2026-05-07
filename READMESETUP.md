## Setup
1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

## Run It
Start the dev server:
```bash
python manage.py runserver
```
Then open:
```text
http://127.0.0.1:8000
```

## Deployment Notes
- Static assets are collected using Django’s `collectstatic`.
- The `npm run build` command runs `python manage.py collectstatic --noinput`.
- `vercel.json` is included in case you deploy on Vercel.

## Project Layout
- `manage.py` — Django command utility
- `config/` — project settings and URL routing
- `main/` — app logic, views, URLs, models
- `templates/` — HTML pages
- `static/typeshift/` — game assets and styles
- `db.sqlite3` — local database file

## How It Works
- The landing screen lets you pick a genre and difficulty.
- Gameplay happens in the browser with a timer and multiple-choice questions.
- Scores are sent to the backend through a simple API.
- The leaderboard shows top scores per category.

## Ideas to Add Later
- User login and profiles
- More questions and topics
- Difficulty-based leaderboard filters
- Better mobile support and accessibility
- Extra sounds and animations

## Contributing
- Open issues for bugs or ideas
- Send PRs for improvements
- Keep updates focused on gameplay, polish, and responsiveness