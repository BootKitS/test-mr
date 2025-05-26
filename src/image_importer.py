import pydicom
from pydicom.errors import InvalidDicomError

def import_dicom_image(file_path: str):
    """
    Reads a DICOM file and returns the DICOM data object.

    Args:
        file_path (str): The path to the DICOM file.

    Returns:
        pydicom.dataset.FileDataset: The DICOM data object if successful,
                                     None otherwise.
    Raises:
        FileNotFoundError: If the DICOM file is not found at the given path.
        InvalidDicomError: If the file is not a valid DICOM file.
        Exception: For any other unexpected errors during processing.
    """
    try:
        dicom_data = pydicom.dcmread(file_path, force=True)
        # The 'force=True' parameter allows reading files that might be missing the
        # DICOM file meta information header or have other minor inconsistencies.
        # You might want to remove or adjust it based on how strict the validation needs to be.
        return dicom_data
    except FileNotFoundError:
        # Re-raise the FileNotFoundError to be handled by the caller
        raise
    except InvalidDicomError:
        # Re-raise the InvalidDicomError for specific handling by the caller
        raise
    except Exception as e:
        # Raise any other unexpected exceptions
        print(f"An unexpected error occurred while reading {file_path}: {e}")
        raise
