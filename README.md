# test-mr: Cardiac MRI T1 Mapping Analysis Tool

## Overview

`test-mr` is a Python-based project designed to support the analysis of cardiac Magnetic Resonance (MR) T1 mapping images. The primary goal is to provide a workflow for importing images, segmenting cardiac structures, calculating Extracellular Volume (ECV), and visualizing the results.

## Features (Current and Planned)

*   **DICOM Image Importing**: Supports importing MR T1 mapping images in DICOM format.
*   **Cardiac Segmentation**: Aims to automatically delineate the endocardium and epicardium. (*Currently a placeholder*)
*   **ECV Calculation**: Aims to automatically analyze T1 values to calculate ECV. (*Currently a placeholder*)
*   **Bullseye Plot Visualization**: Plans to display ECV results using a standard AHA 17-segment bullseye plot. (*Currently a placeholder*)
*   Developed in Python.

## Project Structure

The project is organized into the following main directories:

*   `data/`: Intended for storing sample DICOM images and other data files. (Contains a `.gitkeep` file)
*   `src/`: Contains the core Python source code for the application.
    *   `__init__.py`: Marks the `src` directory as a Python package.
    *   `image_importer.py`: Module for importing DICOM images.
    *   `segmentation.py`: Module for heart segmentation (placeholder).
    *   `ecv.py`: Module for ECV calculation (placeholder).
    *   `visualization.py`: Module for results visualization (placeholder).
*   `tests/`: Contains unit tests for the modules in `src/`.
    *   `__init__.py`: Marks the `tests` directory as a Python package.
    *   `test_image_importer.py`: Tests for `image_importer.py`.
    *   `test_segmentation.py`: Tests for `segmentation.py`.
    *   `test_ecv.py`: Tests for `ecv.py`.
    *   `test_visualization.py`: Tests for `visualization.py`.

## Modules

*   **`src/image_importer.py`**:
    *   Handles the loading of DICOM files using the `pydicom` library.
    *   Provides the function `import_dicom_image(file_path)` which reads a DICOM file and returns a `pydicom.dataset.FileDataset` object.
*   **`src/segmentation.py`**:
    *   Intended for segmenting the heart's endocardial and epicardial contours from DICOM data.
    *   The `segment_heart(dicom_data)` function is currently a **placeholder** and returns empty NumPy arrays.
*   **`src/ecv.py`**:
    *   Designed to calculate Extracellular Volume (ECV) maps and mean ECV values from pre- and post-contrast T1 maps and contours.
    *   The `calculate_ecv(...)` function is currently a **placeholder** and returns a dummy ECV map and a fixed mean ECV value.
*   **`src/visualization.py`**:
    *   Will be used to display results, primarily ECV data as a bullseye plot.
    *   The `display_bullseye_plot(ecv_map)` function is currently a **placeholder** and prints a message to the console.

## Getting Started & Current Status

**Important**: The core image processing and analysis functionalities (segmentation, ECV calculation, and bullseye plot visualization) are currently **placeholders**. They demonstrate the intended modular structure but do not perform actual analysis.

### Conceptual Usage

```python
from src.image_importer import import_dicom_image
from src.segmentation import segment_heart
from src.ecv import calculate_ecv
from src.visualization import display_bullseye_plot
import numpy as np # For example hematocrit and dummy T1 maps

# 1. Import DICOM images (conceptual - assumes you have pre/post contrast images)
try:
    # These would be paths to your actual DICOM files
    dicom_image_pre_contrast = import_dicom_image("path/to/your/pre_contrast_image.dcm")
    dicom_image_post_contrast = import_dicom_image("path/to/your/post_contrast_image.dcm")
    print("DICOM images imported (conceptually).")
except FileNotFoundError:
    print("Sample DICOM files not found. Please provide valid paths.")
    exit()
except Exception as e:
    print(f"An error occurred during DICOM import: {e}")
    exit()

# For the placeholder functions, we need to simulate T1 maps and contours
# In a real workflow, T1 maps might be part of the DICOM data or derived from it.
# Contours would come from the segmentation step.

# Simulate T1 maps (e.g., pixel_array from DICOM if they are T1 maps)
# Or, if they are multi-frame DICOMs, extract relevant T1-weighted images.
# Here, we create dummy numpy arrays for placeholder function calls.
# Ensure these are available if dicom_image_pre_contrast and dicom_image_post_contrast are valid
if dicom_image_pre_contrast and dicom_image_post_contrast:
    # This is a simplification. Real T1 maps are derived, not just pixel arrays of any DICOM.
    # For now, let's assume dummy arrays if pixel_array is not what we need.
    t1_map_pre = np.random.rand(256, 256) # Example shape
    t1_map_post = np.random.rand(256, 256) # Example shape
    print(f"Using dummy T1 maps of shape {t1_map_pre.shape}")

    # 2. Segment heart (currently a placeholder)
    # Assuming dicom_image_pre_contrast is used for segmentation context
    endo_contour, epi_contour = segment_heart(dicom_image_pre_contrast)
    print(f"Segmentation placeholder called. Endo points: {len(endo_contour)}, Epi points: {len(epi_contour)}")

    # 3. Calculate ECV (currently a placeholder)
    hematocrit = 0.45 # Example hematocrit value
    ecv_map_result, mean_ecv_result = calculate_ecv(
        t1_map_pre, t1_map_post, endo_contour, epi_contour, hematocrit
    )
    print(f"ECV calculation placeholder called. Mean ECV: {mean_ecv_result}")

    # 4. Display results (currently a placeholder)
    display_bullseye_plot(ecv_map_result)
else:
    print("Skipping further processing due to missing DICOM data.")

```

## Dependencies

The project relies on the following Python libraries:

*   `pydicom`: For reading and manipulating DICOM files.
*   `numpy`: For numerical operations, especially array manipulation for image data and contours.
*   `matplotlib`: For generating visualizations, including the planned bullseye plot.

You can install these dependencies using pip:
```bash
pip install pydicom numpy matplotlib
```

## Running Tests

The project includes a suite of unit tests in the `tests/` directory using Python's `unittest` framework. To run the tests, navigate to the project's root directory and run:

```bash
python -m unittest discover -s tests
```
This command will discover and execute all tests within the `tests` directory. Current tests are placeholders and primarily verify that the placeholder functions can be called.Okay, I have overwritten the `README.md` file with the new content. It now includes:
- An overview and features (incorporating "系统支持").
- Project structure.
- Descriptions of each module, noting placeholder status.
- A "Getting Started & Current Status" section with a conceptual usage example and a disclaimer about placeholder functionalities.
- A "Dependencies" section with installation instructions.
- A "Running Tests" section with a command to run the existing placeholder tests.

I believe this fulfills all the requirements of the subtask.
