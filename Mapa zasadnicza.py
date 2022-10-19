# Odpowiednio przygotowany plik XXXX_podklad_roboczy.dgn wraz plikiem ksztalty.shx należy wgrać do folderu projektu. Pliki docelowe są wgrywane automatycznie do folderu projektu.

import arcpy
import os

aprx = arcpy.mp.ArcGISProject("CURRENT")

folder = aprx.homeFolder
print(folder)

nr_planu = input("Podaj numer planu: ")

pgdb_name = os.path.join(folder, f"podklad_{nr_planu}.gdb")

print("Creating FileGeoDataBase: {}".format(pgdb_name))
arcpy.management.CreateFileGDB(folder, f"podklad_{nr_planu}.gdb", "CURRENT")
print("Geobaza stworzona")

arcpy.env.workspace = r"{0}\podklad_{1}.gdb".format(folder, nr_planu)
arcpy.env.overwriteOutput = True

workspace = arcpy.env.workspace

mapx = aprx.listMaps("Map")[0]

punktyLyr = mapx.listLayers("PUNKTY")[0]
linieLyr = mapx.listLayers("LINIE")[0]

arcpy.management.DefineProjection(r"{0}\{1}_podklad_roboczy.dgn".format(folder, nr_planu), 'PROJCS["ETRS_1989_Poland_CS2000_Zone_6",GEOGCS["GCS_ETRS_1989",DATUM["D_ETRS_1989",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Transverse_Mercator"],PARAMETER["False_Easting",6500000.0],PARAMETER["False_Northing",0.0],PARAMETER["Central_Meridian",18.0],PARAMETER["Scale_Factor",0.999923],PARAMETER["Latitude_Of_Origin",0.0],UNIT["Meter",1.0]]')

annoLyr = mapx.listLayers("Annotation")[0]
pointLyr = mapx.listLayers("Point")[0]
polyLyr = mapx.listLayers("Polyline")[0]
multiLyr = mapx.listLayers("MultiPatch")[0]
polygonLyr = mapx.listLayers("Polygon")[0]

mapx.removeLayer(annoLyr)
mapx.removeLayer(pointLyr)
mapx.removeLayer(polyLyr)
mapx.removeLayer(multiLyr)
mapx.removeLayer(polygonLyr)

mapx.addDataFromPath(r"{0}\{1}_podklad_roboczy.dgn\Annotation".format(folder, nr_planu))
mapx.addDataFromPath(r"{0}\{1}_podklad_roboczy.dgn\Polyline".format(folder, nr_planu))

rob_polLyr = mapx.listLayers(f"{nr_planu}_podklad_roboczy-Polyline")[0] 
rob_annoLyr = mapx.listLayers(f"{nr_planu}_podklad_roboczy-Annotation")[0] 

mapx.removeLayer(rob_polLyr)
mapx.removeLayer(rob_annoLyr)

# Zmiana nazw dla warstw liniowych

if "BUDOWLE I URZADZENIA" in [layer.name for layer in mapx.listLayers()]:
    budIurzL = mapx.listLayers("BUDOWLE I URZADZENIA")[0]
    budIurzL.name = "BUDOWLE I URZADZENIA 1"
else:
    print("Brak warstwy BUDOWLE_I_URZADZENIA lub cos poszlo nie tak")
if "BUDYNKI" in [lyr.name for lyr in mapx.listLayers()]:
    budL = mapx.listLayers("BUDYNKI")[0]
    budL.name = "BUDYNKI 1"
else:
    print("Brak warstwy BUDYNKI lub cos poszlo nie tak")
if "EWIDENCJA GRUNTOW - DZIALKI" in [layer.name for layer in mapx.listLayers()]:
    ewDzL = mapx.listLayers("EWIDENCJA GRUNTOW - DZIALKI")[0]
    ewDzL.name = "EWIDENCJA GRUNTOW - DZIALKI 1"
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___DZIALKI lub cos poszlo nie tak")
if "EWIDENCJA GRUNTOW - GRANICZNIKI" in [layer.name for layer in mapx.listLayers()]:
    ewGrL = mapx.listLayers("EWIDENCJA GRUNTOW - GRANICZNIKI")[0]
    ewGrL.name = "EWIDENCJA GRUNTOW - GRANICZNIKI 1" 
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___GRANICZNIKI lub cos poszlo nie tak")
if "EWIDENCJA GRUNTOW - GRANICA OBREBU" in [layer.name for layer in mapx.listLayers()]:
    ewGoL = mapx.listLayers("EWIDENCJA GRUNTOW - GRANICA OBREBU")[0]
    ewGoL.name = "EWIDENCJA GRUNTOW - GRANICA OBREBU 1"   
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___GRANICA_OBREBU lub cos poszlo nie tak")
if "EWIDENCJA GRUNTOW - UZYTKI" in [layer.name for layer in mapx.listLayers()]:
    ewUzL = mapx.listLayers("EWIDENCJA GRUNTOW - UZYTKI")[0]
    ewUzL.name = "EWIDENCJA GRUNTOW - UZYTKI 1"
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___UZYTKI lub cos poszlo nie tak")
if "KOMUNIKACJA I TRANSPORT" in [layer.name for layer in mapx.listLayers()]:
    kItrL = mapx.listLayers("KOMUNIKACJA I TRANSPORT")[0]
    kItrL.name = "KOMUNIKACJA I TRANSPORT 1"
else:
    print("Brak warstwy KOMUNIKACJA_I_TRANSPORT lub cos poszlo nie tak")
if "OBIEKTY INNE" in [layer.name for layer in mapx.listLayers()]:
    oInL = mapx.listLayers("OBIEKTY INNE")[0]
    oInL.name = "OBIEKTY INNE 1"
else:
    print("Brak warstwy OBIEKTY_INNE lub cos poszlo nie tak")
if "OBSZAR OPRACOWANIA" in [layer.name for layer in mapx.listLayers()]:
    oOpL = mapx.listLayers("OBSZAR OPRACOWANIA")[0]
    oOpL.name = "OBSZAR OPRACOWANIA 1"
else:
    print("Brak warstwy OBSZAR_OPRACOWANIA lub cos poszlo nie tak")
if "OSNOWA" in [layer.name for layer in mapx.listLayers()]:
    osL = mapx.listLayers("OSNOWA")[0]
    osL.name = "OSNOWA 1"
else:
    print("Brak warstwy OSNOWA lub cos poszlo nie tak")
if "POKRYCIE TERENU" in [layer.name for layer in mapx.listLayers()]:
    pTeL = mapx.listLayers("POKRYCIE TERENU")[0]
    pTeL.name = "POKRYCIE TERENU 1"
else:
    print("Brak warstwy POKRYCIE_TERENU_1 lub cos poszlo nie tak")
if "RZEZBA TERENU" in [layer.name for layer in mapx.listLayers()]:
    rTeL = mapx.listLayers("RZEZBA TERENU")[0]
    rTeL.name = "RZEZBA TERENU 1"
else:
    print("Brak warstwy RZEZBA_TERENU lub cos poszlo nie tak")
if "SIATKA KRZYZY" in [layer.name for layer in mapx.listLayers()]:
    sKrL = mapx.listLayers("SIATKA KRZYZY")[0]
    sKrL.name = "SIATKA KRZYZY 1"
else:
    print("Brak warstwy SIATKA_KRZYZY lub cos poszlo nie tak")
if "SIEC CIEPLOWNICZA" in [layer.name for layer in mapx.listLayers()]:
    sCpL = mapx.listLayers("SIEC CIEPLOWNICZA")[0]
    sCpL.name = "SIEC CIEPLOWNICZA 1"
else:
    print("Brak warstwy SIEC_CIEPLOWNICZA lub cos poszlo nie tak")
if "SIEC ELEKTROENERGETYCZNA" in [layer.name for layer in mapx.listLayers()]:
    sElL = mapx.listLayers("SIEC ELEKTROENERGETYCZNA")[0]
    sElL.name = "SIEC ELEKTROENERGETYCZNA 1"
else:
    print("Brak warstwy SIEC_ELEKTROENERGETYCZNA lub cos poszlo nie tak")
if "SIEC GAZOWA" in [layer.name for layer in mapx.listLayers()]:
    sGaL = mapx.listLayers("SIEC GAZOWA")[0]
    sGaL.name = "SIEC GAZOWA 1"
else:
    print("Brak warstwy SIEC_GAZOWA lub cos poszlo nie tak")
if "SIEC INNA" in [layer.name for layer in mapx.listLayers()]:
    sInL = mapx.listLayers("SIEC INNA")[0]
    sInL.name = "SIEC INNA 1"  
else:
    print("Brak warstwy SIEC_INNA lub cos poszlo nie tak")
if "SIEC KANALIZACYJNA" in [layer.name for layer in mapx.listLayers()]:
    sKaL = mapx.listLayers("SIEC KANALIZACYJNA")[0]
    sKaL.name = "SIEC KANALIZACYJNA 1"
else:
    print("Brak warstwy SIEC_KANALIZACYJNA lub cos poszlo nie tak")
if "SIEC NIEZIDENTYFIKOWANA" in [layer.name for layer in mapx.listLayers()]:
    sNiL = mapx.listLayers("SIEC NIEZIDENTYFIKOWANA")[0]
    sNiL.name = "SIEC NIEZIDENTYFIKOWANA 1"
