import os
import subprocess

def build_extension(base_dir, ext_name):
    # Construct paths dynamically
    source_dir = os.path.join(base_dir, "__assets__", "extensions", ext_name)
    output_dir = os.path.join(source_dir, "web-ext-artifacts")
    
    # Normalize paths for web-ext command line
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
    extensions = ["audio_ff_unsigned", "battery_ff_unsigned", "canvas_ff_unsigned", "canvas_getImageData_ff_unsigned",
                    "canvas_toBlob_ff_unsigned", "canvas_toDataURL_ff_unsigned", "clientRects_ff_unsigned", "font_ff_unsigned",
                    "font_offsetHeight_ff_unsigned", "font_offsetWidth_ff_unsigned", "navigator_ff_unsigned",
                    "screen_availHeight_ff_unsigned", "screen_availWidth_ff_unsigned", "screen_colorDepth_ff_unsigned", 
                    "screen_devicePixelRatio_ff_unsigned", "screen_ff_unsigned", "screen_height_ff_unsigned", "screen_width_ff_unsigned",
                    "timezone_ff_unsigned", "webgl_buffer_ff_unsigned", "webgl_ff_unsigned", "webgl_parameter_ff_unsigned",
                    "webRTC_ff_unsigned"]
    
    # Run the builder for all extensions in the list
    for ext in extensions:
        build_extension(base_dir, ext)