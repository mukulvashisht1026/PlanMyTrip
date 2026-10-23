# django

## How to setup project?

```
cd django
pip install virtualenv
virtualenv env
source env/lib/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Offline demo and current completeness

Original entrypoint: manage.py (PlanMyTrip/settings.py). HomePage/views.py loads CSV data and calls an external route endpoint; the offline mock avoids both live services and legacy dependencies.

Offline travel filtering example. The explicit mock uses synthetic local data, makes no network calls, and does not persist changes. It is separate from the original implementation.

Requirements: Python 3.9+ and Make for the local example; Docker Engine for its container. Run from this repository root:

```sh
make demo
make check
make build
make run
```

The container runs the demo once and exits; it does not expose an HTTP port. First Docker build needs access to the Python base image. For remaining implementation work and known gaps, see [TODO.md](TODO.md). Original dependencies, service integration, and container runtime require separate validation.
