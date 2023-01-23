# ownclouduploader
Bot De Telegram : OwnCloudUploader, Descargador gratis de contenido desde internet a hacia owncloud , nexcloud en cuba

# Deploy Usando Git Win Y Heroku Cli Desde PC
```
(CMD)
git clone https://github.com/ObisoftDev/ownclouduploader 
git init
git add .
git commit -m "OK"
heroku create myherokuapp
heroku git:remote myherokuapp
git push heroku master
```

# Comandos En El Bot (Usuarios Nomales)
```/start : Inicar Bot , Te Da La info
/ls : obtiene los archivos del root
/rm : remueve un archivo del root (index,range)
/zip : comprime un archivo del root (index,splitsize)
/upload : sube un o varios archivo a la nube (index,range)
/listenup : sube uno o varios archivos espera a q se borre el anterior de la nube (index,range)
```

# Deploy Directo (Heroku)
[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ObisoftDev/ownclouduploader)
