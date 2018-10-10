# FilesToPdf

Code to convert multiple text files to pdf

> Tested in Python 3.7.0 on windows

 Need to install
----

**Windows**

```cmd
 python -m pip install pdfkit
```
    
and 

[dependency/wkhtmltox-0.12.5-1.msvc2015-win64.exe](dependency/wkhtmltox-0.12.5-1.msvc2015-win64.exe)

**Linux**

```sh
$ sudo pip install pdfkit
```
    
and 

```sh
$ sudo apt-get install wkhtmltopdf
```

 Configuration
----

Access the [ConfigFile.py](ConfigFile.py) file

Choose the extensions allowed

```py
 allow_extensions = ["txt", "php", "js", "html", "htm", "json"]
```
    
PDF Setup Page

```py
 options_pdf = { ...
```
    
And path of wkthmltopdf 

```py
 path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
```

 How to use
----

 - Execute "executar.cmd" file
 - Select source folder
 - Select destiny folder
 - Wait to convert
 - Done
 
 License
----

MIT

 Stackoverflow
----

[Help me improve my code](https://pt.stackoverflow.com/questions/333694/como-fazer-com-que-o-pdfkit-ignore-as-extens%C3%B5es/333706)
