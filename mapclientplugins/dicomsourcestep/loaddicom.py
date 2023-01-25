
import os
from glob import glob
from mapclientplugins.dicomsourcestep import pydicom_series as dicomSeries
try:
    from gias3.image_analysis import image_tools
except ImportError:
    HAS_GIAS = False
else:
    HAS_GIAS = True

def _get_files(path, pattern='*'):
    
    files = sorted(glob(os.path.join(path, pattern)))
    if len(files)==0:
        raise IOError('No files found')
    else:
        return files

class DicomLoader(object):

    def __init__(self, **kwargs):
        self.scan = None
        self.file_dir = None
        self.file_pattern = None
        self.files = None

    def execute(self, filedir, filepattern):
        self.file_dir = filedir
        self.file_pattern = filepattern
        self._load()

    def _load(self):
        self.files = _get_files(self.file_dir, self.file_pattern)
        self.stack = dicomSeries.read_files(self.files, showProgress=True, readPixelData=True)[0]
        if HAS_GIAS:
            self._make_scan()

    def _make_scan(self):
        self.scan = image_tools.Scan(self.stack.description)
        I = self.stack.get_pixel_array().transpose([2,1,0])
        voxel_spacing = self.stack.sampling[::-1]
        voxel_origin = [float(i) for i in self.stack.info.ImagePositionPatient]
        self.scan.setImageArray(
            I,
            voxel_spacing, 
            voxel_origin,
            )

    def get_stack(self):
        return self.stack

    def get_image_array(self):
        return self.stack.get_pixel_array()

    def get_scan(self):
        return self.scan