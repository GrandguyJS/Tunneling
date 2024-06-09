# About the project
Tunneling is an open-source, self hostable alternative to file-sharing services.

It enables you to share and download files easily with friends, all in a simple UI. You can setup accounts to view and delete the files all within the website.

Simple configuration and install

1. Install Python
```
sudo apt install python3-pip
```
2. Clone this repository
```
git clone https://github.com/GrandguyJS/Tunneling
```
3. Navigate to Tunneling
```
cd Tunneling
```
4. Run the web-app
```
sudo ./install.sh
```
5. Start in stop with
```
sudo systemctl start/stop tunneling
```

## Further configuration

1. SSL-encryption

Please use a reverse-proxy like NGINX or caddy to setup. You will also need a domain. (Tutorial for NGINX: [DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04))

2. Changing ports

If you want to change the port the gunicorn service will run on, you will 

Contributed by Timol44
