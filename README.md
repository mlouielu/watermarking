Watermarking
============

Watermarking image with text



HOW-TO
------

Add watermark to image with text

```
$ python watermarking.py image.jpg "Void after 2021/08/01. Only for applying application." out.png
```

Change text rotation

```
$ python watermarking.py image.jpg "Void after 2021/08/01. Only for applying application." out.png --rotate 45
```


Change text density

```
$ python watermarking.py image.jpg "Void after 2021/08/01. Only for applying application." out.png --row-density 3 --col-density 4
```


Change text font size

```
$ python watermarking.py image.jpg "Void after 2021/08/01. Only for applying application." out.png --font-size 48
```
