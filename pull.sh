#!/bin/bash
cd /home/denis/module_menu_app  || exit 1
#git pull --ff-only https://github.com/Tryd0g0lik/module_menu_app.git tests  || exit 1
# git pull https://github.com/Tryd0g0lik/module_menu_app.git tests  || exit 1
git fetch https://github.com/Tryd0g0lik/module_menu_app.git tests
#git reset --hard https://github.com/Tryd0g0lik/module_menu_app.git origin/test
git add * || exit 1
git commit -m "Update" || exit 1
sudo systemctl restart gunicorn  || exit 1
echo "Deployment completed successfully"

