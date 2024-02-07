sudo pip3 install -r requirements.txt
sudo cp ecg.ini /etc/uwsgi/apps/
sudo cp agents_ecg.conf /etc/supervisor/conf.d/
sudo cp agents_ecg_nginx.conf /etc/nginx/sites-enabled/
sudo supervisorctl update
sudo systemctl restart nginx
sudo certbot --nginx -d ecg.medsenger.ru
touch config.py
