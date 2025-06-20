# Lern-Periode 10

25.4 bis 27.6

## Grob-Planung

1. Welche Programmiersprache möchten Sie verwenden? Was denken Sie, wo Ihre Zeit und Übung am sinnvollsten ist?
   In dieser LP möchte ich hauptsächlich Python benutzen da ich in meinem Projekt ML benutzen möcht.
   
1. Welche Datenbank-Technologie möchten Sie üben? Fühlen Sie sich sicher mit SQL und möchten etwas Neues ausprobieren; oder möchten Sie sich weiter mit SQL beschäftigen?
   Mit SQL fühle ich mich schon ziemlich gut und werde in dieser LP MongoDB lernen und verwenden
   
1. Was wäre ein geeignetes Abschluss-Projekt?
   Ich möchte eine APP machen die dem User ein geeignetes Auto vorschlägt, basierent auf Antworten des User auf Fragen vom Programm.

## 25.4

Welche 3 *features* sind die wichtigsten Ihres Projektes? Wie können Sie die Machbarkeit dieser in jeweils 45' am einfachsten beweisen?

- [x] Frage-Antwort-System zur Nutzerprofil-Erstellung(4 provisorische Fragen)
- [x] Maschinelles Lernmodell (Kleines Modell mit wenig Daten)
- [ ] Ein MongoDB Datenbank erstellen


Heute habe ich getestet, ob mein Projekt umsetzbar ist, mit mein Wissen, in dem ich die wichtigsten Features mit kleinen Prototypen getestet habe. Ich konnte leider nur zwei von drei Projekte fertigstellen, da es beim ML Komplikationen gab. Ich habe im Internet recherchiert und konnte alle Probleme lösen und einen Modell trainieren mit einem sehr kleinen Datensatz. Zum Erstellen von DB in MongoDB bin ich noch nicht gekommen und werde es das nächste Mal fertigstellen.

## 2.5

Ausgehend von Ihren Erfahrungen vom 25.4, welche *features* brauchen noch mehr Recherche? (Sie können auch mehrere AP für ein *feature* aufwenden.)

- [x] Ein MongoDB Datenbank erstellen
- [x] Ein Datensatz für mein Projekt suchen oder selber erstellen
- [ ] Den Datensatz in py einlesen und vorbereiten für ein Random Forest
- [x] Wichtigsten Punkte für eine Vorhersage wählen und die Fragen welche gestellt werden sollen überlegen (📵)

Heute habe ich als erstes die Machbarkeit des letzten Feature bewisen in dem ich ein MongoDB Datenbank erstellt habe. Danach habe ich mit Hilfe von KI ein Datensatz für mein ML Projekt erstellt. Diesen Datensatz habe ich mit pymongo in meine Datenbakn gespeichert. Später habe ich dann die Daten von meiner MongoDB DB in python mit pandas gespeichert und kann sie nun verwenden um mein ML Modell zu trainieren.

## 9.5

Planen Sie nun Ihr Projekt, sodass die *Kern-Funktionalität* in 3 Sitzungen realisiert ist. Schreiben Sie dazu zunächst 3 solche übergeordneten Kern-Funktionalitäten auf: 

1. ML Modell Trainieren
2. Daten von MongoDB lesen, verändern, löschen und hinzufügen
3. In console Nach Daten fragen und verwenden um eine Vorhersage zu treffen.

Diese Kern-Funktionalitäten brechen Sie nun in etwa 4 AP je herunter. Versuchen Sie jetzt bereits, auch die Sitzung vom 16.5 und 23.5 zu planen (im Wissen, dass Sie kleine Anpassungen an Ihrer Planung vornehmen können).

- [x] Daten anpassen so dass sie der ML Modell verwenden kann.
- [x] RandomForest Modell importieren und trainieren
- [x] ML Modell testen und verbessern