else:
    print("Brak warstwy SIEC_NIEZIDENTYFIKOWANA lub cos poszlo nie tak")
if "SIEC TELEKOMUNIKACYJNA" in [layer.name for layer in mapx.listLayers()]:
    sTeL = mapx.listLayers("SIEC TELEKOMUNIKACYJNA")[0]
    sTeL.name = "SIEC TELEKOMUNIKACYJNA 1"
else:
    print("Brak warstwy SIEC_TELEKOMUNIKACYJNA lub cos poszlo nie tak")
if "SIEC WODOCIAGOWA" in [layer.name for layer in mapx.listLayers()]:
    sWoL = mapx.listLayers("SIEC WODOCIAGOWA")[0]
    sWoL.name = "SIEC WODOCIAGOWA 1"
else:
    print("Brak warstwy SIEC_WODOCIAGOWA lub cos poszlo nie tak")
if "SIEC NAFTOWA" in [layer.name for layer in mapx.listLayers()]:
    sNaL = mapx.listLayers("SIEC NAFTOWA")[0]
    sNaL.name = "SIEC NAFTOWA 1"
else:
    print("Brak warstwy SIEC_NAFTOWA lub cos poszlo nie tak")
if "SIEC BENZYNOWA" in [layer.name for layer in mapx.listLayers()]:
    sBeL = mapx.listLayers("SIEC BENZYNOWA")[0]
    sBeL.name = "SIEC BENZYNOWA 1"
else:
    print("Brak warstwy SIEC_BENZYNOWA lub cos poszlo nie tak")

# Zapisanie elementów punktowych do geobazy

try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\BUDOWLE I URZADZENIA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\BUDYNKI'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\EWIDENCJA GRUNTOW - DZIALKI'.format(nr_planu), workspace) 
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\EWIDENCJA GRUNTOW - GRANICZNIKI'.format(nr_planu), workspace) 
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\EWIDENCJA GRUNTOW - UZYTKI'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\EWIDENCJA GRUNTOW - GRANICA OBREBU'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\KOMUNIKACJA I TRANSPORT'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\OBIEKTY INNE'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\OBSZAR OPRACOWANIA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\OSNOWA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\POKRYCIE TERENU'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\RZEZBA TERENU'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIATKA KRZYZY'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC CIEPLOWNICZA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC ELEKTROENERGETYCZNA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC GAZOWA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC INNA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC KANALIZACYJNA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC NIEZIDENTYFIKOWANA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC TELEKOMUNIKACYJNA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC WODOCIAGOWA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC NAFTOWA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Annotation Group\SIEC BENZYNOWA'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
    
# Zapisanie elementów liniowych do geobazy
    
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\BUDOWLE I URZADZENIA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\BUDYNKI 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\EWIDENCJA GRUNTOW - DZIALKI 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\EWIDENCJA GRUNTOW - GRANICZNIKI 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\EWIDENCJA GRUNTOW - UZYTKI 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\EWIDENCJA GRUNTOW - GRANICA OBREBU 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\KOMUNIKACJA I TRANSPORT 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\OBIEKTY INNE 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\OBSZAR OPRACOWANIA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\OSNOWA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\POKRYCIE TERENU 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\RZEZBA TERENU 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIATKA KRZYZY 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC CIEPLOWNICZA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC ELEKTROENERGETYCZNA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC GAZOWA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC INNA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC KANALIZACYJNA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC NIEZIDENTYFIKOWANA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC TELEKOMUNIKACYJNA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC WODOCIAGOWA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC NAFTOWA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
try:
    arcpy.conversion.FeatureClassToGeodatabase(r'{}_podklad_roboczy-Polyline Group\SIEC BENZYNOWA 1'.format(nr_planu), workspace)
except arcpy.ExecuteError:
    pass
    print(arcpy.GetMessages())
    
print("Warstwy załadowane do geobazy")

# Dodanie warstw z geobazy do mapy

try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\BUDOWLE_I_URZADZENIA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa BUDOWLE_I_URZADZENIA nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\BUDOWLE_I_URZADZENIA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa BUDOWLE_I_URZADZENIA_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\BUDYNKI".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa BUDYNKI nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\BUDYNKI_1".format(folder, nr_planu))
except RuntimeError:
    #pass
    print("Warstwa BUDYNKI_1 nie istnieje")
    #pass
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\EWIDENCJA_GRUNTOW___DZIALKI".format(folder, nr_planu)) 
except RuntimeError:
    print("Warstwa EWIDENCJA_GRUNTOW___DZIALKI nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\EWIDENCJA_GRUNTOW___DZIALKI_1".format(folder, nr_planu)) 
except RuntimeError:
    print("Warstwa EWIDENCJA_GRUNTOW___DZIALKI_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\EWIDENCJA_GRUNTOW___GRANICZNIKI".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa EWIDENCJA_GRUNTOW___GRANICZNIKI nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\EWIDENCJA_GRUNTOW___GRANICZNIKI_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa EWIDENCJA_GRUNTOW___GRANICZNIKI_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\EWIDENCJA_GRUNTOW___UZYTKI".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa EWIDENCJA_GRUNTOW___UZYTKI nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\EWIDENCJA_GRUNTOW___UZYTKI_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa EWIDENCJA_GRUNTOW___UZYTKI_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\EWIDENCJA_GRUNTOW___GRANICA_OBREBU".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa EWIDENCJA_GRUNTOW___GRANICA_OBREBU nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1 nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\KOMUNIKACJA_I_TRANSPORT".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa KOMUNIKACJA_I_TRANSPORT nie istnieje")
try:  
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\KOMUNIKACJA_I_TRANSPORT_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa KOMUNIKACJA_I_TRANSPORT_1 nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\OBIEKTY_INNE".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa OBIEKTY_INNE nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\OBIEKTY_INNE_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa OBIEKTY_INNE_1 nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\OBSZAR_OPRACOWANIA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa OBSZAR_OPRACOWANIA nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\OBSZAR_OPRACOWANIA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa OBSZAR_OPRACOWANIA_1 nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\OSNOWA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa OSNOWA nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\OSNOWA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa OSNOWA_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\POKRYCIE_TERENU".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa POKRYCIE_TERENU nie istnieje")
try:  
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\POKRYCIE_TERENU_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa POKRYCIE_TERENU_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\RZEZBA_TERENU".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa RZEZBA_TERENU nie istnieje")
try: 
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\RZEZBA_TERENU_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa RZEZBA_TERENU_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIATKA_KRZYZY".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIATKA_KRZYZY nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIATKA_KRZYZY_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIATKA_KRZYZY_1 nie istnieje")
try:  
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_CIEPLOWNICZA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_CIEPLOWNICZA nie istnieje")
try: 
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_CIEPLOWNICZA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_CIEPLOWNICZA_1 nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_ELEKTROENERGETYCZNA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_ELEKTROENERGETYCZNA nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_ELEKTROENERGETYCZNA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_ELEKTROENERGETYCZNA_1 nie istnieje")
try:   
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_GAZOWA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_GAZOWA nie istnieje")
try:  
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_GAZOWA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_GAZOWA_1 nie istnieje")
try:  
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_INNA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_INNA nie istnieje")
try: 
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_INNA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_INNA_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_KANALIZACYJNA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_KANALIZACYJNA nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_KANALIZACYJNA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_KANALIZACYJNA_1 nie istnieje")
try: 
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_NIEZIDENTYFIKOWANA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_NIEZIDENTYFIKOWANA nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_NIEZIDENTYFIKOWANA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_NIEZIDENTYFIKOWANA_1 nie istnieje")
try: 
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_TELEKOMUNIKACYJNA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_TELEKOMUNIKACYJNA nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_TELEKOMUNIKACYJNA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_TELEKOMUNIKACYJNA_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_WODOCIAGOWA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_WODOCIAGOWA nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_WODOCIAGOWA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_WODOCIAGOWA_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_NAFTOWA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_NAFTOWA nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_NAFTOWA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_NAFTOWA_1 nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_BENZYNOWA".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_BENZYNOWA nie istnieje")
try:
    mapx.addDataFromPath(r"{0}\podklad_{1}.gdb\SIEC_BENZYNOWA_1".format(folder, nr_planu))
except RuntimeError:
    print("Warstwa SIEC_BENZYNOWA_1 nie istnieje")

print("Warstwy zaladowane do mapy")

# Usuniecie dgn'a z mapy

robGr_polLyr = mapx.listLayers(f"{nr_planu}_podklad_roboczy-Polyline Group")[0] 
robGr_annoLyr = mapx.listLayers(f"{nr_planu}_podklad_roboczy-Annotation Group")[0] 

mapx.removeLayer(robGr_polLyr)
mapx.removeLayer(robGr_annoLyr)

# Rozszerzone przypisanie warstw i zamiana nazw

if "BUDOWLE_I_URZADZENIA" in [layer.name for layer in mapx.listLayers()] and "BUDOWLE_I_URZADZENIA_1" in [layer.name for layer in mapx.listLayers()]:
    budIurzP = mapx.listLayers("BUDOWLE_I_URZADZENIA")[0]
    budIurzL = mapx.listLayers("BUDOWLE_I_URZADZENIA_1")[0]
