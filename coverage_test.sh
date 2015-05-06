#!/bin/bash

rm -f .coverage
rm -rf htmlcov/
coverage run --omit='*/tests.py','ls */features/steps.py | tr "\n" ","' \
    --source=usuarios \
    manage.py harvest
echo "Test completed!"
echo "Generating HTML report..."
coverage html
echo "Console report:"
coverage report

