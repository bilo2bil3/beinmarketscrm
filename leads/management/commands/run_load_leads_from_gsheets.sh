#!/bin/bash
cd $HOME/beinmarketscrm
source $HOME/beinmarketscrm/venv/bin/activate
export GOOGLE_API_KEY=AIzaSyD8lNEjfyY6APNWikfqB6FfyOLfk4pb-M0
export READ_DOT_ENV_FILE=True
python manage.py load_leads_from_gsheets