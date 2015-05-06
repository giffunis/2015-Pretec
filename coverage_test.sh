#!/bin/bash

rm -f .coverage
rm -f db/test-database.db
rm -rf htmlcov/
python manage.py syncdb --settings=test_settings
coverage run --omit=`ls */features/steps.py | tr "\n" ","` \
    --source=User,frontend,Message,Micropost,Photo \
    manage.py harvest --settings=test_settings
echo "Cleaning test database..."
rm db/test-database.db
echo "Test completed!"
echo "Generating HTML report..."
coverage html
echo "Console report:"
coverage report

