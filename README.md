# FilesToPdf

Code to convert multiple text files to pdf

> Tested in Python 3.7.0 on windows

 Need to install
----

```cmd
 python -m pip install pdfkit
```
    
and 

```cmd
 dependency/wkhtmltox-0.12.5-1.msvc2015-win64.exe
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

[Help me improve my code](https://pt.stackoverflow.com/questions/333694/como-fazer-com-que-o-pdfkit-ignore-as-extens%C3%B5es/333706?noredirect=1#comment675052_333706)
