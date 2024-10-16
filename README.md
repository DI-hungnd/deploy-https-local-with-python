## Quickstart
Install mkcert and generate a certificate for localhost
```

# git: https://github.com/FiloSottile/mkcert
# Install mkcert
sudo apt install libnss3-tools
curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64"
chmod +x mkcert-v*-linux-amd64
sudo cp mkcert-v*-linux-amd64 /usr/local/bin/mkcert

# Certificate Installation
mkcert -key-file key.pem -cert-file cert.pem localhost 127.0.0.1 ::1

# Copy cert and key to project directory
cp cert.pem key.pem </path/to/project>

# Install the local CA
mkcert -install
```

Install virtualenv and requirements
```
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

```


Run project
```
# cd </path/to/project>
python main.py
```

