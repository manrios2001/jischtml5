"""
Convert a presentation (PowerPoint or Impress) to a single HTML page, with semantic markup 
compatible with the J5Slide viewer.

Uses unoconv to convert PPT et al into HTML, but via a subprocess system call
TODO: Import unoconv directly via Python, and get it to restart OpenOffice when necessary

"""

from bs4 import BeautifulSoup as bs
import codecs
import subprocess
import os
import getopt, sys

def createSlides(dest):
    num = 0
    def filename():
        return os.path.join(dest, "text%s.html" % str(num))
    def imgHtmlFilename():
        return os.path.join(dest, "img%s.html" % str(num))
        
    #TODO, Add a standalone mode with embedded player <script type='text/javascript' src='./j5slide_embed.js'>
    slides = u"<html><head> <meta charset='UTF-8'></script></head><body>"

    while os.path.exists(filename()):
                raw = codecs.open(filename(),'r', 'utf-8').read()
                #Beautiful soup parser has trouble closing headings 
                # putting in paragraphs forces it to close them
                raw = raw.replace(u"<h", u"<p></p><h")
                raw = raw.                                                                                  replace(u"<body>", u"<body><section  typeof='http://purl.org/ontology/bibo/Slide'><object data='img%s.jpg'>" 
                                  % str(num))
                raw = raw.replace(u"</body>", u"</details></section></body>")
                raw = raw.replace(u"<h3>Notes:</h3>", u"</object><details open='open'>")       
                soup = bs(raw)
                soup.center.decompose() #get rid of navigation
                title = soup.title.string
                slide = soup.title.decompose()      
                #soup.section['title'] = title
                for item in soup.find_all(True):
                    if item.name == "p" and item.contents == []:
                        item.decompose()
                    elif item.get('style') <> None:
                        del item['style']  
                slides += soup.section.prettify()
                os.remove(filename())
                if os.path.exists(imgHtmlFilename()):
                    os.remove(imgHtmlFilename())
                num += 1
         
    slides += u"</body></html>"
    return slides

def convert(path, dest, destDir):
    #tempdir  = os.path.join(destDir, "temp")
    command = ["unoconv","-v", "-f", "html", "-e","IsExportNotes=True", "-o", destDir, path]   
    result = subprocess.call(command)
    #os.remove(tempFile)
    codecs.open(dest,'w', 'utf-8').write(createSlides(destDir))
    return result




    
def main():
    retVal = 0
    doc = None
    stdout = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:",
                 ["help"])
      
        for o, a in opts:       
            if o in ("-h", "--help"):	
                usage()
                sys.exit()

        if not len(args) or len(args) > 2:
            usage()
            sys.exit()
            
            
        #TODO - this is copied from WordDownOO - should put into a separate file
        path = args[0]
        path = os.path.abspath(path)
        dir, outFilename = os.path.split(path)
        filestem, ext = os.path.splitext(outFilename)
        if len(args) == 2:
            destDir = args[1]
            dest = os.path.join(destDir, filestem + ".html")
        else:
            destDir = os.path.join(dir,"_html", outFilename)
            dest = os.path.join(destDir,"index.html")
             
        if not os.path.exists(destDir):
            os.makedirs(destDir)
        convert(path, dest, destDir)
        
        
    except getopt.GetoptError,e:
        sys.stderr.write( str(e) + "\n" )
        usage()
        retVal = 1
        sys.exit(retVal)

if __name__ == "__main__":
    main()

