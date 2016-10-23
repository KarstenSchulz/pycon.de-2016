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
     \fancyfoot[CEO]{\sffamily \tiny \vspace{0.28cm} ©2016 CC BY-SA 4.0 - Karsten Schulz, Datenschutz.systems, Dortmund }



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
    * Wieso reicht es nicht, dass mein Code sicher ist?
    * Beispiele?
    * Quellen zum Nachlesen?

Professionelle Programmierer, deren Produkte auch personenbezogene Daten verarbeiten, sollten sich im eigenen Interesse ab sofort mit dem Thema Datenschutz beschäftigen und damit sicherstellen, dass ihre Software auch in Zukunft noch benutzt werden darf. Am 25. Mai 2016 ist die EU-Datenschutz Grundverordnung (EU-DSGVO) in Kraft getreten. Diese Vorschrift muss bei der Verarbeitung von personenbezogene Daten ab dem 25. Mai 2018 obligatorisch eingehalten werden.

Personenbezogene Daten sind beispielsweise Benutzernamen und -anschriften. Aber auch Login-Daten, E-Mail Adressen, Session-Cookies und sämtliche anderen Informationen, die eine natürliche Person identifizierbar machen. Nahezu jede Software verarbeitet in irgendeiner Form personenbezogene Daten.

Das neue, europaweit geltende Gesetz enthält konkrete Vorgaben, die Einfluss auf die Gestaltung von Software haben. Der Betreiber der Software, also der Käufer oder Auftraggeber, ist verantwortlich dafür, dass die Software beim Betrieb die Vorgaben EU-DSGVO einhält. Bei Verstoss droht Bußgeld.

Für den professionellen Programmierer gibt es unter diesen Umständen nur eine logische Schlussfolgerung. Und die lautet: „*Möchte ich künftig meine Software in der EU an den Mann bringen, muss sie EU-DSGVO-konform sein, sonst kauft sie keiner mehr.*“ Schließlich möchte kein Kunde ein Bußgeld riskieren, nur weil der Programmierer die gesetzlichen Vorgaben nicht umgesetzt hat.

Dieser Vortrag beleuchtet die EU-DSGVO aus dem Blickwinkel der Software-Entwickler und -Architekten. Neben einem fundierten Überblick, worum es überhaupt geht, werden auch konkrete Tipps und Tricks aus dem Umfeld der Python Programmierung gegeben. So wird beispielsweise anhand einer Django-App gezeigt, wie Systeme so zu gestalten sind, dass sie auch unter dem neuen Datenschutz-Recht in der EU im geschäftlichen Umfeld einsetzbar und damit an den Kunden zu bringen sind.



Wer erzählt hier?
==================

Der Diplom-Informatiker Karsten Schulz ist GDD-zertifizierter Datenschutzexperte und Betriebswirt. Als bundesweit tätiger Datenschutzbeauftragter und -berater verfügt er über jahrelange Erfahrung in der effizienten Umsetzung von Datenschutz im Unternehmen. Darüber hinaus ist er Lehrbeauftragter der Fachhochschule Dortmund, Fachautor und Gutachter für die IHK Dortmund.

Er berät als externer Berater Kunden wie die Deutsche Fußball Liga, Caterpillar oder den Deutschen Mieterbund. 

Für die TÜV NORD Akademie hält er Seminare wie „Datenschutz Cloud-Computing“, „Datenschutz Social Media“ und „Die EU-Datenschutz-Grundverordnung.“

Die Programmiersprache Python hat er vor vielen Jahren kennen und schätzen gelernt. Sowohl seine persönlichen Projekte wie auch die professionellen werden von ihm hauptsächlich in Python realisiert. Bei der Web-Entwicklung setzt er meistens Django als Framework ein.

.. image:: _static/referent1.*
    :align: center
    :width: 100%


.. slide::
    :level: 2

    |

    .. rst-class:: referentenlogo

    .. image:: _static/referent1.*
        :align: center
        :width: 100%


Was geht mich als Coder die EU-DSGVO an?
========================================

Der spätere Nutzer Eurer Software muss künftig erweiterte Vorgaben zur Einhaltung des Datenschutzes einhalten und nachweisen können. Einige dieser Vorgaben kann er nur einhalten, wenn Ihr als Softwareentwickler die notwendigen Informationen, Strukturen, Funktionen und Dokumentation liefert.

