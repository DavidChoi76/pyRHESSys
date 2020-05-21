import itertools
import os
import shutil
from urllib.request import urlretrieve
import subprocess
from hs_restclient import HydroShare


def get_hs_resource(resource_id, file_path):
    hs = HydroShare()
    hs.getResource(resource_id, destination=file_path, unzip=True)

    # unpack the simulation archive and remove unncessary files
    hs_resource_dir = os.path.join(file_path, resource_id, resource_id, 'data/contents/')
    hs_resource = os.listdir(hs_resource_dir)
    shutil.unpack_archive(hs_resource_dir+hs_resource[0], extract_dir=file_path)
    cmd = "rm -rf " + os.path.join(file_path, resource_id)
    subprocess.run(cmd, shell=True)

def replace_string(file, current_string, new_string):
    if not os.path.isfile(file):
        print ("Error on replace_string, not a regular file: "+file)
        sys.exit(1)

    f1=open(file,'r').read()
    f2=open(file,'w')
    m=f1.replace(current_string,new_string)
    f2.write(m)

def complie(file_path, version_option="rhessys5.20.0.develop"):
    if version_option:
        complie_RHESSys = 'cd ' + file_path +'/RHESSysEastCoast;make'
        subprocess.run(complie_RHESSys, shell=True)
        exe_RHESSys = 'cd ' + file_path +'/RHESSysEastCoast;chmod +rwx ' + version_option
        subprocess.run(exe_RHESSys, shell=True)
        execution_file = file_path + '/RHESSysEastCoast/' + version_option

    else:
        print("You have to set the exact RHESSys version")

    return execution_file

def product_dict(**kwargs):
    """
    Take a set of dictionary arguments and generate a new set of
    dictionaries that have all combinations of values for each key.
    """
    keys, vals = kwargs.keys(), kwargs.values()
    for instance in itertools.product(*vals):
        yield dict(zip(keys, instance))

def netcdf_output()


class ChainDict(dict):
    """
    A dictionary which instead of overwriting on existing keys,
    will instead store the values in a list.
    """
    def __setitem__(self, key, val):
        newval = [val]
        if key in list(self.keys()):
            oldval = self.__getitem__(key)
            newval = list(set(oldval + newval))
        dict.__setitem__(self, key, newval)
