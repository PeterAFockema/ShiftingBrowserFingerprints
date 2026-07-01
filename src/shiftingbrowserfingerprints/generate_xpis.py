import os
import subprocess

def build_extension(base_dir, ext_name):
    # Construct paths dynamically
    source_dir = os.path.join(base_dir, "__assets__", "extensions", ext_name)
    output_dir = os.path.join(source_dir, "web-ext-artifacts")
    
    # Normalise paths for web-ext command line
    clean_source_dir = source_dir.replace("\\", "/")
    
    print(f"\nBuilding extension: {ext_name}")
    print(f"Source directory is: {clean_source_dir}")

    # Define the command arguments
    command = [
        "web-ext", 
        "build", 
        "--source-dir", clean_source_dir, 
        "--artifacts-dir", output_dir, 
        "--overwrite-dest", 
        f"--filename={ext_name}.xpi"
    ]

    try:
        # Run the command (shell=True is required on Windows if web-ext is a cmd/bat wrapper)
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=True)
        print(f"Build successful for {ext_name}!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Build failed for {ext_name}!")
        print(e.stderr)


def build_all_unsigned_xpi_extensions():
    # Get base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # List of your extension folder names
    extensions = ["aud_ff", "batt_ff", "canv_ff", "canv_getImaDat_ff",
                    "canv_toBl_ff", "canv_toDatURL_ff", "clientRects_ff", "font_ff",
                    "font_offHei_ff", "font_offWid_ff", "nav_ff",
                    "scre_avaHei_ff", "scre_avaWid_ff", "scre_colDep_ff", 
                    "scre_devPixRat_ff", "scre_ff", "scre_hei_ff", "scre_wid_ff",
                    "timez_ff", "webgl_buf_ff", "webgl_ff", "webgl_param_ff",
                    "webRTC_ff"]
    
    # Run the builder for all extensions in the list
    for ext in extensions:
        build_extension(base_dir, ext)