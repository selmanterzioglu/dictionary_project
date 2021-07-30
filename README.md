Program Gereksinimleri 

Linux bilgisayarlarda alınan "Pyperclip could not find a copy/paste mechanism for your system. " hatası için aşağıdaki  paketlerden birisi  kullanılmalıdır. 

Geliştiricinin kullanıdığı  paket:

sudo apt-get install xclip

Diğer Paketler:

sudo apt-get install xsel to install the xsel utility.
sudo apt-get install xclip to install the xclip utility.
pip install gtk to install the gtk Python module.
pip install PyQt4 to install the PyQt4 Python module.

Kaynak: 
https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error

Program gereksinimleri requirements.txt dossyasında mevcuttur. venv için kullanılmalıdır !
