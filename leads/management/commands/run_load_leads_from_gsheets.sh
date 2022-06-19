#!/bin/bash
cd $HOME/beinmarketscrm
source $HOME/beinmarketscrm/venv/bin/activate
export GOOGLE_API_KEY=AIzaSyC5CQfVlRKGeVOVUqFhVnI8IF0vVo06gH0
export READ_DOT_ENV_FILE=True
python manage.py load_leads_from_gsheets