Heute habe ich den ML Modell für mein Projekt erstellt und trainiert. Dafür musste ich als Erstes die Daten anpassen und entscheiden, welche relevant und welche irrelevant sind. Danach konnte ich ein RF Modell implementieren mit 100 Bäumen. Der Test lief sehr gut mit einer Genauigkeit von 99%, was darauf hinweist, dass die Anzahl Bäume gut gewählt sind.
Dazu habe ich noch meinen Datensatz geändert, da sie nicht so geignet war für mein Projekt.

## 16.5

- [x] Daten von MongoDB einlesen in py
- [x] Daten in MongoDB hinzufügen von py lernen
- [x] Über Konsole alle nötigen Daten abfragen
- [x] Alle Daten speichern und dem ML Model geben für eine vorhersage


## 23.5

- [x] Programm soll nachfragen ob der User zufriden ist mit der Vorhersage
- [x] Fals user unzufrieden wird er nach dem Vahrzeug gefragt, den er sich vorgestellt hat
- [x] die daten mit dem Fahrzeug und Modell werden nun zum DatenSatz hinzugefügt
- [x] Das Modell speicher und laden, damit man nicht immer trainieren muss.

Heute habe ich mein ML Modell weiter entwickelt und es kann nun von den Usern neues lernen. Ich habe das gemacht, indem mein Programm den User fragt, ob er zufrieden ist mit der Empfehlung. Falls der User unzufrieden ist, kann er das Fahrzeug, welches er sich vorgestellt hatte eingeben und das speicher sich dann die KI und benutzt es das nächste Mal. Ausserdem wird jetzt das trainierte Modell gespeichert und wieder geladen, wenn nötig, wo durch die Effizienz des Projektes gesteigert wird. Nach hinzufügen von Daten wird das Model erneut trainiert und gespeichert.


## 6.6

Ihr Projekt sollte nun alle Funktionalität haben, dass man es benutzen kann. Allerdings gibt es sicher noch Teile, welche "schöner" werden können: Layout, Code, Architektur... beschreiben Sie kurz den Stand Ihres Projekts, und leiten Sie daraus 6 solche "kosmetischen" AP für den 6.6 und den 13.6 ab.

- [x] Code verschönern und überarbeiten, so dass es für 3. Personen verständlich ist
- [x] HTML erstellen und mein Py mit HTML verbinden
- [x] Mit HTML Fragen und Antwortmöglichkeiten erstellen

Heute habe ich ein Frontend für mein AutoEpmpfehlerAi erstellt. Ich habe als Erstes nach Lösungen recherchiert, wie ich mein Python mit HTML und CSS verbinden kann und bin auf Flask gestossen. Mithilfe von Flask habe ich dann ein sehr einfaches Frontend erstellt, wo es einfacher für den User macht eine Vorhersage zu erhalten.

## 13.6

- [x] Antworte an Py weiter geben so dass sie verarbeitet werden können.
- [x] CSS für den Projekt erstellen

Heute habe ich den Design meines Projektes verbessert, indem ich eine CSS Datei hinzugefügt habe und alles designt habe. (50-100 Wörter)

## 20.6

Was fehlt Ihrem fertigen Projekt noch, um es auszuliefern? Reicht die Zeit für ein *nice-to-have feature*?

- [ ] Neues Fahrzeug der DB hinzufügen debuggen
- [x] Design verbessern mit CSS
- [x] Neue Version ohne DB connection, um Projekt auf bewerbungswebseite hochzuladen
- [x] Projekt zu meiner Webseite hinzufügen

Heute habe ich den grössten Teil meiner Zeit ins debuggen investiert jedoch ohne erfolg. Danach habe ich herausgefunden das isch ein Flask WebApp nicht auf github hosten kann und habe nach alternativen gesucht. Schliesslich bin ich auf Render gestossen, wo ich meine Web-App gratis gehosted habe. Zum Schluss habe ich diesen Projekt noch auf meiner Githubwebseite verlinkt.

Bereiten Sie in den verbleibenden 2 AP Ihre Präsentation vor

- [ ] Materialien der Präsentation vorbereiten
- [ ] Präsentation üben

✍️ Heute habe ich... (50-100 Wörter)

☝️  Vergessen Sie nicht, die Unterlagen für Ihre Präsentation auf github hochzuladen.

## 27.6