elif "BUDOWLE_I_URZADZENIA" in [layer.name for layer in mapx.listLayers()]:
    budIurzL = mapx.listLayers("BUDOWLE_I_URZADZENIA")[0]
    budIurzL.name = "BUDOWLE_I_URZADZENIA_1"
elif "BUDOWLE_I_URZADZENIA_1" in [layer.name for layer in mapx.listLayers()]:
    budIurzL = mapx.listLayers("BUDOWLE_I_URZADZENIA_1")[0]
else:
    pass
if "BUDYNKI" in [lyr.name for lyr in mapx.listLayers()] and "BUDYNKI_1" in [lyr.name for lyr in mapx.listLayers()]:
    budP = mapx.listLayers("BUDYNKI")[0]
    budL = mapx.listLayers("BUDYNKI_1")[0]
elif "BUDYNKI" in [lyr.name for lyr in mapx.listLayers()]:
    budL = mapx.listLayers("BUDYNKI")[0]
    budL.name = "BUDYNKI_1"
elif "BUDYNKI_1" in [lyr.name for lyr in mapx.listLayers()]:
    budL = mapx.listLayers("BUDYNKI_1")[0]
else:
    pass
if "EWIDENCJA_GRUNTOW___DZIALKI" in [layer.name for layer in mapx.listLayers()] and "EWIDENCJA_GRUNTOW___DZIALKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewDzP = mapx.listLayers("EWIDENCJA_GRUNTOW___DZIALKI")[0]
    ewDzL = mapx.listLayers("EWIDENCJA_GRUNTOW___DZIALKI_1")[0]
elif "EWIDENCJA_GRUNTOW___DZIALKI" in [layer.name for layer in mapx.listLayers()]:
    ewDzL = mapx.listLayers("EWIDENCJA_GRUNTOW___DZIALKI")[0]
    ewDzL.name = "EWIDENCJA_GRUNTOW___DZIALKI_1"
elif "EWIDENCJA_GRUNTOW___DZIALKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewDzL = mapx.listLayers("EWIDENCJA_GRUNTOW___DZIALKI_1")[0]
else:
    pass
if "EWIDENCJA_GRUNTOW___GRANICZNIKI" in [layer.name for layer in mapx.listLayers()] and "EWIDENCJA_GRUNTOW___GRANICZNIKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewGrP = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI")[0]
    ewGrL = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI_1")[0]
elif "EWIDENCJA_GRUNTOW___GRANICZNIKI" in [layer.name for layer in mapx.listLayers()]:
    ewGrL = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI")[0]
    ewGrL.name = "EWIDENCJA_GRUNTOW___GRANICZNIKI_1"
elif "EWIDENCJA_GRUNTOW___GRANICZNIKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewGrL = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI_1")[0]
else:
    pass
if "EWIDENCJA_GRUNTOW___GRANICA_OBREBU" in [layer.name for layer in mapx.listLayers()] and "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1" in [layer.name for layer in mapx.listLayers()]:
    ewGoP = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU")[0]
    ewGoL = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1")[0]
elif "EWIDENCJA_GRUNTOW___GRANICA_OBREBU" in [layer.name for layer in mapx.listLayers()]:
    ewGoL = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU")[0]
    ewGoL.name = "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1"
elif "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1" in [layer.name for layer in mapx.listLayers()]:
    ewGoL = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1")[0]
else:
    pass
if "EWIDENCJA_GRUNTOW___UZYTKI" in [layer.name for layer in mapx.listLayers()] and "EWIDENCJA_GRUNTOW___UZYTKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewUzP = mapx.listLayers("EWIDENCJA_GRUNTOW___UZYTKI")[0]
    ewUzL = mapx.listLayers("EWIDENCJA_GRUNTOW___UZYTKI_1")[0]
elif "EWIDENCJA_GRUNTOW___UZYTKI" in [layer.name for layer in mapx.listLayers()]:
    ewUzL = mapx.listLayers("EWIDENCJA_GRUNTOW___UZYTKI")[0]
    ewUzL.name = "EWIDENCJA_GRUNTOW___UZYTKI_1"
elif "EWIDENCJA_GRUNTOW___UZYTKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewUzL = mapx.listLayers("EWIDENCJA_GRUNTOW___UZYTKI_1")[0]
else:
    pass
if "KOMUNIKACJA_I_TRANSPORT" in [layer.name for layer in mapx.listLayers()] and "KOMUNIKACJA_I_TRANSPORT_1" in [layer.name for layer in mapx.listLayers()]:
    kItrP = mapx.listLayers("KOMUNIKACJA_I_TRANSPORT")[0]
    kItrL = mapx.listLayers("KOMUNIKACJA_I_TRANSPORT_1")[0]
elif "KOMUNIKACJA_I_TRANSPORT" in [layer.name for layer in mapx.listLayers()]:
    kItrL = mapx.listLayers("KOMUNIKACJA_I_TRANSPORT")[0]
    kItrL.name = "KOMUNIKACJA_I_TRANSPORT_1"
elif "KOMUNIKACJA_I_TRANSPORT_1" in [layer.name for layer in mapx.listLayers()]:
    kItrL = mapx.listLayers("KOMUNIKACJA_I_TRANSPORT_1")[0]
else:
    pass
if "OBIEKTY_INNE" in [layer.name for layer in mapx.listLayers()] and "OBIEKTY_INNE_1" in [layer.name for layer in mapx.listLayers()]:
    oInP = mapx.listLayers("OBIEKTY_INNE")[0]
    oInL = mapx.listLayers("OBIEKTY_INNE_1")[0]
elif "OBIEKTY_INNE" in [layer.name for layer in mapx.listLayers()]:
    oInL = mapx.listLayers("OBIEKTY_INNE")[0]
    oInL.name = "OBIEKTY_INNE_1"
elif "OBIEKTY_INNE_1" in [layer.name for layer in mapx.listLayers()]:
    oInL = mapx.listLayers("OBIEKTY_INNE_1")[0]
else:
    pass
if "OBSZAR_OPRACOWANIA" in [layer.name for layer in mapx.listLayers()] and "OBSZAR_OPRACOWANIA_1" in [layer.name for layer in mapx.listLayers()]:
    oOpP = mapx.listLayers("OBSZAR_OPRACOWANIA")[0]
    oOpL = mapx.listLayers("OBSZAR_OPRACOWANIA_1")[0]
elif "OBSZAR_OPRACOWANIA" in [layer.name for layer in mapx.listLayers()]:
    oOpL = mapx.listLayers("OBSZAR_OPRACOWANIA")[0]
    oOpL.name = "OBSZAR_OPRACOWANIA_1"
elif "OBSZAR_OPRACOWANIA_1" in [layer.name for layer in mapx.listLayers()]:
    oOpL = mapx.listLayers("OBSZAR_OPRACOWANIA_1")[0]
else:
    pass
if "OSNOWA" in [layer.name for layer in mapx.listLayers()] and "OSNOWA_1" in [layer.name for layer in mapx.listLayers()]:
    osP = mapx.listLayers("OSNOWA")[0]
    osL = mapx.listLayers("OSNOWA_1")[0]
elif "OSNOWA" in [layer.name for layer in mapx.listLayers()]:
    osL = mapx.listLayers("OSNOWA")[0]
    osL.name = "OSNOWA_1"
elif "OSNOWA_1" in [layer.name for layer in mapx.listLayers()]:
    osL = mapx.listLayers("OSNOWA_1")[0]
else:
    pass
if "POKRYCIE_TERENU" in [layer.name for layer in mapx.listLayers()] and "POKRYCIE_TERENU_1" in [layer.name for layer in mapx.listLayers()]:
    pTeP = mapx.listLayers("POKRYCIE_TERENU")[0]
    pTeL = mapx.listLayers("POKRYCIE_TERENU_1")[0]
elif "POKRYCIE_TERENU" in [layer.name for layer in mapx.listLayers()]:
    pTeL = mapx.listLayers("POKRYCIE_TERENU")[0]
    pTeL.name = "POKRYCIE_TERENU_1"
elif "POKRYCIE_TERENU_1" in [layer.name for layer in mapx.listLayers()]:
    pTeL = mapx.listLayers("POKRYCIE_TERENU_1")[0]
else:
    pass
if "RZEZBA_TERENU" in [layer.name for layer in mapx.listLayers()] and "RZEZBA_TERENU_1" in [layer.name for layer in mapx.listLayers()]:
    rTeP = mapx.listLayers("RZEZBA_TERENU")[0]
    rTeL = mapx.listLayers("RZEZBA_TERENU_1")[0]
elif "RZEZBA_TERENU" in [layer.name for layer in mapx.listLayers()]:
    rTeL = mapx.listLayers("RZEZBA_TERENU")[0]
    rTeL.name = "RZEZBA_TERENU_1"
elif "RZEZBA_TERENU_1" in [layer.name for layer in mapx.listLayers()]:
    rTeL = mapx.listLayers("RZEZBA_TERENU_1")[0]
else:
    pass
