import zipfile


def unzip():
    zip_ref = zipfile.ZipFile(
        "C:/Users/kfatyga/PycharmProjects/database_bullshit/full_traffic-2019_02_22__11_37_44.zip", "r")
    zip_ref.extractall("C:/Users/kfatyga/PycharmProjects/database_bullshit/extracted/")
    zip_ref.close()

# unzip()