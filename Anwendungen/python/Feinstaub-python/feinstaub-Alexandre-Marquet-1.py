"""
Leseformat. Siehe http://cl.ly/ekot
0 Header ' \ xaa '
1 Befehl ' \ xc0 '
2 DATA1 PM2.5 Low-Byte
3 DATA2 PM2.5 High-Byte
4 DATA3 PM10 Low-Byte
5 DATA4 PM10 High-Byte
6 DATA5 ID Byte 1
7 DATA6 ID Byte 2
8 Checksum Low-Byte der Summe der DATA-Bytes
9 Schwanz ' \ xab '
"""

#ustruct  als  struct importieren
import  sys

SDS011_CMDS  = { 'SET' : b ' \ x01 ' ,
        'GET' : b ' \ x00 ' ,
        'QUERY' : b ' \ x04 ' ,
        'REPORTING_MODE' : b ' \ x02 ' ,
        'DUTYCYCLE' : b ' \ x08 ' ,
        'SLEEPWAKE' : b ' \ x06 ' }

Klasse  SDS011 :
    "" "Ein Treiber für den SDS011-Partikelsensor.
    : param uart: Das zu verwendende UART-Objekt.
    "" "
    def  __init__ ( self , uart ):
        selbst . _uart  =  uart
        selbst . _pm25  =  0,0
        selbst . _pm10  =  0,0
        selbst . _packet_status  =  False
        selbst . _packet  = ()

        selbst . set_reporting_mode_query ()

    @ Eigenschaft
    def  pm25 ( selbst ):
        Geben Sie die PM2,5-Konzentration in μg / m 3 zurück.
        kehre  selbst zurück . _pm25

    @ Eigenschaft
    def  pm10 ( selbst ):
        Geben Sie die PM10-Konzentration in μg / m 3 zurück.
        kehre  selbst zurück . _pm10

    @ Eigenschaft
    def  packet_status ( self ):
        "" Gibt False zurück, wenn das empfangene Paket beschädigt ist. ""
        kehre  selbst zurück . _packet_status

    @ Eigenschaft
    def  paket ( selbst ):
        "" "Das zuletzt empfangene Paket zurücksenden." "
        kehre  selbst zurück . _Paket

    def  make_command ( self , cmd , mode , param ):
        header  =  b ' \ xaa \ xb4 '
        padding  =  b ' \ x00 \ x00 \ x00 \ x00 \ x00 \ x00 \ x00 \ x00 \ x00 \ x00 \ xff \ xff '
        Prüfsumme  =  chr (( ord ( cmd ) +  ord ( mode ) +  ord ( param ) +  255  +  255 ) %  256 )
        Prüfsumme  =  Bytes ( Prüfsumme , 'utf8' )
        tail  =  b ' \ xab '

        Return -  Header  +  cmd  +  Modus  +  param  +  Polsterung  +  Prüfsumme  +  tail

    def  wake ( self ):
        "" Sendet den Befehl wake an sds011 (startet den Lüfter). ""
        cmd  =  self . make_command ( _SDS011_CMDS [ 'SLEEPWAKE' ],
                _SDS011_CMDS [ 'SET' ], chr ( 1 ))
        selbst . _uart . schreiben ( cmd )

    def  Schlaf ( Selbst ):
        "" Sendet den Befehl sleep an sds011 (stoppt den Lüfter). ""
        cmd  =  self . make_command ( _SDS011_CMDS [ 'SLEEPWAKE' ],
                _SDS011_CMDS [ 'SET' ], chr ( 0 ))
        selbst . _uart . schreiben ( cmd )

    def  set_reporting_mode_query ( self ):
        cmd  =  self . make_command ( _SDS011_CMDS [ 'REPORTING_MODE' ],
                _SDS011_CMDS [ 'SET' ], chr ( 1 ))
        selbst . _uart . schreiben ( cmd )

    def  Abfrage ( selbst ):
        "" Neue Messdaten abfragen ""
        cmd  =  self . make_command ( _SDS011_CMDS [ 'QUERY' ], chr ( 0 ), chr ( 0 ))
        selbst . _uart . schreiben ( cmd )

    def  process_measurement ( self , Paket ):
        versuche :
            * data , checksum , tail  =  struct . entpacken ( '<HHBBBs' , Paket )
            selbst . _pm25  =  Daten [ 0 ] / 10,0
            selbst . _pm10  =  Daten [ 1 ] / 10.0
            checksum_OK  = ( checksum  == ( Summe ( Daten ) %  256 ))
            tail_OK  =  tail  ==  b ' \ xab '
            selbst . _packet_status  =  True  if ( Checksumme_OK  und  Tail_OK ) else  False
        außer  Ausnahme  als  e :
            print ( 'Problem beim Dekodieren des Pakets:' , e )
            sys . print_exception ( e )

    def  read ( self ):
        "" "
        Fragen Sie eine neue Messung ab, warten Sie auf die Antwort und verarbeiten Sie sie.
        Wartet auf eine Antwort während 512 Zeichen (0,4 s bei 9600 Baud).

        Rückgabe True, wenn eine Antwort empfangen wurde, False overwise.
        "" "
        #Query Messung
        selbst . query ()

        #Messung lesen
        #Lässt bis zu 512 Zeichen fallen, bevor die Suche nach einem Messwert abgebrochen wird.
        für  i  in  range ( 512 ):
            versuche :
                header  =  self . _uart . lesen ( 1 )
                if  header  ==  b ' \ xaa ' :
                    befehl  =  selbst . _uart . lesen ( 1 )

                    if  Befehl  ==  b ' \ xc0 ' :
                        package  =  self . _uart . lesen ( 8 )
                        Wenn  Paket  ! =  Keine :
                            selbst . Prozessmessung ( Paket )
                            return  True
            außer  Ausnahme  als  e :
                print ( 'Problem beim Lesen:' , e )
                sys . print_exception ( e )

        #Wenn wir aufgegeben haben, einen Messwert zu finden, pkt
        return  False