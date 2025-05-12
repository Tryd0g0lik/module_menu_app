#!/bin/bash
cd /home/denis/module_menu_app  || exit 1
git pull --ff-only https://github.com/Tryd0g0lik/module_menu_app.git tests  || exit 1
sudo systemctl restart gunicorn  || exit 1
echo "Deployment completed successfully"

