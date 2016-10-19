.. slideconf::
   :autoslides: False


..   :slide_classes: appear


.. only:: latex

  .. raw:: latex

     %%\renewcommand{\headrulewidth}{0pt}
     \fancyhead[L]{}
     \fancyhead[R]{
             \vspace{-1cm}
             \includegraphics[width=1.0cm]{dssyslogo.pdf}
         }

     \pagestyle{fancy}
     \fancyfoot[CEO]{\sffamily \tiny \vspace{0.28cm} ©2016 Dipl.-Inform. Karsten Schulz, Datenschutz.systems}



=============================
Datenschutz und Programmierer
=============================


.. slide:: Datenschutz und Programmierer
   :level: 1

   .. figure:: /_static/editor_faded.png
      :class: fill

   Warum bei der Softwareentwicklung Datenschutz relevant wird.

.. slide:: Antworten auf folgende Fragen
    :level: 2

    * Was geht mich als Coder die EU-DSGVO an?
    * Wieso muss ich an mehr als an Security Standards denken?
    * Um welche Teile meiner Arbeit geht es?
    * Best Practices
    * Quellen

Professionelle Programmierer, deren Produkte auch personenbezogene Daten verarbeiten, sollten sich im eigenen Interesse ab sofort mit dem Thema Datenschutz beschäftigen und damit sicherstellen, dass ihre Software auch in Zukunft noch benutzt werden darf. Am 25. Mai 2016 ist die EU-Datenschutz Grundverordnung (EU-DSGVO) in Kraft getreten, deren Vorschriften bei der Verarbeitung von personenbezogene Daten demnächst eingehalten werden müssen.

Personenbezogene Daten sind beispielsweise Benutzernamen und -anschriften. Aber auch Login-Daten, E-Mail Adressen, Session-Cookies und sämtliche anderen Informationen, die eine natürliche Person identifizierbar machen. Nahezu jede Software verarbeitet in irgendeiner Form personenbezogene Daten.

Das neue, europaweit geltende Gesetz enthält konkrete Vorgaben, die Einfluss auf die Gestaltung von Software haben. Der Betreiber der Software, also der Käufer oder Auftraggeber, ist verantwortlich dafür, dass die Software die Vorgaben EU-DSGVO einhält. Bei Verstoss droht Bußgeld.

Für den professionellen Programmierer gibt es unter diesen Umständen nur eine logische Schlussfolgerung. Und die lautet: „Möchte ich künftig meine Software in der EU an den Mann bringen, muss sie EU-DSGVO-konform sein, sonst kauft sie keiner mehr.“ Schließlich möchte kein Kunde ein Bußgeld riskieren, nur weil der Programmierer die gesetzlichen Vorgaben nicht umgesetzt hat.

Der Vortrag beleuchtet die EU-DSGVO aus dem Blickwinkel der Software-Entwickler und -Architekten. Neben einem fundierten Überblick, worum es überhaupt geht, werden auch konkrete Tipps und Tricks aus dem Umfeld der Python Programmierung gegeben. So wird beispielsweise anhand einer Django-App gezeigt, wie Systeme so zu gestalten sind, dass sie auch unter dem neuen Datenschutz-Recht in der EU im geschäftlichen Umfeld einsetzbar und damit an den Kunden zu bringen sind.



Referent
========

Der Diplom-Informatiker Karsten Schulz ist GDD-zertifizierter
Datenschutzexperte und Betriebswirt. Als bundesweit tätiger
Datenschutzbeauftragter und -berater verfügt er über jahrelange Erfahrung in
der effizienten Umsetzung von Datenschutz im Unternehmen. Darüber hinaus ist er
Lehrbeauftragter der Fachhochschule Dortmund, Fachautor und Gutachter für die
IHK Dortmund.

Für die TÜV NORD Akademie hält er die Seminare „Datenschutz Cloud-Computing“,
„Datenschutz Social Media“ und „Die EU-Datenschutz-Grundverordnung.“

Python hat er vor einigen Jahren kennen und schätzen gelernt. Sowohl die persönlichen
Projekte, wie auch die professionellen werden von ihm hauptsächlich in Python, Bash und
C++ realisiert. In der Web-Entwicklung setzt er meistens Django als Framework ein.

