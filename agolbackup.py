from arcgis.gis import GIS
from pathlib import Path

# Add your own credentials here
org_url = 'https://www.arcgis.com'
username = ''
password = ''


# Change this when necessary
download_location = Path('C:/temp/agolbackup')
export_format = 'File Geodatabase' # or Shapefile, CSV

gis = GIS(org_url, username, password)
search_result = gis.content.search(query="", item_type="Feature Service", max_items=500)
for item in search_result:
    try:
        backup = item.export(title=item.title + ' Backup', export_format=export_format, wait=True)
        print("Finished backing up " + item.title + " to " + backup.title + "(ID: " + backup.id + ")")
    except:
        print('Error backing up ' + item.title)
        continue
    print("Downloading " + backup.title)
    downloaded = backup.download(download_location)
    if downloaded == None:
        print("Downloading of " + backup.title + " failed.")
    else:
        print("Finished downloading to " + downloaded)
        print("Deleting backup item " + backup.title)
        try:
            backup.delete()
        except:
            print("Cannot delete " + backup.title)