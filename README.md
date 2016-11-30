# BVGAnzeige
Kleines Projekt um in der WG die kommende Busse und S-Bahn zu sehen

<img src="images/example1.jpg" alt="Example1" style="width: 750;"/>

## Installation
1. Installiere Kivy, siehe https://kivy.org/docs/installation/installation.html
Falls du einen Raspberry PI benutzt, schau dir KivyPie an, da ist Kivy schon vorkonfiguriert.
2. Installiere bvg-grabber
~~~bash
sudo pip3 install bvg-grabber
~~~
3. Installiere Executor, damit der Bildschirm in der Nacht ausgeht(funktioniert zurzeit nur auf Linux)
~~~bash
sudo pip3 install executor
~~~
4. Bereinige Fehler in bvg-grabber
Suche die Dateien "actualdeparture.py" und "scheduleddeparture.py"
~~~bash
sudo find / -name "scheduleddeparture.py"
sudo find / -name "actualdeparture.py"
~~~
Veraendere die Zeilen in beiden Datein:
~~~python
soup = BeautifulSoup(response.text)
~~~
zu
~~~python
soup = BeautifulSoup(response.text, "lxml")
~~~