.. image:: _static/referent1.*
    :align: center
    :width: 100%


.. slide:: Karsten Schulz
    :level: 2

    .. rst-class:: referentenlogo

    .. image:: _static/referent1.*
        :align: center
        :width: 100%


Was geht mich als Coder die EU-DSGVO an?
========================================

.. slide:: Was geht mich als Coder die EU-DSGVO an?
    :level: 2

    * Die EU-DSGVO (EU-Datenschutz-Grundverordnung) gilt für alle, die in der EU Produkte oder Dienstleistungen anbieten, z. B.:

      * Diensteanbieter (SaaS)
      * Cloud-Anbieter (IaaS, PaaS)
      * alle Unternehmen mit Niederlassungen in der EU uvm.

    * Nutzer eurer Software müssen die EU-DSGVO ebenfalls einhalten

    .. attention:: Verstöße gegen die EU-DSGVO können dem Nutzer eurer Software bis zu 20.000.000,- EUR Bußgeld kosten!



Der spätere Nutzer eurer Software muss künftig erweiterte Vorgaben zur Einhaltung des Datenschutzes berücksichtigen. Einige dieser Vorgaben kann er nur einhalten, wenn der Softwareentwickler die notwendigen Informationen, Strukturen und Dokumentation liefert.

Der Nutzer eurer Software ist vor dem Gesetz der sogenannte „Verantwortliche Verarbeiter“, kurz: „Verantwortlicher“. Das bedeutet für ihn, dass er für die korrekte Verarbeitung personenbezogener Daten gerade stehen muss. Wenn er gegen Datenschutz-Bestimmungen verstößt, kann er ab dem 25. Mai 2018\ [#anwendung_geudsgvo]_ mit Bußgeldern belegt werden. Das sind:

* 2% des letztjährigen globalen Umsatzes oder 10.000.000,- EUR - oder -
* 4% des letztjährigen globalen Umsatzes oder 20.000.000,- EUR

je nachdem, was höher ist.

Es ist klar, dass der Verantwortliche sehr genau darauf achten wird, dass die Verarbeitung personenbezogener Daten korrekt verläuft. Wie kann er das sicherstellen? Er muss seine gesetzlichen Pflichten einhalten.

.. [#anwendung_geudsgvo] Die EU-DSGVO trat am 25. Mai 2016 in Kraft. Es gibt eine Übergangszeit bis zum 25. Mai 2018. Ab diesem Datum müssen die Vorschriften angewendet werden.


Gesetzliche Pflichten des Verantwortlichen
-------------------------------------------

Nachfolgend ein Auszug der gesetzlichen Pflichten des für die Verarbeitung Verantwortlichen. Dies ist keine vollständige Darstellung sondern nur die Pflichten, auf deren Erfüllung  wir als Softwareentwickler Einfluss haben.

In der Tabelle werden die Pflichten mit den Fundstellen in der EU-Datenschutz-Grundverordnung aufgelistet. Dabei bedeutet die Abkürzung „Art.“ Artikel (so etwas wie ein Paragraf im deutschen Recht) und die Abkürzung „EG“ Erwägungsgrund, ein kurzer Text des europäischen Gesetzgebers, der die Intention einer Regelung beschreibt.

Die vollständige EU-DSGVO findet Ihr hier:

http://eur-lex.europa.eu/legal-content/DE/TXT/?uri=uriserv%3AOJ.L_.2016.119.01.0001.01.DEU&toc=OJ:L:2016:119:TOC


.. csv-table:: Gesetzliche Pflichten des Verantwortlichen
   :header: "","Pflicht","Begründung"
   :widths: 10,45,45

    "☐","Verwalten von Einwilligungen","EGs: 32, 38, 42, 43, 171;  Art.: 4 Nr. 11, 7, 8, 9, 22 Abs. 2c"
    "☐","Verwalten von Widerrufen","EG 65; Art.: 7 Abs. 3, 17 "
    "☐","Kategorien personenbezogener Daten dokumentieren","EGs: 51 - 54; Art.: 9, 14, 15, 30 Abs. 1c, 30 Abs. 5, 33 Abs. 3a, 35 Abs. 3b, 83 Abs. 2g"
    "☐","Übermittlungen dokumentieren","EGs: 48, 101, 102, 110 - 115; Art.: 13 Abs. 1f, 14 Abs. 1f, 15 Abs. 2, 30 Abs. 1e, 30 Abs. 2c, 44 - 50"
    "☐","Auskunftsprozess an betroffene Personen gestalten","EGs: 39, 63, 64; Art.: 13 Abs. 2b, 14 Abs. 2c, 15"

Einwilligungen
    Einwilligungen müssen nachweisbar sein. Falls unsere Software Einwilligungen verarbeitet (z. B. Opt-Ins zu Newslettern oder anderen Verarbeitungen), muss unser Datenmodell diese Einwilligung protokollieren.
Widerrufe
    Jede Einwilligung kann von der betreffenden Person auch widerrufen werden. Ein solcher Widerruf muss in unseren Strukturen und Abläufen darstellbar sein. Sowohl die Protokollierung, wann der Widerruf auf welche Art stattfand könnte relevant sein, als auch die Sicherstellung, dass der Widerruf wirksam ist.
Kategorien personenbezogener Daten
    Der Verantwortliche muss dokumentieren, welche personenbezogenen Daten verarbeitet werden. Entwickler können den Anwender der Software dadurch unterstützen, dass sie das Datenmodell im Handbuch dokumentieren.
Übermittlungen
    Verantwortliche müssen den betroffenen Personen gegebenenfalls mitteilen, an wen sie die personenbezogenen Daten übermittelt haben. Sollte in der Software eine Übermittlung stattfinden, muss das dokumentiert werden. Beispiele für solche Übermittlungen können sein:

    * Speicherplatz in der Cloud
    * Nutzung von Single Sign On Systemen (z. B. OpenID, Facebook-API etc)
    * User Tracking durch einen dritten Dienstleister (z. B. Google, Adobe, Facebook etc)

Auskunftsprozess
    Eine betroffene Person kann beim Verantwortlichen Auskunft verlangen. Diese Auskunft muss vollständig und korrekt sein. Softwareentwickler sollten Funtkionen vorsehen, die eine solche Beauskunftung erleichtern.



Die wichtigsten Betroffenenrechte nach EU-DSGVO
-----------------------------------------------

Einige Rechte der betroffenen Person (das ist immer der Besitzer der personenbezogenen Daten) erfordern ebenfalls bestimmte Funktionen in der Software.


Recht auf Berichtigung (Art. 16)
    Alle gespeicherten Daten der betroffenen Person müssen editierbar sein.
Recht auf Löschung („Recht auf Vergessenwerden“) (Art. 17)
    Alle gespeicherten Daten der betroffenen Person müssen löschbar sein.
Löschung öffentlicher Daten („Vergessen“) (Art. 17 Abs. 2)
    Bei einem Löschbegehren hat der Verantwortliche die Pflicht, andere Empfänger dieser Daten darüber zu informieren, dass ein solches Löschen vom Betroffenen verlangt wird. Die Software muss also nachhalten können, an welche Empfänger Daten in der Vergangenheit übermittelt wurden.
Recht auf Einschränkung der Verarbeitung (Art. 18)
    Eine betroffene person kann verlangen, dass ihre Daten nicht gelöscht, sondern für die weitere Verarbeitung gesperrt werden. Wird die Verarbeitung auf diese Art eingeschränkt, dürfen die Daten nur noch gespeichert werden, nicht mehr anderweitig genutzt, übermittelt, geändert oder gelöscht werden.
    Die Software muss ein entsprechendes „Einschränkungs-Kennzeichen“ im Datenmodell berücksichtigen.
Recht auf Datenübertragbarkeit „Datenportabilität“ (Art. 20)
    Künftig haben betroffene Personen das Recht darauf, ihre eigenen Daten in einem nutzbaren Format zu erhalten. Die Software sollte eine entsprechende Export-Funktion enthalten. Nutzbare Formate könnten zum Beipiel JSON, XML oder ein CSV-Dump sein.

Wieso muss ich an mehr als an Security Standards denken?
========================================================

.. figure:: _static/ds_vs_is.png
   :alt: Datenschutz versus Informationssicherheit
   :align: center
   :width: 100%

   Überschneidungen der Maßnahmen bei Datenschutz und Informationssicherheit

Datenschutz ist nicht gleich Datensicherheit. Datenschutz ist auch nicht nur der Schutz von Daten!
Datensicherheit ist eine Teilmenge des Datenschutzes und manche Maßnahmen, die die Datensicherheit erhöhen, senken den Datenschutz.

Die 7 Schutzziele des Datenschutzes
-----------------------------------

Datensparsamkeit
    Es werden nur die personenbezogenen Daten verarbeitet, die für den jeweiligen Verarbeitungsschritt erforderlich sind.
Integrität
    Die Verarbeitung findet innerhalb der Spezifikation in der Art statt, dass die Daten unversehrt und vollständig bleiben.
Intervenierbarkeit
    Mit Intervenierbarkeit ist gemeint, dass die datenverarbeitenden Verfahren so gestaltet sind, dass die Rechte der Betroffenen jederzeit und vollständig ausgeübt werden können.
Nichtverkettbarkeit
    Das Zusammenführen von Daten, die zu unterschiedlichen Zwecken verarbeitet werden, ist ohne Einwilligung des Betroffenen zu verhindern.
Transparenz
    Interessierte Parteien (Verantwortlicher, betroffene Person, Aufsicht) können Einsicht nehmen und nachvollziehen, welche Daten zu welchem Zweck mit welchen Mitteln verarbeitet werden.
Verfügbarkeit
    Die personenbezogenen Daten stehen zeitgerecht zur Verfügung, sind auffindbar und werden in den zugeordneten Prozessen sachgerecht verarbeitet.
Vertraulichkeit
    Nur befugte Personen können auf die Daten zugreifen. Befugt sind nur die Personen, deren zweckgebundene Aufgabenerfüllung den Zugriff auf die Daten erforderlich macht.

Mögliche Konflikte von Schutzmaßnahmen
----------------------------------------

.. csv-table:: Auswirkungen der Maßnahmen für ...
    :header: "","Informationssicherheit","Datenschutz"

    "Webproxy","gut","schlecht"
    "Serverprotokolle","gut","schlecht"
    "Eingabekontrolle","gut","gut"
    "Intervenierbarkeit","schlecht","gut"
    "Transparenz","schlecht","gut"
    "Integrität","gut","gut"
    "Richtlinien für Mitarbeiter","gut","gut"


Worum geht es beim Datenschutz jetzt wirklich?
----------------------------------------------

Datenschutz soll folgende Aspekte der Datenverarbeitung sicherstellen. 

Die betroffene Person weiß immer welche ihrer Daten von wem zu welchen Zwecken warum wie verarbeitet werden. Und sie kann intervenieren:

  * sie erhält Auskunft,
  * kann berichtigen lassen,
  * kann löschen lassen,
  * kann die Verarbeitung einschränken lassen,
  * kann die Einwilligung zur Verarbeitung widerufen.
  
Sichere Software stellt nicht zwangsläufig die genannten Punkte sicher.
   


Um welche Teile meiner Arbeit geht es?
======================================

.. figure:: _static/apple_uuids.png
   :alt: personenbezogene Daten im Apple iPhone
   :align: center
   :width: 40%

   Personenbezogene Daten in Apples iPhone unter iOS 10



Best Practices
==============

.. figure:: _static/bahn_app.png
   :alt: Widerspruchsmöglichkeit gegen Tracking in der Bahn App
   :align: center
   :width: 40%

   Widerspruchsmöglichkeit gegen Tracking in der Bahn App


Quellen
=======



Grundsätze des Datenschutzes
============================

Sowohl heute im BDSG als auch ab dem 25. Mai 2018 in der kommenden EU-Datenschutz-Grundverordnung gilt das Verbot der Verarbeitung personenbezogener Daten mit Erlaubnisvorbehalt.

Deadline 25. Mai 2018
---------------------

Der Termin steht fest. Software, die heute geschrieben wird, sollte die Grundverordnung berücksichtigen.

Die EU-Datenschutzgrundverordnung
---------------------------------

*Verordnung des Europäischen Parlaments und des Rates zum Schutz natürlicher Personen bei der Verarbeitung personenbezogener Daten, zum freien Datenverkehr und zur Aufhebung der Richtlinie 95/46/EG (Datenschutz-Grundverordnung)*

Ab dem 25. Mai 2018 wird die EU-Datenschutz-Grundverordnung (EU-DSGVO) für alle Verarbeiter personenbezogener Daten angewendet, die in der EU ihre Produkte oder Dienstleistungen anbieten.

http://eur-lex.europa.eu/legal-content/DE/TXT/?uri=uriserv%3AOJ.L_.2016.119.01.0001.01.DEU&toc=OJ:L:2016:119:TOC


Was sind personenbezogene Daten?
--------------------------------


* *Personenbezogene Daten* sind Einzelangaben über persönliche oder sachliche Verhältnisse einer bestimmten oder bestimmbaren natürlichen Person.
* *Besondere Arten personenbezogener Daten* sind Angaben über rassische und ethnische Herkunft, politische Meinungen, religiöse oder philosophische / weltanschauliche Überzeugungen, Gewerkschaftszugehörigkeit, Gesundheit, Sexualleben, biometrische Daten


Mit *Daten* ist in diesem Zusammenhang die formalisierte Darstellung von
Informationen gemeint, die für die Verarbeitung durch Menschen oder
automatisierte Abläufe geeignet sind.

*Personenbezogene Daten* sind Einzelangaben über persönliche oder sachliche
Verhältnisse einer bestimmten oder bestimmbaren natürlichen Person.

Die EU-DSGVO definiert in Art. 4 Nr. 1 personenbezogene Daten als: „*alle Informationen, die sich auf eine identifizierte oder identifizierbare natürliche Person (im Folgenden „betroffene Person“) beziehen; als identifizierbar wird eine natürliche Person angesehen, die direkt oder indirekt, insbesondere mittels Zuordnung zu einer Kennung wie einem Namen, zu einer Kennnummer, zu Standortdaten, zu einer Online-Kennung oder zu einem oder mehreren besonderen Merkmalen, die Ausdruck der physischen, physiologischen, genetischen, psychischen, wirtschaftlichen, kulturellen oder sozialen Identität dieser natürlichen Person sind, identifiziert werden kann*“

*Besondere Arten personenbezogener Daten* sind nach § 3 Abs. 9 BDSG und Art. 9 EU-DSGVO Daten, die Angaben machen über:

* rassische und ethnische Herkunft
* politische Meinungen
* religiöse oder philosophische / weltanschauliche Überzeugungen
* Gewerkschaftszugehörigkeit
* Gesundheit
* Sexualleben
* biometrische Daten

Für die Verarbeitung dieser Art Daten werden hohe Ansprüche an die Schutzmaßnahmen gestellt, die die verantwortliche Stelle ergreifen muss.

Die Verarbeitung der besonderen Kategorien personenbezogener Daten ist untersagt, es sei den, die betroffene Person hat **ausdrücklich** eingewilligt oder eine rechtliche Norm legitimiert die Verarbeitung.

Eine Unterscheidung der personenbezogenen Daten hinsichtlich ihrer privater oder geschäftlicher Natur findet nicht statt. Weder das BDSG noch die EU-DSGVO unterscheiden zwischen einer B2C- und B2B-Verarbeitung.


Beispiele für personenbezogene Daten
------------------------------------

* Namen
* E-Mail Adressen
* persönliche Durchwahl
* Anschrift mit Personenbezug, z. B. Personengesellschaft
* Tracking ID im Web oder Apps
* AD-ID (Advertising ID)
* Pseudonym im Web-Forum
* IP-Adresse
* IMEI (International Mobile Station Equipment Identity)
* MEID (Mobile Equipment Identifier)
* SEID (Secure Element ID Number)
* und andere UUIDs (Universally Unique Identifier

.. figure:: _static/apple_uuids.png
   :alt: personenbezogene Daten im Apple iPhone
   :align: center
   :width: 40%

   Personenbezogene Daten in Apples iPhone unter iOS 10

Was ist Verarbeiten?
--------------------

*Verarbeiten* ist das Erheben, das Erfassen, die Organisation, das Ordnen, die Speicherung, die Anpassung oder Veränderung, das Auslesen, das Abfragen, die Verwendung, die Offenlegung durch Übermittlung, Verbreitung oder eine andere Form der Bereitstellung, den Abgleich oder die Verknüpfung, die Einschränkung, das Löschen oder die Vernichtung.

Python Code: Beispiele
======================

Sockets
-------

.. code-block:: python
    :emphasize-lines: 1,2,3

    import socket
    sock = socket.socket()
    sock.connect((address, port))

Beim Öffnen eines Sockets wird die IP-Adresse des Client-PCs an den Server übertragen. Die IP-Adresse ist ein personenbezogenes Datum und wird an jemand anderen übermittelt. Es ist ein datenschutzrelevanter Vorgang.


Requests
--------

.. code-block:: python

    import requests
    requests.get('https://api.someserver.anywhere')

Natürlich werden nicht nur bei low-level Sockets, sondern bei jeder Netzwerkkommunikation personenbezogene Daten ausgetauscht.


Django
--------
.. code-block:: python

    from django.contrib.auth.models import User
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

Offensichtlich ist das Anlegen und Verwalten eines Benutzerkontos die Verarbeitung personenbezogener Daten.

.. code-block:: python

    from django.contrib.auth.models import User
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

Offensichtlich ist das Anlegen und Verwalten eines Benutzerkontos die Verarbeitung personenbezogener Daten.



Privacy by Design / Privacy by Default
======================================

Artikel 25 der EU DSGVO

.. code-block:: python

    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
    # default: False

Whether to expire the session when the user closes their browser. See Browser-length sessions vs. persistent sessions.




Datenschutz versus Informationssicherheit
-----------------------------------------

.. figure:: _static/ds_vs_is.png
   :alt: Datenschutz versus Informationssicherheit
   :align: center
   :width: 100%

   Überschneidungen der Maßnahmen bei Datenschutz und Informationssicherheit


Legitimation der Verarbeitung
=============================


Um zu beurteilen, ob personenbezogene Daten verarbeitet werden dürfen, helfen folgende Checklisten, die Rechtsgrundlage für die Verarbeitung zu ermitteln.

Prüfen der Legitimation der Verarbeitung nach EU-DSGVO
------------------------------------------------------

Falls keiner der Punkte zutreffen sollte, ist eine Verarbeitung der Daten
nicht möglich.


.. csv-table:: Checkliste Rechtmäßigkeit der pbDV nach EU-DSGVO
    :header: "","**Checkliste Rechtmäßigkeit der pbDV nach EU-DSGVO**",""
    :widths: 10,70,20

    "","*Eine der folgenden Voraussetzungen trifft zu*","*Gründe*"

    "☐","Die Verarbeitung ist erforderlich zur Erfüllung eines Vertrags mit der betroffenen Person","Art. 6 Abs. 1b, EG 44"
    "☐","Die Verarbeitung ist erforderlich für vorvertragliche Maßnahmen auf Anfrage der betroffenen Person","Art. 6 Abs. 1b, EG 44"
    "☐","Die Verarbeitung ist erforderlich zur Erfüllung einer rechtlichen Pflicht des für die Verarbeitung Verantwortlichen","Art. 6 Abs. 1c, EG 45"
    "☐","Die Verarbeitung ist erforderlich, weil lebenswichtige Interessen der betroffenen Person oder einer anderen natürlichen Person geschützt werden","Art. 6 Abs. 1d, EG 46"
    "☐","Die Verarbeitung ist erforderlich im öffentlichen Interesse oder in Ausübung öffentlicher Gewalt","Art. 6 Abs. 1e, EG 45"
    "☐","Berechtigtes Interesse, wenn schutzwürdige Interessen dem nicht entgegen stehen (insbesondere bei Kindern)","Art. 6 Abs. 1f, EG 47"
    "☐","Einwilligung der Person für einen oder mehrere Zwecke ist nachweisbar","Art. 7 Abs. 1, EG 42"

Falls eine Verarbeitung möglich ist, müssen folgende Grundsätze der Verarbeitung nachweisbar eingehalten werden:

.. csv-table:: Checkliste Grundsätze der pbDV
    :header: "","**Checkliste Grundsätze der pbDV**",""
    :widths: 10,70,20

    "","*Alle der folgenden Voraussetzungen treffen zu*","*Gründe*"

    "☐","Die Verarbeitung ist rechtmäßig","Art. 5 Abs. 1a"
    "☐","Die Verarbeitung erfolgt nach Treu und Glauben","Art. 5 Abs. 1a"
    "☐","Die Transparenzpflichten sind eingehalten","Art. 5 Abs. 1a, EG 58"
    "☐","Alle Informationen und Mitteilungen zur Verarbeitung sind leicht erreichbar","EG 39"
    "☐","Alle Informationen und Mitteilungen zur Verarbeitung sind verständlich und in klarer, einfacher Sprache verfasst","EG 39"
    "☐","Der Umfang der Verarbeitung ist dokumentiert","EG 39"
    "☐","Die Zwecke der Verarbeitung sind dokumentiert","EG 39"
    "☐","Es werden nur die für die Verarbeitung erforderlichen Daten verarbeitet","Art. 5 Abs. 1c"
    "☐","Die verarbeiteten Daten sind aktuell und sachlich richtig","Art. 5 Abs. 1d"
    "☐","Unrichtige Daten können unverzüglich gelöscht oder berichtigt werden","Art. 5 Abs. 1d"
    "☐","Es werden kürzestmögliche Löschfristen eingehalten","Art. 5 Abs. 1e"
    "☐","Die Daten werden vor unbefugter und unrechtmäßiger Verarbeitung geschützt","Art. 5 Abs. 1f"
    "☐","Die Daten werden vor unbeabsichtigter Zerstörung und Schädigung geschützt","Art. 5 Abs. 1f"
    "☐","Die vorgenannte Maßnahmen können nachgewiesen werden","Art. 5 Abs. 2"


Tracking von Personen
---------------------



Das Erstellen von pseudonymen Nutzungsprofilen ist in Grenzen erlaubt. § 15 TMG Abs. 3:

„*(3) Der Diensteanbieter darf für Zwecke der Werbung, der Marktforschung oder zur bedarfsgerechten Gestaltung der Telemedien Nutzungsprofile bei Verwendung von Pseudonymen erstellen, sofern der Nutzer dem nicht widerspricht. Der Diensteanbieter hat den Nutzer auf sein Widerspruchsrecht im Rahmen der Unterrichtung nach § 13 Abs. 1 hinzuweisen.*“

Tracking muss in der Datenschutzerklärung deklariert werden. In der Datenschutzerklärung muss ausserdem dargestellt werden, dass der Nutzer widersprechen und wie sich der Nutzer vom Tracking abmelden kann („Opt-Out“ laut § 13 TMG ). Auf diese Möglichkeit ist vor Beginn des Trackings hinzuweisen. Alternativ kann er beim ersten Besuch aufgefordert werden, in das Tracking einzuwilligen („Opt-In“ laut E-Privacy-Richtlinie Nr. 2009/136/EG, auch „Cookie-Richtlinie)

Für Apps gelten die gleichen Vorgaben wie für Webseiten.

.. figure:: _static/bahn_app.png
   :alt: Widerspruchsmöglichkeit gegen Tracking in der Bahn App
   :align: center
   :width: 40%

   Widerspruchsmöglichkeit gegen Tracking in der Bahn App



Pflichten des Verantwortlichen nach EU-DSGVO
============================================

* Informationspflicht bei

    * Erhebung bei betroffener Person (Art. 13)
    * Erhebung nicht bei der betroffenen Person (Art. 14)
    * Zweckänderung (Art. 13 Abs. 3 und Art 14 Abs. 4)

* Datenschutz by design / by default  (Art. 25)
* Durchführung von Datenschutz-Folgenabschätzung (Art. 35)