if "SIATKA_KRZYZY" in [layer.name for layer in mapx.listLayers()] and "SIATKA_KRZYZY_1" in [layer.name for layer in mapx.listLayers()]:
    sKrP = mapx.listLayers("SIATKA_KRZYZY")[0]
    sKrL = mapx.listLayers("SIATKA_KRZYZY_1")[0]
elif "SIATKA_KRZYZY" in [layer.name for layer in mapx.listLayers()]:
    sKrL = mapx.listLayers("SIATKA_KRZYZY")[0]
    sKrL.name = "SIATKA_KRZYZY_1"
elif "SIATKA_KRZYZY_1" in [layer.name for layer in mapx.listLayers()]:
    sKrL = mapx.listLayers("SIATKA_KRZYZY_1")[0]
else:
    pass
if "SIEC_CIEPLOWNICZA" in [layer.name for layer in mapx.listLayers()] and "SIEC_CIEPLOWNICZA_1" in [layer.name for layer in mapx.listLayers()]:
    sCpP = mapx.listLayers("SIEC_CIEPLOWNICZA")[0]
    sCpL = mapx.listLayers("SIEC_CIEPLOWNICZA_1")[0]
elif "SIEC_CIEPLOWNICZA" in [layer.name for layer in mapx.listLayers()]:
    sCpL = mapx.listLayers("SIEC_CIEPLOWNICZA")[0]
    sCpL.name = "SIEC_CIEPLOWNICZA_1"
elif "SIEC_CIEPLOWNICZA_1" in [layer.name for layer in mapx.listLayers()]:
    sCpL = mapx.listLayers("SIEC_CIEPLOWNICZA_1")[0]
else:
    pass
if "SIEC_ELEKTROENERGETYCZNA" in [layer.name for layer in mapx.listLayers()] and "SIEC_ELEKTROENERGETYCZNA_1" in [layer.name for layer in mapx.listLayers()]:
    sElP = mapx.listLayers("SIEC_ELEKTROENERGETYCZNA")[0]
    sElL = mapx.listLayers("SIEC_ELEKTROENERGETYCZNA_1")[0]
elif "SIEC_ELEKTROENERGETYCZNA" in [layer.name for layer in mapx.listLayers()]:
    sElL = mapx.listLayers("SIEC_ELEKTROENERGETYCZNA")[0]
    sElL.name = "SIEC_ELEKTROENERGETYCZNA_1"
elif "SIEC_ELEKTROENERGETYCZNA_1" in [layer.name for layer in mapx.listLayers()]:
    sElL = mapx.listLayers("SIEC_ELEKTROENERGETYCZNA_1")[0]
else:
    pass
if "SIEC_GAZOWA" in [layer.name for layer in mapx.listLayers()] and "SIEC_GAZOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sGaP = mapx.listLayers("SIEC_GAZOWA")[0]
    sGaL = mapx.listLayers("SIEC_GAZOWA_1")[0]
elif "SIEC_GAZOWA" in [layer.name for layer in mapx.listLayers()]:
    sGaL = mapx.listLayers("SIEC_GAZOWA")[0]
    sGaL.name = "SIEC_GAZOWA_1"
elif "SIEC_GAZOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sGaL = mapx.listLayers("SIEC_GAZOWA_1")[0]
else:
    pass
if "SIEC_INNA" in [layer.name for layer in mapx.listLayers()] and "SIEC_INNA_1" in [layer.name for layer in mapx.listLayers()]:
    sInP = mapx.listLayers("SIEC_INNA")[0]
    sInL = mapx.listLayers("SIEC_INNA_1")[0]
elif "SIEC_INNA" in [layer.name for layer in mapx.listLayers()]:
    sInL = mapx.listLayers("SIEC_INNA")[0]
    sInL.name = "SIEC_INNA_1"
elif "SIEC_INNA_1" in [layer.name for layer in mapx.listLayers()]:
    sInL = mapx.listLayers("SIEC_INNA_1")[0]  
else:
    pass
if "SIEC_KANALIZACYJNA" in [layer.name for layer in mapx.listLayers()] and "SIEC_KANALIZACYJNA_1" in [layer.name for layer in mapx.listLayers()]:
    sKaP = mapx.listLayers("SIEC_KANALIZACYJNA")[0]
    sKaL = mapx.listLayers("SIEC_KANALIZACYJNA_1")[0]
elif "SIEC_KANALIZACYJNA" in [layer.name for layer in mapx.listLayers()]:
    sKaL = mapx.listLayers("SIEC_KANALIZACYJNA")[0]
    sKaL.name = "SIEC_KANALIZACYJNA_1"
elif "SIEC_KANALIZACYJNA_1" in [layer.name for layer in mapx.listLayers()]:
    sKaL = mapx.listLayers("SIEC_KANALIZACYJNA_1")[0]
else:
    pass
if "SIEC_NIEZIDENTYFIKOWANA" in [layer.name for layer in mapx.listLayers()] and "SIEC_NIEZIDENTYFIKOWANA_1" in [layer.name for layer in mapx.listLayers()]:
    sNiP = mapx.listLayers("SIEC_NIEZIDENTYFIKOWANA")[0]
    sNiL = mapx.listLayers("SIEC_NIEZIDENTYFIKOWANA_1")[0]
elif "SIEC_NIEZIDENTYFIKOWANA" in [layer.name for layer in mapx.listLayers()]:
    sNiL = mapx.listLayers("SIEC_NIEZIDENTYFIKOWANA")[0]
    sNiL.name = "SIEC_NIEZIDENTYFIKOWANA_1"
elif "SIEC_NIEZIDENTYFIKOWANA_1" in [layer.name for layer in mapx.listLayers()]:
    sNiL = mapx.listLayers("SIEC_NIEZIDENTYFIKOWANA_1")[0]
else:
    pass
if "SIEC_TELEKOMUNIKACYJNA" in [layer.name for layer in mapx.listLayers()] and "SIEC_TELEKOMUNIKACYJNA_1" in [layer.name for layer in mapx.listLayers()]:
    sTeP = mapx.listLayers("SIEC_TELEKOMUNIKACYJNA")[0]
    sTeL = mapx.listLayers("SIEC_TELEKOMUNIKACYJNA_1")[0]
elif "SIEC_TELEKOMUNIKACYJNA" in [layer.name for layer in mapx.listLayers()]:
    sTeL = mapx.listLayers("SIEC_TELEKOMUNIKACYJNA")[0]
    sTeL.name = "SIEC_TELEKOMUNIKACYJNA_1"
elif "SIEC_TELEKOMUNIKACYJNA_1" in [layer.name for layer in mapx.listLayers()]:
    sTeL = mapx.listLayers("SIEC_TELEKOMUNIKACYJNA_1")[0]
else:
    pass
if "SIEC_WODOCIAGOWA" in [layer.name for layer in mapx.listLayers()] and "SIEC_WODOCIAGOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sWoP = mapx.listLayers("SIEC_WODOCIAGOWA")[0]
    sWoL = mapx.listLayers("SIEC_WODOCIAGOWA_1")[0]
elif "SIEC_WODOCIAGOWA" in [layer.name for layer in mapx.listLayers()]:
    sWoL = mapx.listLayers("SIEC_WODOCIAGOWA")[0]
    sWoL.name = "SIEC_WODOCIAGOWA_1"
elif "SIEC_WODOCIAGOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sWoL = mapx.listLayers("SIEC_WODOCIAGOWA_1")[0]
else:
    pass
if "SIEC_NAFTOWA" in [layer.name for layer in mapx.listLayers()] and "SIEC_NAFTOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sNaP = mapx.listLayers("SIEC_NAFTOWA")[0]
    sNaL = mapx.listLayers("SIEC_NAFTOWA_1")[0]
elif "SIEC_NAFTOWA" in [layer.name for layer in mapx.listLayers()]:
    sNaL = mapx.listLayers("SIEC_NAFTOWA")[0]
    sNaL.name = "SIEC_NAFTOWA_1"
elif "SIEC_NAFTOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sNaL = mapx.listLayers("SIEC_NAFTOWA_1")[0]
else:
    pass
if "SIEC_BENZYNOWA" in [layer.name for layer in mapx.listLayers()] and "SIEC_BENZYNOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sBeP = mapx.listLayers("SIEC_BENZYNOWA")[0]
    sBeL = mapx.listLayers("SIEC_BENZYNOWA_1")[0]
elif "SIEC_BENZYNOWA" in [layer.name for layer in mapx.listLayers()]:
    sBeL = mapx.listLayers("SIEC_BENZYNOWA")[0]
    sBeL.name = "SIEC_BENZYNOWA_1"
elif "SIEC_BENZYNOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sBeL = mapx.listLayers("SIEC_BENZYNOWA_1")[0]
else:
    pass

print("Warstwy zdefiniowane")

# Przeniesienie warstw do warstw: PUNKTY i LINIE

try:
    if budIurzL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, budIurzL)
        mapx.removeLayer(budIurzL)
    elif budIurzL.isFeatureLayer == False and budIurzP == True:
        mapx.addLayerToGroup(linieLyr, budIurzP)
        mapx.removeLayer(budIurzP)
    else:
        print("Brak warstwy budIurzL lub cos poszlo nie tak") 
except NameError:
    pass
