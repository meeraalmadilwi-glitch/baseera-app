import os
import zipfile

def zipdir(path, ziph):
    # Directories and files to exclude
    exclude_dirs = {'.git', '__pycache__', 'venv', 'env', 'node_modules', '.idea', '.vscode'}
    exclude_exts = {'.sqlite3', '.pyc', '.log'}
    
    for root, dirs, files in os.walk(path):
        # Modify dirs in-place to skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if any(file.endswith(ext) for ext in exclude_exts):
                continue
            
            # Skip the zip file itself and the script
            if file in ['baseera_production.zip', 'zip_project.py', 'fix_api_views.py', 'fix_security.py', 'fix_views.py', 'fix_urls_final.py', 'check_urls.py', 'fix_api_urls.py']:
                continue
                
            file_path = os.path.join(root, file)
            # Add file to zip archive, using relative path
            ziph.write(file_path, os.path.relpath(file_path, path))

if __name__ == '__main__':
    zip_filename = 'baseera_production.zip'
    print(f"Creating {zip_filename}...")
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir('.', zipf)
    print("Done!")
