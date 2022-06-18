#!/bin/bash
cd $HOME/kingcrm
source $HOME/.local/share/virtualenvs/kingcrm-EZ-qjEbz/bin/activate
export GOOGLE_API_KEY=AIzaSyD8lNEjfyY6APNWikfqB6FfyOLfk4pb-M0
export READ_DOT_ENV_FILE=True
python manage.py load_leads_from_gsheets
