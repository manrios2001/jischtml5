For use in a Linux environment, WordDownOO.py is a script to automate OpenOffice or LibreOffice to open an office document, preprocess it, save it as HTML then run WordDown on the result


# Installation #

The following instructions are for Ubuntu.

  * Check out the JiscHTML tools:
```
    sudo mkdir /opt/jischtml5
    sudo chown $USER:$USER /opt/jischtml5
    git clone https://code.google.com/p/jischtml5/ /opt/jischtml5
```
  * Install dependencies:
```
   sudo apt-get install libreoffice phantomjs python-dev libxml2-dev libxslt1-dev python-pip
   pip install lxml
```
> > If you want to make EPUB books (via --epub), install calibre using the instructions [here](http://calibre-ebook.com/download_linux).
# Usage #
For help try:
```
python WordDownOO.py
```
To convert a document from Word or OpenDocument (odt) format to HTML
First, make sure LibreOffice is running:
```
 soffice  "-accept=socket,host=localhost,port=2002;urp;" --headless
```


```
  cd /opt/jischtml/tools/commandline
  python WordDownOO.py /path-to-document
```