# BVGAnzeige
BVGAnzeige fuer die WG

## Installation

~~~bash
sudo pip3 install Cython
sudo pip3 install kivy
sudo pip3 install executor
sudo pip3 install bvg-grabber
~~~

### Fehler in BeautifulSoup bereinigen
Veraendere die Zeile:
~~~python
soup = BeautifulSoup(response.text)
~~~
zu
~~~python
soup = BeautifulSoup(response.text, "lxml")
~~~
in
~~~bash
sudo find / -name "scheduleddeparture.py"
vim scheduleddeparture.py
sudo find / -name "actualdeparture.py"
vim actualdeparture.py
~~~