try:
    if budIurzP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, budIurzP)
        mapx.removeLayer(budIurzP)
    else:
        print("Brak warstwy budIurzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if budL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, budL)
        mapx.removeLayer(budL)
    elif budL.isFeatureLayer == False and budP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, budP)
        mapx.removeLayer(budP)
    else:
        print("Brak warstwy budL lub cos poszlo nie tak")  
except NameError:
    pass
try:
    if budP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, budP)
        mapx.removeLayer(budP)
    else:
        print("Brak warstwy budP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewDzL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, ewDzL)
        mapx.removeLayer(ewDzL)
    elif ewDzL.isFeatureLayer == False and ewDzP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, ewDzP)
        mapx.removeLayer(ewDzP)
    else:
        print("Brak warstwy ewDzL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewDzP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, ewDzP)
        mapx.removeLayer(ewDzP)
    else:
        print("Brak warstwy ewDzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGrL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, ewGrL)
        mapx.removeLayer(ewGrL)
    elif ewGrL.isFeatureLayer == False and ewGrP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, ewGrP)
        mapx.removeLayer(ewGrP)
    else:
        print("Brak warstwy ewGrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGrP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, ewGrP)
        mapx.removeLayer(ewGrP)
    else:
        print("Brak warstwy ewGrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGoL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, ewGoL)
        mapx.removeLayer(ewGoL)
    elif ewGoL.isFeatureLayer == False and ewGoP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, ewGoP)
        mapx.removeLayer(ewGoP)
    else:
        print("Brak warstwy ewGoL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGoP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, ewGoP)
        mapx.removeLayer(ewGoP)
    else:
        print("Brak warstwy ewGoP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewUzL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, ewUzL)
        mapx.removeLayer(ewUzL)
    elif ewUzL.isFeatureLayer == False and ewUzP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, ewUzP)
        mapx.removeLayer(ewUzP)
    else:
        print("Brak warstwy ewUzL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewUzP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, ewUzP)
        mapx.removeLayer(ewUzP)
    else:
        print("Brak warstwy ewUzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if kItrL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, kItrL)
        mapx.removeLayer(kItrL)
    elif kItrL.isFeatureLayer == False and kItrP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, kItrP)
        mapx.removeLayer(kItrP)
    else:
        print("Brak warstwy kItrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if kItrP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, kItrP)
        mapx.removeLayer(kItrP)
    else:
        print("Brak warstwy kItrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oInL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, oInL)
        mapx.removeLayer(oInL)
    elif oInL.isFeatureLayer == False and oInP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, oInP)
        mapx.removeLayer(oInP)
    else:
        print("Brak warstwy oInL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oInP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, oInP)
        mapx.removeLayer(oInP)
    else:
        print("Brak warstwy oInP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oOpL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, oOpL)
        mapx.removeLayer(oOpL)
    elif oOpL.isFeatureLayer == False and oOpP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, oOpP)
        mapx.removeLayer(oOpP)
    else:
        print("Brak warstwy oOpL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oOpP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, oOpP)
        mapx.removeLayer(oOpP)
    else:
        print("Brak warstwy oOpP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if osL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, osL)
        mapx.removeLayer(osL)
    elif osL.isFeatureLayer == False and osP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, osP)
        mapx.removeLayer(osP)
    else:
        print("Brak warstwy osL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if osP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, osP)
        mapx.removeLayer(osP)
    else:
        print("Brak warstwy osP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if pTeL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, pTeL)
        mapx.removeLayer(pTeL)
    elif pTeL.isFeatureLayer == False and pTeP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, pTeP)
        mapx.removeLayer(pTeP)
    else:
        print("Brak warstwy pTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if pTeP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, pTeP)
        mapx.removeLayer(pTeP)
    else:
        print("Brak warstwy pTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if rTeL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, rTeL)
        mapx.removeLayer(rTeL)
    elif rTeL.isFeatureLayer == False and rTeP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, rTeP)
        mapx.removeLayer(rTeP)
    else:
        print("Brak warstwy rTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if rTeP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, rTeP)
        mapx.removeLayer(rTeP)
    else:
        print("Brak warstwy rTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKrL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sKrL)
        mapx.removeLayer(sKrL)
    elif sKrL.isFeatureLayer == False and sKrP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sKrP)
        mapx.removeLayer(sKrP)
    else:
        print("Brak warstwy sKrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKrP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sKrP)
        mapx.removeLayer(sKrP)
    else:
        print("Brak warstwy sKrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sCpL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sCpL)
        mapx.removeLayer(sCpL)
    elif sCpL.isFeatureLayer == False and sCpP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sCpP)
        mapx.removeLayer(sCpP)
    else:
        print("Brak warstwy sCpL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sCpP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sCpP)
        mapx.removeLayer(sCpP)
    else:
        print("Brak warstwy sCpP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sElL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sElL)
        mapx.removeLayer(sElL)
    elif sElL.isFeatureLayer == False and sElP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sElP)
        mapx.removeLayer(sElP)
    else:
        print("Brak warstwy sElL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sElP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sElP)
        mapx.removeLayer(sElP)
    else:
        print("Brak warstwy sElP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sGaL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sGaL)
        mapx.removeLayer(sGaL)
    elif sGaL.isFeatureLayer == False and sGaP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sGaP)
        mapx.removeLayer(sGaP)
    else:
        print("Brak warstwy sGaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sGaP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sGaP)
        mapx.removeLayer(sGaP)
    else:
        print("Brak warstwy sGaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sInL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sInL)
        mapx.removeLayer(sInL)
    elif sInL.isFeatureLayer == False and sInP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sInP)
        mapx.removeLayer(sInP)
    else:
        print("Brak warstwy sInL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sInP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sInP)
        mapx.removeLayer(sInP)
    else:
        print("Brak warstwy sInP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKaL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sKaL)
        mapx.removeLayer(sKaL)
    elif sKaL.isFeatureLayer == False and sKaP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sKaP)
        mapx.removeLayer(sKaP)
    else:
        print("Brak warstwy sKaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKaP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sKaP)
        mapx.removeLayer(sKaP)
    else:
        print("Brak warstwy sKaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNiL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sNiL)
        mapx.removeLayer(sNiL)
    elif sNiL.isFeatureLayer == False and sNiP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sNiP)
        mapx.removeLayer(sNiP)
    else:
        print("Brak warstwy sNiL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNiP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sNiP)
        mapx.removeLayer(sNiP)
    else:
        print("Brak warstwy sNiP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sTeL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sTeL)
        mapx.removeLayer(sTeL)
    elif sTeL.isFeatureLayer == False and sTeP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sTeP)
        mapx.removeLayer(sTeP)
    else:
        print("Brak warstwy sTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sTeP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sTeP)
        mapx.removeLayer(sTeP)
    else:
        print("Brak warstwy sTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sWoL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sWoL)
        mapx.removeLayer(sWoL)
    elif sWoL.isFeatureLayer == False and sWoP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sWoP)
        mapx.removeLayer(sWoP)
    else:
        print("Brak warstwy sWoL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sWoP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sWoP)
        mapx.removeLayer(sWoP)
    else:
        print("Brak warstwy sWoP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNaL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sNaL)
        mapx.removeLayer(sNaL)
    elif sNaL.isFeatureLayer == False and sNaP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sNaP)
        mapx.removeLayer(sNaP)
    else:
        print("Brak warstwy sNaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNaP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sNaP)
        mapx.removeLayer(sNaP)
    else:
        print("Brak warstwy sNaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sBeL.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sBeL)
        mapx.removeLayer(sBeL)
    elif sBeL.isFeatureLayer == False and sBeP.isFeatureLayer == True:
        mapx.addLayerToGroup(linieLyr, sBeP)
        mapx.removeLayer(sBeP)
    else:
        print("Brak warstwy sBeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sBeP.isFeatureLayer == True:
        mapx.addLayerToGroup(punktyLyr, sBeP)
        mapx.removeLayer(sBeP)
    else:
        print("Brak warstwy sBeP lub cos poszlo nie tak")
except NameError:
    pass

print("Warstwy punktowe i liniowe przeniesione w odpowiednie miejsce")

# Ponowne przypisanie warstw - uproszczone

if "BUDOWLE_I_URZADZENIA" in [layer.name for layer in mapx.listLayers()]:
    budIurzP = mapx.listLayers("BUDOWLE_I_URZADZENIA")[0]
else:
    print("Brak warstwy BUDOWLE_I_URZADZENIA lub cos poszlo nie tak")
if "BUDOWLE_I_URZADZENIA_1" in [layer.name for layer in mapx.listLayers()]:
    budIurzL = mapx.listLayers("BUDOWLE_I_URZADZENIA_1")[0]
else:
    print("Brak warstwy BUDOWLE_I_URZADZENIA_1 lub cos poszlo nie tak")
if "BUDYNKI" in [lyr.name for lyr in mapx.listLayers()]:
    budP = mapx.listLayers("BUDYNKI")[0]
else:
    print("Brak warstwy BUDYNKI lub cos poszlo nie tak")
if "BUDYNKI_1" in [lyr.name for lyr in mapx.listLayers()]:
    budL = mapx.listLayers("BUDYNKI_1")[0]
else:
    print("Brak warstwy BUDYNKI_1 lub cos poszlo nie tak")
if "EWIDENCJA_GRUNTOW___DZIALKI" in [layer.name for layer in mapx.listLayers()]:
    ewDzP = mapx.listLayers("EWIDENCJA_GRUNTOW___DZIALKI")[0]
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___DZIALKI lub cos poszlo nie tak")
if "EWIDENCJA_GRUNTOW___DZIALKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewDzL = mapx.listLayers("EWIDENCJA_GRUNTOW___DZIALKI_1")[0]
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___DZIALKI_1 lub cos poszlo nie tak")
if "EWIDENCJA_GRUNTOW___GRANICZNIKI" in [layer.name for layer in mapx.listLayers()]:
    ewGrP = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI")[0]
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___GRANICZNIKI lub cos poszlo nie tak")
if "EWIDENCJA_GRUNTOW___GRANICZNIKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewGrL = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICZNIKI_1")[0]
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___GRANICZNIKI_1 lub cos poszlo nie tak")
if "EWIDENCJA_GRUNTOW___GRANICA_OBREBU" in [layer.name for layer in mapx.listLayers()]:
    ewGoP = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU")[0]
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___GRANICA_OBREBU lub cos poszlo nie tak")
if "EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1" in [layer.name for layer in mapx.listLayers()]:
    ewGoL = mapx.listLayers("EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1")[0]
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___GRANICA_OBREBU_1 lub cos poszlo nie tak")
if "EWIDENCJA_GRUNTOW___UZYTKI" in [layer.name for layer in mapx.listLayers()]:
    ewUzP = mapx.listLayers("EWIDENCJA_GRUNTOW___UZYTKI")[0]
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___UZYTKI lub cos poszlo nie tak")
if "EWIDENCJA_GRUNTOW___UZYTKI_1" in [layer.name for layer in mapx.listLayers()]:
    ewUzL = mapx.listLayers("EWIDENCJA_GRUNTOW___UZYTKI_1")[0]
else:
    print("Brak warstwy EWIDENCJA_GRUNTOW___UZYTKI_1 lub cos poszlo nie tak")
if "KOMUNIKACJA_I_TRANSPORT" in [layer.name for layer in mapx.listLayers()]:
    kItrP = mapx.listLayers("KOMUNIKACJA_I_TRANSPORT")[0]
else:
    print("Brak warstwy KOMUNIKACJA_I_TRANSPORT lub cos poszlo nie tak")
if "KOMUNIKACJA_I_TRANSPORT_1" in [layer.name for layer in mapx.listLayers()]:
    kItrL = mapx.listLayers("KOMUNIKACJA_I_TRANSPORT_1")[0]
else:
    print("Brak warstwy KOMUNIKACJA_I_TRANSPORT_1 lub cos poszlo nie tak")
if "OBIEKTY_INNE" in [layer.name for layer in mapx.listLayers()]:
    oInP = mapx.listLayers("OBIEKTY_INNE")[0]
else:
    print("Brak warstwy OBIEKTY_INNE lub cos poszlo nie tak")
if "OBIEKTY_INNE_1" in [layer.name for layer in mapx.listLayers()]:
    oInL = mapx.listLayers("OBIEKTY_INNE_1")[0]
else:
    print("Brak warstwy OBIEKTY_INNE_1 lub cos poszlo nie tak")
if "OBSZAR_OPRACOWANIA" in [layer.name for layer in mapx.listLayers()]:
    oOpP = mapx.listLayers("OBSZAR_OPRACOWANIA")[0]
else:
    print("Brak warstwy OBSZAR_OPRACOWANIA lub cos poszlo nie tak")
if "OBSZAR_OPRACOWANIA_1" in [layer.name for layer in mapx.listLayers()]:
    oOpL = mapx.listLayers("OBSZAR_OPRACOWANIA_1")[0]
else:
    print("Brak warstwy OBSZAR_OPRACOWANIA_1 lub cos poszlo nie tak")
if "OSNOWA" in [layer.name for layer in mapx.listLayers()]:
    osP = mapx.listLayers("OSNOWA")[0]
else:
    print("Brak warstwy OSNOWA lub cos poszlo nie tak")
if "OSNOWA_1" in [layer.name for layer in mapx.listLayers()]:
    osL = mapx.listLayers("OSNOWA_1")[0]
else:
    print("Brak warstwy OSNOWA_1 lub cos poszlo nie tak")
if "POKRYCIE_TERENU" in [layer.name for layer in mapx.listLayers()]:
    pTeP = mapx.listLayers("POKRYCIE_TERENU")[0]
else:
    print("Brak warstwy POKRYCIE_TERENU_1 lub cos poszlo nie tak")
if "POKRYCIE_TERENU_1" in [layer.name for layer in mapx.listLayers()]:
    pTeL = mapx.listLayers("POKRYCIE_TERENU_1")[0]
else:
    print("Brak warstwy POKRYCIE_TERENU lub cos poszlo nie tak")
if "RZEZBA_TERENU" in [layer.name for layer in mapx.listLayers()]:
    rTeP = mapx.listLayers("RZEZBA_TERENU")[0]
else:
    print("Brak warstwy RZEZBA_TERENU lub cos poszlo nie tak")
if "RZEZBA_TERENU_1" in [layer.name for layer in mapx.listLayers()]:
    rTeL = mapx.listLayers("RZEZBA_TERENU_1")[0]
else:
    print("Brak warstwy RZEZBA_TERENU_1 lub cos poszlo nie tak")
if "SIATKA_KRZYZY" in [layer.name for layer in mapx.listLayers()]:
    sKrP = mapx.listLayers("SIATKA_KRZYZY")[0]
else:
    print("Brak warstwy SIATKA_KRZYZY lub cos poszlo nie tak")
if "SIATKA_KRZYZY_1" in [layer.name for layer in mapx.listLayers()]:
    sKrL = mapx.listLayers("SIATKA_KRZYZY_1")[0]
else:
    print("Brak warstwy SIATKA_KRZYZY_1 lub cos poszlo nie tak")
if "SIEC_CIEPLOWNICZA" in [layer.name for layer in mapx.listLayers()]:
    sCpP = mapx.listLayers("SIEC_CIEPLOWNICZA")[0]
else:
    print("Brak warstwy SIEC_CIEPLOWNICZA lub cos poszlo nie tak")
if "SIEC_CIEPLOWNICZA_1" in [layer.name for layer in mapx.listLayers()]:
    sCpL = mapx.listLayers("SIEC_CIEPLOWNICZA_1")[0]
else:
    print("Brak warstwy SIEC_CIEPLOWNICZA_1 lub cos poszlo nie tak")
if "SIEC_ELEKTROENERGETYCZNA" in [layer.name for layer in mapx.listLayers()]:
    sElP = mapx.listLayers("SIEC_ELEKTROENERGETYCZNA")[0]
else:
    print("Brak warstwy SIEC_ELEKTROENERGETYCZNA lub cos poszlo nie tak")
if "SIEC_ELEKTROENERGETYCZNA_1" in [layer.name for layer in mapx.listLayers()]:
    sElL = mapx.listLayers("SIEC_ELEKTROENERGETYCZNA_1")[0]
else:
    print("Brak warstwy SIEC_ELEKTROENERGETYCZNA_1 lub cos poszlo nie tak")
if "SIEC_GAZOWA" in [layer.name for layer in mapx.listLayers()]:
    sGaP = mapx.listLayers("SIEC_GAZOWA")[0]
else:
    print("Brak warstwy SIEC_GAZOWA lub cos poszlo nie tak")
if "SIEC_GAZOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sGaL = mapx.listLayers("SIEC_GAZOWA_1")[0]
else:
    print("Brak warstwy SIEC_GAZOWA_1 lub cos poszlo nie tak")
if "SIEC_INNA" in [layer.name for layer in mapx.listLayers()]:
    sInP = mapx.listLayers("SIEC_INNA")[0]
else:
    print("Brak warstwy SIEC_INNA lub cos poszlo nie tak")
if "SIEC_INNA_1" in [layer.name for layer in mapx.listLayers()]:
    sInL = mapx.listLayers("SIEC_INNA_1")[0]
else:
    print("Brak warstwy SIEC_INNA_1 lub cos poszlo nie tak")
if "SIEC_KANALIZACYJNA" in [layer.name for layer in mapx.listLayers()]:
    sKaP = mapx.listLayers("SIEC_KANALIZACYJNA")[0]
else:
    print("Brak warstwy SIEC_KANALIZACYJNA lub cos poszlo nie tak")
if "SIEC_KANALIZACYJNA_1" in [layer.name for layer in mapx.listLayers()]:
    sKaL = mapx.listLayers("SIEC_KANALIZACYJNA_1")[0]
else:
    print("Brak warstwy SIEC_KANALIZACYJNA_1 lub cos poszlo nie tak")
if "SIEC_NIEZIDENTYFIKOWANA" in [layer.name for layer in mapx.listLayers()]:
    sNiP = mapx.listLayers("SIEC_NIEZIDENTYFIKOWANA")[0]
else:
    print("Brak warstwy SIEC_NIEZIDENTYFIKOWANA lub cos poszlo nie tak")
if "SIEC_NIEZIDENTYFIKOWANA_1" in [layer.name for layer in mapx.listLayers()]:
    sNiL = mapx.listLayers("SIEC_NIEZIDENTYFIKOWANA_1")[0]
else:
    print("Brak warstwy SIEC_NIEZIDENTYFIKOWANA_1 lub cos poszlo nie tak")
if "SIEC_TELEKOMUNIKACYJNA" in [layer.name for layer in mapx.listLayers()]:
    sTeP = mapx.listLayers("SIEC_TELEKOMUNIKACYJNA")[0]
else:
    print("Brak warstwy SIEC_TELEKOMUNIKACYJNA lub cos poszlo nie tak")
if "SIEC_TELEKOMUNIKACYJNA_1" in [layer.name for layer in mapx.listLayers()]:
    sTeL = mapx.listLayers("SIEC_TELEKOMUNIKACYJNA_1")[0]
else:
    print("Brak warstwy SIEC_TELEKOMUNIKACYJNA_1 lub cos poszlo nie tak")
if "SIEC_WODOCIAGOWA" in [layer.name for layer in mapx.listLayers()]:
    sWoP = mapx.listLayers("SIEC_WODOCIAGOWA")[0]
else:
    print("Brak warstwy SIEC_WODOCIAGOWA lub cos poszlo nie tak")
if "SIEC_WODOCIAGOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sWoL = mapx.listLayers("SIEC_WODOCIAGOWA_1")[0] 
else:
    print("Brak warstwy SIEC_WODOCIAGOWA_1 lub cos poszlo nie tak")
if "SIEC_NAFTOWA" in [layer.name for layer in mapx.listLayers()]:
    sNaP = mapx.listLayers("SIEC_NAFTOWA")[0]
else:
    print("Brak warstwy SIEC_NAFTOWA lub cos poszlo nie tak")
if "SIEC_NAFTOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sNaL = mapx.listLayers("SIEC_NAFTOWA_1")[0]
else:
    print("Brak warstwy SIEC_NAFTOWA_1 lub cos poszlo nie tak")
if "SIEC_BENZYNOWA" in [layer.name for layer in mapx.listLayers()]:
    sBeP = mapx.listLayers("SIEC_BENZYNOWA")[0]
else:
    print("Brak warstwy SIEC_BENZYNOWA lub cos poszlo nie tak")
if "SIEC_BENZYNOWA_1" in [layer.name for layer in mapx.listLayers()]:
    sBeL = mapx.listLayers("SIEC_BENZYNOWA_1")[0] 
else:
    print("Brak warstwy SIEC_BENZYNOWA_1 lub cos poszlo nie tak")

# Przypisanie symboliki
    
try:
    if budIurzL.isFeatureLayer == True:
        symbudIurzL = budIurzL.symbology
        symbudIurzL.renderer.symbol.applySymbolFromGallery("Budowle i Urządzenia")
        budIurzL.symbology = symbudIurzL
    else:
        print("Brak symbolu budIurzL lub cos poszlo nie tak") 
except NameError:
    pass
try:
    if budL.isFeatureLayer == True:
        symbudL = budL.symbology
        symbudL.renderer.symbol.applySymbolFromGallery("Budynki")
        budL.symbology = symbudL
    else:
        print("Brak symbolu budL lub cos poszlo nie tak")  
except NameError:
    pass
try:
    if ewDzL.isFeatureLayer == True:
        symewDzL = ewDzL.symbology
        symewDzL.renderer.symbol.applySymbolFromGallery("Ewidencja Gruntów - Działki")
        ewDzL.symbology = symewDzL
    else:
        print("Brak symbolu ewDzL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGrL.isFeatureLayer == True:
        symewGrL = ewGrL.symbology
        symewGrL.renderer.symbol.applySymbolFromGallery("Ewidencja Gruntów - Graniczniki")
        ewGrL.symbology = symewGrL
    else:
        print("Brak symbolu ewGrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGoL.isFeatureLayer == True:
        symewGoL = ewGoL.symbology
        symewGoL.renderer.symbol.applySymbolFromGallery("Ewidencja Gruntów - Granica Obrębu")
        ewGoL.symbology = symewGoL
    else:
        print("Brak symbolu ewGoL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewUzL.isFeatureLayer == True:
        symewUzL = ewUzL.symbology
        symewUzL.renderer.symbol.applySymbolFromGallery("Ewidencja Gruntów - Użytki")
        ewUzL.symbology = symewUzL
    else:
        print("Brak symbolu ewUzL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if kItrL.isFeatureLayer == True:
        symkItrL = kItrL.symbology
        symkItrL.renderer.symbol.applySymbolFromGallery("Komunikacja i Transport")
        kItrL.symbology = symkItrL
    else:
        print("Brak symbolu kItrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oInL.isFeatureLayer == True:
        symoInL = oInL.symbology
        symoInL.renderer.symbol.applySymbolFromGallery("Obiekty Inne")
        oInL.symbology = symoInL
    else:
        print("Brak symbolu oInL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oOpL.isFeatureLayer == True:
        symoOpL = oOpL.symbology
        symoOpL.renderer.symbol.applySymbolFromGallery("Obszar Opracowania")
        oOpL.symbology = symoOpL
    else:
        print("Brak symbolu oOpL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if osL.isFeatureLayer == True:
        symosL = osL.symbology
        symosL.renderer.symbol.applySymbolFromGallery("Osnowa")
        osL.symbology = symosL
    else:
        print("Brak symbolu osL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if pTeL.isFeatureLayer == True:
        sympTeL = pTeL.symbology
        sympTeL.renderer.symbol.applySymbolFromGallery("Pokrycie Terenu")
        pTeL.symbology = sympTeL
    else:
        print("Brak symbolu pTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if rTeL.isFeatureLayer == True:
        symrTeL = rTeL.symbology
        symrTeL.renderer.symbol.applySymbolFromGallery("Rzezba Terenu")
        rTeL.symbology = symrTeL
    else:
        print("Brak symbolu rTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKrL.isFeatureLayer == True:
        symsKrL = sKrL.symbology
        symsKrL.renderer.symbol.applySymbolFromGallery("Siatka Krzyży")
        sKrL.symbology = symsKrL
    else:
        print("Brak symbolu sKrL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sCpL.isFeatureLayer == True:
        symsCpL = sCpL.symbology
        symsCpL.renderer.symbol.applySymbolFromGallery("Sieć Ciepłownicza")
        sCpL.symbology = symsCpL
    else:
        print("Brak symbolu sCpL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sElL.isFeatureLayer == True:
        symsElL = sElL.symbology
        symsElL.renderer.symbol.applySymbolFromGallery("Siec Elektroenergetyczna")
        sElL.symbology = symsElL
    else:
        print("Brak symbolu sElL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sGaL.isFeatureLayer == True:
        symsGaL = sGaL.symbology
        symsGaL.renderer.symbol.applySymbolFromGallery("Sieć Gazowa")
        sGaL.symbology = symsGaL
    else:
        print("Brak symbolu sGaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sInL.isFeatureLayer == True:
        symsInL = sInL.symbology
        symsInL.renderer.symbol.applySymbolFromGallery("Sieć Inna")
        sInL.symbology = symsInL
    else:
        print("Brak symbolu sInL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKaL.isFeatureLayer == True:
        symsKaL = sKaL.symbology
        symsKaL.renderer.symbol.applySymbolFromGallery("Sieć Kanalizacyjna")
        sKaL.symbology = symsKaL
    else:
        print("Brak symbolu sKaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNiL.isFeatureLayer == True:
        symsNiL = sNiL.symbology
        symsNiL.renderer.symbol.applySymbolFromGallery("Sieć Niezidentyfikowana")
        sNiL.symbology = symsNiL
    else:
        print("Brak symbolu sNiL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sTeL.isFeatureLayer == True:
        symsTeL = sTeL.symbology
        symsTeL.renderer.symbol.applySymbolFromGallery("Sieć Telekomunikacyjna")
        sTeL.symbology = symsTeL
    else:
        print("Brak symbolu sTeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sWoL.isFeatureLayer == True:
        symsWoL = sWoL.symbology
        symsWoL.renderer.symbol.applySymbolFromGallery("Sieć Wodociągowa")
        sWoL.symbology = symsWoL
    else:
        print("Brak symbolu sWoL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNaL.isFeatureLayer == True:
        symsNaL = sNaL.symbology
        symsNaL.renderer.symbol.applySymbolFromGallery("Sieć Naftowa")
        sNaL.symbology = symsNaL
    else:
        print("Brak symbolu sNaL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sBeL.isFeatureLayer == True:
        symsBeL = sBeL.symbology
        symsBeL.renderer.symbol.applySymbolFromGallery("Sieć Benzynowa")
        sBeL.symbology = symsBeL
    else:
        print("Brak symbolu sBeL lub cos poszlo nie tak")
except NameError:
    pass
try:
    if budIurzP.isFeatureLayer == True:
        symbudIurzP = budIurzP.symbology
        symbudIurzP.renderer.symbol.applySymbolFromGallery("Pikiety")
        budIurzP.symbology = symbudIurzP
        budIurzP.showLabels = True
    else:
        print("Brak symbolu budIurzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if budP.isFeatureLayer == True:
        symbudP = budP.symbology
        symbudP.renderer.symbol.applySymbolFromGallery("Pikiety")
        budP.symbology = symbudP
        budP.showLabels = True
    else:
        print("Brak symbolu budP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewDzP.isFeatureLayer == True:
        symewDzP = ewDzP.symbology
        symewDzP.renderer.symbol.applySymbolFromGallery("Pikiety")
        ewDzP.symbology = symewDzP
        ewDzP.showLabels = True
    else:
        print("Brak symbolu ewDzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGrP.isFeatureLayer == True:
        symewGrP = ewGrP.symbology
        symewGrP.renderer.symbol.applySymbolFromGallery("Pikiety")
        ewGrP.symbology = symewGrP
        ewGrP.showLabels = True
    else:
        print("Brak symbolu ewGrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewGoP.isFeatureLayer == True:
        symewGoP = ewGoP.symbology
        symewGoP.renderer.symbol.applySymbolFromGallery("Pikiety")
        ewGoP.symbology = symewGoP
        ewGoP.showLabels = True
    else:
        print("Brak symbolu ewGoP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if ewUzP.isFeatureLayer == True:
        symewUzP = ewUzP.symbology
        symewUzP.renderer.symbol.applySymbolFromGallery("Pikiety")
        ewUzP.symbology = symewUzP 
        ewUzP.showLabels = True
    else:
        print("Brak symbolu ewUzP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if kItrP.isFeatureLayer == True:
        symkItrP = kItrP.symbology
        symkItrP.renderer.symbol.applySymbolFromGallery("Pikiety")
        kItrP.symbology = symkItrP 
        kItrP.showLabels = True
    else:
        print("Brak symbolu kItrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oInP.isFeatureLayer == True:
        symoInP = oInP.symbology
        symoInP.renderer.symbol.applySymbolFromGallery("Pikiety")
        oInP.symbology = symoInP
        oInP.showLabels = True
    else:
        print("Brak symbolu oInP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if oOpP.isFeatureLayer == True:
        symoOpP = oOpP.symbology
        symoOpP.renderer.symbol.applySymbolFromGallery("Pikiety")
        oOpP.symbology = symoOpP
        oOpP.showLabels = True
    else:
        print("Brak symbolu oOpP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if osP.isFeatureLayer == True:
        symosP = osP.symbology
        symosP.renderer.symbol.applySymbolFromGallery("Pikiety")
        osP.symbology = symosP
        osP.showLabels = True
    else:
        print("Brak symbolu osP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if pTeP.isFeatureLayer == True:
        sympTeP = pTeP.symbology
        sympTeP.renderer.symbol.applySymbolFromGallery("Pikiety")
        pTeP.symbology = sympTeP
        pTeP.showLabels = True
    else:
        print("Brak symbolu pTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if rTeP.isFeatureLayer == True:
        symrTeP = rTeP.symbology
        symrTeP.renderer.symbol.applySymbolFromGallery("Pikiety")
        rTeP.symbology = symrTeP 
        rTeP.showLabels = True
    else:
        print("Brak symbolu rTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKrP.isFeatureLayer == True:
        symsKrP = sKrP.symbology
        symsKrP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sKrP.symbology = symsKrP
        sKrP.showLabels = True
    else:
        print("Brak symbolu sKrP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sCpP.isFeatureLayer == True:
        symsCpP = sCpP.symbology
        symsCpP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sCpP.symbology = symsCpP 
        sCpP.showLabels = True
    else:
        print("Brak symbolu sCpP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sElP.isFeatureLayer == True:
        symsElP = sElP.symbology
        symsElP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sElP.symbology = symsElP 
        sElP.showLabels = True
    else:
        print("Brak symbolu sElP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sGaP.isFeatureLayer == True:
        symsGaP = sGaP.symbology
        symsGaP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sGaP.symbology = symsGaP  
        sGaP.showLabels = True
    else:
        print("Brak symbolu sGaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sInP.isFeatureLayer == True:
        symsInP = sInP.symbology
        symsInP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sInP.symbology = symsInP  
        sInP.showLabels = True
    else:
        print("Brak symbolu sInP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sKaP.isFeatureLayer == True:
        symsKaP = sKaP.symbology
        symsKaP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sKaP.symbology = symsKaP
        sKaP.showLabels = True
    else:
        print("Brak symbolu sKaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNiP.isFeatureLayer == True:
        symsNiP = sNiP.symbology
        symsNiP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sNiP.symbology = symsNiP
        sNiP.showLabels = True
    else:
        print("Brak symbolu sNiP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sTeP.isFeatureLayer == True:
        symsTeP = sTeP.symbology
        symsTeP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sTeP.symbology = symsTeP
        sTeP.showLabels = True
    else:
        print("Brak symbolu sTeP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sWoP.isFeatureLayer == True:
        symsWoP = sWoP.symbology
        symsWoP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sWoP.symbology = symsWoP
        sWoP.showLabels = True
    else:
        print("Brak symbolu sWoP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sNaP.isFeatureLayer == True:
        symsNaP = sNaP.symbology
        symsNaP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sNaP.symbology = symsNaP
        sNaP.showLabels = True
    else:
        print("Brak symbolu sNaP lub cos poszlo nie tak")
except NameError:
    pass
try:
    if sBeP.isFeatureLayer == True:
        symsBeP = sBeP.symbology
        symsBeP.renderer.symbol.applySymbolFromGallery("Pikiety")
        sBeP.symbology = symsBeP
        sBeP.showLabels = True
    else:
        print("Brak symbolu sBeP lub cos poszlo nie tak")
except NameError:
    pass

print("Symbolika liniowa i punktowa podłączona")

# Przypisanie symboliki opisów

try:
    if sWoP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_WODOCIAGOWA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_WODOCIAGOWA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sTeP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_TELEKOMUNIKACYJNA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_TELEKOMUNIKACYJNA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sNiP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_NIEZIDENTYFIKOWANA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_NIEZIDENTYFIKOWANA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sKaP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_KANALIZACYJNA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_KANALIZACYJNA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sInP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_INNA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_INNA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sGaP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_GAZOWA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_GAZOWA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sElP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_ELEKTROENERGETYCZNA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_ELEKTROENERGETYCZNA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sCpP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_CIEPLOWNICZA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_CIEPLOWNICZA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sKrP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIATKA_KRZYZY", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIATKA_KRZYZY.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if rTeP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\RZEZBA_TERENU", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\RZEZBA_TERENU.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if osP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\OSNOWA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\OSNOWA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if kItrP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\KOMUNIKACJA_I_TRANSPORT", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\KOMUNIKACJA_I_TRANSPORT.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if ewUzP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\EWIDENCJA_GRUNTOW___UZYTKI", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\EWIDENCJA_GRUNTOW___UZYTKI.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if ewDzP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\EWIDENCJA_GRUNTOW___DZIALKI", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\EWIDENCJA_GRUNTOW___DZIALKI.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass 
try:
    if ewGoP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\EWIDENCJA_GRUNTOW___GRANICA_OBREBU", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\EWIDENCJA_GRUNTOW___GRANICA_OBREBU.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if ewGrP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\EWIDENCJA_GRUNTOW___GRANICZNIKI", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\EWIDENCJA_GRUNTOW___GRANICZNIKI.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if budP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\BUDYNKI", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\BUDYNKI.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if budIurzP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\BUDOWLE_I_URZADZENIA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\BUDOWLE_I_URZADZENIA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if pTeP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\POKRYCIE_TERENU", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\POKRYCIE_TERENU.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sNaP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_NAFTOWA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_NAFTOWA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if sBeP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\SIEC_BENZYNOWA", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\SIEC_BENZYNOWA.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass
try:
    if oInP.isFeatureLayer == True:
        arcpy.management.ApplySymbologyFromLayer(r"MAPA_ZASADNICZA\PUNKTY\OBIEKTY_INNE", r"\\192.168.1.41\Zespolowe\ZAP\GIS\MZ_ArcGIS\MZ_warstwy\POKRYCIE_TERENU.lyrx", None, "DEFAULT")
    else:
        pass
except arcpy.ExecuteError:
    pass
except NameError:
    pass

print("Symbolika opisów podłączona")

outputFileP = r"{0}\{1}_MZ_punkty.lpkx".format(folder, nr_planu)
outputFileL = r"{0}\{1}_MZ_linie.lpkx".format(folder, nr_planu)

punktyLyr = mapx.listLayers("PUNKTY")[0]
linieLyr = mapx.listLayers("LINIE")[0]

arcpy.PackageLayer_management([punktyLyr], outputFileP, "PRESERVE", 
                              "CONVERT_ARCSDE", "#", "ALL", "ALL", "ALL", 
                              "#", "Mapa zasadnicza podkład do planu", 
                              "brg, mapa zasadnicza")
arcpy.PackageLayer_management([linieLyr], outputFileL, "PRESERVE", 
                              "CONVERT_ARCSDE", "#", "ALL", "ALL", "ALL", 
                              "#", "Mapa zasadnicza podkład do planu", 
                              "brg, mapa zasadnicza")

print("Warstwy wyeksportowane")

print("Wszystko Super. Good job !")