.. slide:: Was geht mich als Coder die EU-DSGVO an?
    :level: 2
    :inline-contents: True
    
    * Die EU-DSGVO (EU-Datenschutz-Grundverordnung) gilt für alle, die in der EU Produkte oder Dienstleistungen anbieten, z. B.:

      * Diensteanbieter (SaaS)
      * Cloud-Anbieter (IaaS, PaaS)
      * alle Unternehmen mit Niederlassungen in der EU uvm.

    .. attention:: 
    
        **Nutzer Eurer Software müssen die EU-DSGVO einhalten**
    
        Verstöße gegen die EU-DSGVO können dem Nutzer eurer Software bis zu 20.000.000,- EUR Bußgeld kosten!

Der Nutzer eurer Software ist vor dem Gesetz der sogenannte „Verantwortliche Verarbeiter“, kurz: „Verantwortlicher“. Das bedeutet für ihn, dass er für die korrekte Verarbeitung personenbezogener Daten gerade stehen muss. Wenn er gegen Datenschutz-Bestimmungen verstößt, kann er ab dem 25. Mai 2018\ [#anwendung_geudsgvo]_ mit Bußgeldern belegt werden. Das sind je nach Verstoß:

* 2% des letztjährigen globalen Umsatzes oder 10.000.000,- EUR - oder -
* 4% des letztjährigen globalen Umsatzes oder 20.000.000,- EUR

je nachdem, was höher ist.

Es ist klar, dass der Verantwortliche sehr genau darauf achten wird, dass die Verarbeitung personenbezogener Daten korrekt verläuft. 

.. [#anwendung_geudsgvo] Die EU-DSGVO trat am 25. Mai 2016 in Kraft. Es gibt eine Übergangszeit bis zum 25. Mai 2018. Ab diesem Datum müssen die Vorschriften angewendet werden.


Gesetzliche Pflichten des Verantwortlichen
-------------------------------------------

Nachfolgend ein Auszug der gesetzlichen Pflichten des Verantwortlichen. Dies ist keine vollständige Darstellung sondern nur die Auflistung der Pflichten, auf deren Erfüllung wir als Softwareentwickler Einfluss haben.

In der Tabelle werden die Pflichten mit den Fundstellen in der EU-Datenschutz-Grundverordnung aufgelistet. Dabei bedeutet die Abkürzung „Art.“ Artikel (so etwas wie ein Paragraf im deutschen Recht) und die Abkürzung „EG“ Erwägungsgrund, ein kurzer Text des europäischen Gesetzgebers, der die Intention einer Regelung beschreibt.

Die vollständige EU-DSGVO findet Ihr hier:

http://eur-lex.europa.eu/legal-content/DE/TXT/HTML/?uri=CELEX:32016R0679&from=DE

.. csv-table:: Gesetzliche Pflichten des Verantwortlichen
   :header: "Pflicht","Begründung"
   :widths: 50,50

    "Verwalten von Einwilligungen (z. B. von Kunden)","EGs: 32, 38, 42, 43, 171;  Art.: 4 Nr. 11, 7, 8, 9, 22 Abs. 2c"
    "Verwalten von Widerrufen","EG 65; Art.: 7 Abs. 3, 17 "
    "Kategorien personenbezogener Daten dokumentieren","EGs: 51 - 54; Art.: 9, 14, 15, 30 Abs. 1c, 30 Abs. 5, 33 Abs. 3a, 35 Abs. 3b, 83 Abs. 2g"
    "Übermittlungen an Andere dokumentieren","EGs: 48, 101, 102, 110 - 115; Art.: 13 Abs. 1f, 14 Abs. 1f, 15 Abs. 2, 30 Abs. 1e, 30 Abs. 2c, 44 - 50"
    "Auskunftsprozess an betroffene Personen gestalten","EGs: 39, 63, 64; Art.: 13 Abs. 2b, 14 Abs. 2c, 15"

.. slide:: Gesetzliche Pflichten des Verantwortlichen
    :level: 2
    :inline-contents: True

    Einwilligungen
        Einwilligungen müssen nachweisbar sein. Falls eine Software Einwilligungen verarbeitet (z. B. Opt-Ins zu Newslettern), muss das Datenmodell diese Einwilligung protokollieren.

        .. admonition:: Tipp!
    
            Einwilligungen protokollieren.

.. slide:: Gesetzliche Pflichten des Verantwortlichen
    :level: 2
    :inline-contents: True

    Widerrufe
        Jede Einwilligung kann von der betreffenden Person auch widerrufen werden. Ein solcher Widerruf muss in den Strukturen und Abläufen der Software darstellbar sein. Sowohl die Protokollierung wann der Widerruf auf welche Art stattfand ist relevant, als auch die Sicherstellung, dass der Widerruf wirksam ist.

        .. admonition:: Tipp!
    
            Widerrufe protokollieren.

.. slide:: Gesetzliche Pflichten des Verantwortlichen
    :level: 2
    :inline-contents: True

    Kategorien personenbezogener Daten
        Der Verantwortliche muss dokumentieren, welche personenbezogenen Daten verarbeitet werden. Entwickler können den Anwender der Software dadurch unterstützen, dass sie das Datenmodell im Handbuch vollständig dokumentieren.

        .. admonition:: Tipp!
    
            Datenstrukturen / -modelle in die Dokumentation!

.. slide:: Gesetzliche Pflichten des Verantwortlichen
    :level: 2
    :inline-contents: True

    Auskunftsprozess
        Eine betroffene Person kann beim Verantwortlichen Auskunft über die von ihr gespeicherten Daten verlangen. Diese Auskunft muss vollständig und korrekt sein. Softwareentwickler sollten Möglichkeiten vorsehen, die eine solche Beauskunftung erleichtern. Die Auskunft muss alle Daten zu einer Person umfassen, aus allen Datenbanken und aus allen Tabellen.

        .. admonition:: Tipp!
    
            Vollständige und korrekte Beauskunftung durch Funktionen oder Dokumentation gewährleisten.

.. slide:: Gesetzliche Pflichten des Verantwortlichen
    :level: 2
    :inline-contents: True

    Übermittlungen
        Künftig muss der Verantwortliche angeben können, an welche Empfänger oder Empfängerkategorien Daten übermittelt wurden, zum Beispiel bei:

        * Speicherplatz in der Cloud
        * Nutzung von Single Sign On Systemen (OpenID etc.)
        * User Tracking durch Dritte (Google & Co.)
        * Übermittlung an andere Empfänger

        .. admonition:: Tipp!
    
            Alle Übermittlungen darstellen und dokumentieren. Ggfs. Übermittlungen optional machen.


Die wichtigsten Betroffenenrechte nach EU-DSGVO
-----------------------------------------------

Einige Rechte der betroffenen Person (das ist immer der Eigentümer der personenbezogenen Daten) erfordern bestimmte Funktionen in der Software.

.. slide:: Die wichtigsten Betroffenenrechte nach EU-DSGVO
    :level: 2
    :inline-contents: True

    Recht auf Berichtigung (Art. 16)
        Alle gespeicherten Daten der betroffenen Person müssen jederzeit editierbar und damit korrigierbar sein.
    Recht auf Löschung („Recht auf Vergessenwerden“) (Art. 17)
        Alle gespeicherten Daten der betroffenen Person müssen löschbar sein, solange keine gesetzlichen Aufbewahrungsfristen dagegen stehen.
    Löschung öffentlicher Daten („Vergessen“) (Art. 17 Abs. 2)
        Bei einem Löschbegehren hat der Verantwortliche die Pflicht, andere Empfänger dieser Daten darüber zu informieren, dass ein solches Löschen vom Betroffenen verlangt wird. In der Verarbeitung muss man also nachhalten können, an welche Empfänger die Daten in der Vergangenheit übermittelt wurden.

.. slide:: Die wichtigsten Betroffenenrechte nach EU-DSGVO
    :level: 2
    :inline-contents: True

    Recht auf Einschränkung der Verarbeitung (Art. 18)
        Eine betroffene Person kann verlangen, dass ihre Daten nicht gelöscht, sondern für die weitere Verarbeitung gesperrt werden. Wird die Verarbeitung auf diese Art eingeschränkt, dürfen die Daten nur noch gespeichert werden, nicht mehr anderweitig genutzt, übermittelt, geändert oder gelöscht werden.
        Die Software muss ein entsprechendes „Einschränkungs-Kennzeichen“ im Datenmodell berücksichtigen.
    Recht auf Datenübertragbarkeit „Datenportabilität“ (Art. 20)
        Künftig haben betroffene Personen das Recht darauf, ihre eigenen Daten in einem nutzbaren Format zu erhalten. Die Software sollte eine entsprechende Export-Funktion enthalten. Nutzbare Formate könnten zum Beispiel JSON, XML oder ein CSV-Dump sein.
        
        
Datenschutz by Design und by Default (Art. 25)
----------------------------------------------

.. slide:: Datenschutz by Design (Art. 25)
    :level: 2
    :inline-contents: True

    Der Verantwortliche sorgt

    * zum Zeitpunkt der Festlegung der Mittel (Ausschreibung, Anforderung)
    * zum Zeitpunkt der eigentlichen Verarbeitung (Betrieb, Nutzung)

    für geeignete technische und organisatorische Maßnahmen zum Schutz personenbezogener Daten

Artikel 25 der EU-DSGVO „Datenschutz durch Technikgestaltung und durch datenschutzfreundliche Voreinstellungen“ verlangt vom Verarbeiter, dass sowohl bei der Festlegung der Mittel für die Verarbeitung, also auch beim Definieren der Anforderungen der Funktionen und Datenstrukturen der Software, als auch beim Betreiben, also beim Nutzen der Software, Datenschutz eingehalten wird:

    Art. 25 Abs. 1: Unter Berücksichtigung des Stands der Technik, der Implementierungskosten und der Art, des Umfangs, der Umstände und der Zwecke der Verarbeitung sowie der unterschiedlichen Eintrittswahrscheinlichkeit und Schwere der mit der Verarbeitung verbundenen Risiken für die Rechte und Freiheiten natürlicher Personen trifft der Verantwortliche sowohl zum Zeitpunkt der Festlegung der Mittel für die Verarbeitung als auch zum Zeitpunkt der eigentlichen Verarbeitung geeignete technische und organisatorische Maßnahmen — wie z. B. Pseudonymisierung — trifft, die dafür ausgelegt sind, die Datenschutzgrundsätze wie etwa Datenminimierung wirksam umzusetzen und die notwendigen Garantien in die Verarbeitung aufzunehmen, um den Anforderungen dieser Verordnung zu genügen und die Rechte der betroffenen Personen zu schützen.
    
Folgende generische Maßnahmen unterstützen beispielhaft Datenschutz durch Technikgestaltung:

.. slide:: Datenschutz by Design (Art. 25)
    :level: 2
    :inline-contents: True

    * Trennung nach Verarbeitungszweck
    * Anonymisierung (so früh wie möglich)
    * Pseudonymisierung (so früh wie möglich)
    * Verschlüsselte Kommunikation
    

.. slide:: Datenschutz by Default (Art. 25)
    :level: 2
    :inline-contents: True

    Der Verantwortliche trifft geeignete technische und organisatorische Maßnahmen, die sicherstellen, dass

    * Datenminimierung
    * Zweckgebundenheit
    * Vertraulichkeit

    gewährleistet ist.

Bei der Verarbeitung, muss eine Software datenschutzfreundliche Voreinstellungen aufweisen:

    Art. 25 Abs. 2: Der Verantwortliche trifft geeignete technische und organisatorische Maßnahmen, die sicherstellen, dass durch Voreinstellung grundsätzlich nur personenbezogene Daten, deren Verarbeitung für den jeweiligen bestimmten Verarbeitungszweck erforderlich ist, verarbeitet werden. Diese Verpflichtung gilt für die Menge der erhobenen personenbezogenen Daten, den Umfang ihrer Verarbeitung, ihre Speicherfrist und ihre Zugänglichkeit. Solche Maßnahmen müssen insbesondere sicherstellen, dass personenbezogene Daten durch Voreinstellungen nicht ohne Eingreifen der Person einer unbestimmten Zahl von natürlichen Personen zugänglich gemacht werden.

Folgende generische Maßnahmen unterstützen Datenschutz durch datenschutzfreundliche Voreinstellungen :

     
.. slide:: Datenschutz by Default (Art. 25)
    :level: 2
    :inline-contents: True

    * Nur erforderliche Daten verarbeiten
    * Zugriffsschutz per Voreinstellung
    * Transparenz durch Dokumentation
    * Verschlüsselte Kommunikation voreingestellt
     

Wieso reicht es nicht, dass mein Code sicher ist?
=================================================

.. slide:: Wieso reicht es nicht, dass mein Code sicher ist?
    :level: 1

.. slide:: Datenschutz vs. Informationssicherheit
    :level: 2

    .. figure:: _static/ds_vs_is.png
       :alt: Datenschutz versus Informationssicherheit
       :align: center
       :width: 100%

.. figure:: _static/ds_vs_is.png
   :alt: Datenschutz versus Informationssicherheit
   :align: center
   :width: 100%

   Überschneidungen der Maßnahmen bei Datenschutz (DS) und Informationssicherheit (IS)

Datenschutz (DS) ist nicht gleich Informationssicherheit (IS). Datenschutz ist auch nicht nur der Schutz von Daten, sondern auch - aber nicht nur - die Einhaltung aller Betroffenenrechte!

.. attention:: Maßnahmen, die die Informationssicherheit verbessern, können unter Umständen den Datenschutz senken und umgekehrt.

Die 7 Schutzziele des Datenschutzes
-----------------------------------


.. slide:: Die 7 Schutzziele des Datenschutzes
    :level: 2
    :inline-contents: True

    Datensparsamkeit (DS)
        Es werden nur die personenbezogenen Daten verarbeitet, die für den jeweiligen Verarbeitungsschritt erforderlich sind.
        
        .. admonition:: Tipp!
    
            * Die Datenmodelle müssen auf die Erforderlichkeit der Datenfelder überprüft werden
            * Keine Verarbeitung „auf Vorrat“!
            * Temporäre Daten frühest möglich löschen. 
        
.. slide:: Die 7 Schutzziele des Datenschutzes
    :level: 2
    :inline-contents: True

    Integrität (DS & IS)
        Die Verarbeitung findet innerhalb der Spezifikation in der Art statt, dass die Daten unversehrt und vollständig bleiben.
        
        .. admonition:: Tipp!

            * Tests
            * Transaktionen nutzen
            * FS Prüfsummen (z. B. btrfs, zfs, ...)
            * DB Prüfsummen (z. B. PostgreSQL ``initdb ... --data-checksums``\ [#postgresql]_ nutzen.
            
        
.. slide:: Die 7 Schutzziele des Datenschutzes
    :level: 2
    :inline-contents: True

    Intervenierbarkeit (DS)
        Mit Intervenierbarkeit ist gemeint, dass die datenverarbeitenden Verfahren so gestaltet sind, dass die Rechte der Betroffenen jederzeit und vollständig ausgeübt werden können.
        
        .. admonition:: Tipp!

            * Betroffenenrechte sicherstellen
            * Alle Datenstrukturen und -ablagen dokumentieren
            * Ggfs. Auskunfts-Funktion und Export-Funktion implementieren
            * Kennzeichen zur Einschränkung der Verarbeitung vorsehen. 

.. slide:: Die 7 Schutzziele des Datenschutzes
    :level: 2
    :inline-contents: True

    Nichtverkettbarkeit (DS)
        Das Zusammenführen von Daten, die zu unterschiedlichen Zwecken verarbeitet werden, ist ohne Einwilligung des Betroffenen zu verhindern.
        
        .. admonition:: Tipp!
    
            Auf die Trennung der Daten und der Zugriffsberechtigungen nach Verarbeitungszweck achten.   
        
              
.. slide:: Die 7 Schutzziele des Datenschutzes
    :level: 2
    :inline-contents: True
    
    Transparenz (DS)
        Interessierte Parteien (Verantwortlicher, betroffene Person, Datenschutz-Aufsichtsbehörde) können Einsicht nehmen und nachvollziehen, welche Daten zu welchem Zweck mit welchen Mitteln verarbeitet werden.

        .. admonition:: Dokumentieren!

            * Datenmodelle, -strukturen, -formate
            * Abläufe
            * Berechtigungen

.. slide:: Die 7 Schutzziele des Datenschutzes
    :level: 2
    :inline-contents: True

    Verfügbarkeit  (DS & IS)
        Die personenbezogenen Daten stehen zeitgerecht zur Verfügung, sind auffindbar und werden in den zugeordneten Prozessen sachgerecht verarbeitet.
        
        .. admonition:: Tipp!
    
            * Doku
            * Tests
            * Backup
            * Exportfunktion mit „nutzbarem“ Format („Recht auf Datenportabilität“)

.. slide:: Die 7 Schutzziele des Datenschutzes
    :level: 2
    :inline-contents: True

    Vertraulichkeit  (DS & IS)
        Nur befugte Personen können auf die Daten zugreifen. Befugt sind nur die Personen, deren zweckgebundene Aufgabenerfüllung den Zugriff auf die Daten erforderlich macht.

        .. admonition:: Tipp!
    
            * Berechtigungskonzept
            * Zugriffsrechte und -rollen
            * Protokollierung von Zugriffen
            * Ggfs. Vier-Augen-Prinzip.
    

Worum geht es beim Datenschutz jetzt wirklich?
----------------------------------------------

Datenschutz soll folgende Aspekte der Datenverarbeitung sicherstellen.

.. slide:: Worum geht es beim Datenschutz jetzt wirklich?
    :level: 2
    :inline-contents: True

    .. hint:: Die betroffene Person weiß immer welche ihrer Daten von wem zu welchen Zwecken warum wie verarbeitet werden.


    .. hint:: Die Betroffene Person kann Ihre Rechte wahrnehmen:

      * sie erhält Auskunft,
      * kann berichtigen lassen,
      * kann löschen lassen,
      * kann die Verarbeitung einschränken lassen,
      * kann die Einwilligung zur Verarbeitung widerrufen.


.. attention:: Sichere Software und eine sichere Laufzeitumgebungen stellen nicht zwangsläufig und automatisch die Forderungen des Datenschutzes sicher!

.. hint:: Datenschutzaspekte der Software gehören als *user story* ins *backlog*.


Beispiele?
==========

Beispiel: Personenbezogene Daten im iPhone
------------------------------------------

*Personenbezogene Daten* sind Einzelangaben über persönliche oder sachliche Verhältnisse einer bestimmten oder bestimmbaren natürlichen Person.


.. slide:: Personenbezogene Daten sind fast überall
    :level: 2
    :inline-contents: True


    .. figure:: _static/apple_uuids.png
       :alt: personenbezogene Daten im Apple iPhone
       :align: center
       :width: 40%

       Personenbezogene Daten in Apples iPhone unter iOS 10

Bei Nutzung dieser Daten durch Eure Software muss die Erforderlichkeit sichergestellt sein. Diese Art IDs sollten nicht *einfach nur so* von Euren Apps mitgespeichert werden.


Beispiel: Personenbezogene Daten beim Tracking
----------------------------------------------

Das Erstellen von pseudonymen Nutzungsprofilen ist in Grenzen erlaubt. § 15 TMG Abs. 3:

„*(3) Der Diensteanbieter darf für Zwecke der Werbung, der Marktforschung oder zur bedarfsgerechten Gestaltung der Telemedien Nutzungsprofile bei Verwendung von Pseudonymen erstellen, sofern der Nutzer dem nicht widerspricht. Der Diensteanbieter hat den Nutzer auf sein Widerspruchsrecht im Rahmen der Unterrichtung nach § 13 Abs. 1 hinzuweisen.*“

.. slide:: Personenbezogene Daten sind fast überall
    :level: 2
    :inline-contents: True

    .. figure:: _static/bahn_app.png
       :alt: Widerspruchsmöglichkeit gegen Tracking in der Bahn App
       :align: center
       :width: 40%

       Widerspruchsmöglichkeit gegen Tracking in der Bahn App

Jede Form von Tracking muss vom Nutzer erlaubt werden. Die so genannte Cookie-Richtlinie verlangt es, den Nutzer zu informieren und ein Opt-In zu gestalten.\ [#cookies]_



Beispiel: Personenbezogene Daten in der Django Middleware
---------------------------------------------------------

.. slide:: Daten in der Django Middleware
    :level: 2
    :inline-contents: True

    .. code-block:: python
        :emphasize-lines: 2,5,7,8
        :linenos:

        MIDDLEWARE_CLASSES = (
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.common.BrokenLinkEmailsMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
            'django.middleware.security.SecurityMiddleware',
        )
        
In den Zeilen 2,5,7 und 8 werden personenbezogene Daten verarbeitet:

django.contrib.sessions.middleware.SessionMiddleware
    Eine Session ist einem User oder Browser zugeordnet. Unabhängig davon, ob ich ihn kenne oder nicht, ist es eine Person, die über Datenschutzrechte verfügt.
django.middleware.common.BrokenLinkEmailsMiddleware
    Die E-Mail geht an eine Person. Ja, auch der Admin ist eine Person.
django.contrib.auth.middleware.AuthenticationMiddleware
    Diese Middleware ist gerade dazu da, einen eindeutigen Personenbezug herzustellen.
django.contrib.auth.middleware.SessionAuthenticationMiddleware
    Sessionverwaltung, siehe oben.

.. slide:: Daten in der Django Middleware
    :level: 2
    :inline-contents: True

    .. admonition:: Tipps!
    
        Datenschutzerklärung zur Software mitliefern, z. B.:
    
        * Hinweis auf Session-Cookies mit Lebenszeit
        * Speicherung von Admin-Mailadressen
        * Speicherung von Passwort-Hashes



Beispiel: Personenbezogene Daten im Django Datenmodell
------------------------------------------------------

.. slide:: Daten im Django Datenmodell
    :level: 2
    :inline-contents: True

    .. code-block:: python
        :emphasize-lines: 3-5,9,10
        :linenos:

        class Person(AbstractContact):

            user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True,
                                        unique=True, default=None,
                                        related_name='profile')
            newsletter = models.BooleanField(default=True,
                help_text=_('Please check this, if you want to receive our newsletter')
            )
            first_name = models.CharField(_('first name'), max_length=50, blank=True)
            last_name = models.CharField(_('last name'), max_length=50, blank=True)

In diesem Code-Block werden Benutzerdaten (Vorname, Nachname) zu einer digitalen Identität (``user``) zugespeichert.

.. slide:: Daten im Django Datenmodell
    :level: 2
    :inline-contents: True

    .. admonition:: Tipps!
        
        * Datenmodell dokumentieren
        * Berichtigung und Löschung der Daten sicherstellen
        * Datenexport in „nutzbarem“ Format sicherstellen


Beispiel: Personenbezogene Daten im Web-Frontend
------------------------------------------------

Profil- oder Kontaktformulare enthalten personenbezogene Daten. In den Zeilen 8 und 9 werden Formulare automatisch erzeugt, mit denen die Daten durch das Netz an den Client und wieder zurück gesendet werden.

.. slide:: Daten im Web-Frontend
    :level: 2
    :inline-contents: True

    .. code-block:: html
        :emphasize-lines: 8,9
        :linenos:

        <div class="panel panel-primary">
            <div class="panel-heading">
                <h2 class="panel-title">Stammdaten</h2>
            </div>
            <div class="panel-body">
                <form id="profile_form" action="" method="post">
                    {% csrf_token %}
                    {{ user_form|crispy }}
                    {{ profile_form|crispy }}
                    <div>
                        <button class="btn btn-primary pull-right"
                                type="submit"
                                name=”submit”>Speichern</button>
                    </div>
                </form>
            </div>
        </div>



.. slide:: Daten im Web-Frontend
    :level: 2
    :inline-contents: True

    .. admonition:: Tipps!
    
        * Datenmodell dokumentieren
        * Verschlüsselte Datenübertragung (mind. TLS 1.2 mit perfect forward secrecy)
        * Berichtigung und Löschung der Daten sicherstellen
        * Datenexport in „nutzbarem“ Format sicherstellen


.. [#cookies] http://eur-lex.europa.eu/LexUriServ/LexUriServ.do?uri=OJ:L:2009:337:0011:0036:de:PDF
.. [#postgresql] http://www.postgresql.org/docs/current/static/app-initdb.html#APP-INITDB-DATA-CHECKSUMS

.. slide:: Alles klar?
    :level: 1
    
    .. figure:: /_static/editor_faded.png
       :class: fill

    
