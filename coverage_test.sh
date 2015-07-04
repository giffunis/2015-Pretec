#!/bin/bash

rm -f .coverage
rm -rf htmlcov/
echo "Erasing previously collected data"
coverage erase
echo "Running coverage"
coverage run --omit='*/__init__.py','*/admin.py','*/views.py','*/forms.py','*/migrations/*.py','*/tests.py','ls */features/steps.py | tr "\n" ","' \
    --source=usuarios,microposts \
    manage.py harvest
echo "Test completed!"
echo "Generating HTML report..."
coverage html
echo "Console report:"
coverage report
