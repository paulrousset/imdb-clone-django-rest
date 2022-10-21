# :movie_camera: WATCHMATE API

IMDB Clone API built with Django Rest Framework

- Admin users can create and edit list of streaming platforms and related contents (movies, series, anime)
- Users can access the list of contents and create / edit related reviews

## :wrench: Run Locally

1. Clone the repo.
2. Make sure you have [poetry](https://python-poetry.org/) (python environment and dependency manager) installed.
3. In the project folder run `poetry install` to install dependencies.
4. Run `poetry shell` to open a new shell with all dependencies available.
5. Run `python manage.py runserver`
6. Check the links hereunder to interact with the API

## 🔗 Links

**1. Admin Access**

- Admin Section: [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)

**2. Accounts**

- Registration: [http://127.0.0.1:8000/api/account/register/](http://127.0.0.1:8000/api/account/register/)
- Login: [http://127.0.0.1:8000/api/account/login/](http://127.0.0.1:8000/api/account/login/)
- Logout: [http://127.0.0.1:8000/api/account/logout/](http://127.0.0.1:8000/api/account/logout/)

**3. Stream Platforms**

- Create Element & Access List: [http://127.0.0.1:8000/api/watchmate/stream/](http://127.0.0.1:8000/api/watchmate/stream/)
- Access, Update & Destroy Individual Element: [http://127.0.0.1:8000/api/watchmate/stream/<int:streamplatform_id>/ ](http://127.0.0.1:8000/api/watchmate/stream/<int:streamplatform_id>/)

**4. Watch List**

- Create & Access List: [http://127.0.0.1:8000/api/watchmate/](http://127.0.0.1:8000/api/watchmate/)
- Access, Update & Destroy Individual Element: [http://127.0.0.1:8000/api/watchmate/<int:movie_id>/](http://127.0.0.1:8000/api/watchmate/<int:movie_id>/)

**5. Reviews**

- Create Review For Specific Movie: [http://127.0.0.1:8000/api/watchmate/**_*int:movie_id*_**/reviews/create/](http://127.0.0.1:8000/api/watchmate/int:movie_id/reviews/create/)
- List Of All Reviews For Specific Movie: [http://127.0.0.1:8000/api/watchmate/**_*int:movie_id*_**/reviews/](http://127.0.0.1:8000/api/watchmate/int:movie_id/reviews/)
- Access, Update & Destroy Individual Review: [http://127.0.0.1:8000/api/watchmate/reviews/**_int:review_id_**/ ](http://127.0.0.1:8000/api/watchmate/reviews/int:review_id/)

**6. User Review**

- Access All Reviews For Specific User: Logout: [http://127.0.0.1:8000/api/watchmate/user-reviews/?username=example](http://127.0.0.1:8000/api/watchmate/user-reviews/?username=example)
