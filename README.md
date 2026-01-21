# Vault Voice Export to Google Drive (Python)

This Python script downloads voice call recordings from Google Vault exports and uploads them to Google Drive.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set environment variables:

   ```bash
   export GOOGLE_SERVICE_ACCOUNT_JSON='{"type": "service_account", ...}'
   export WORKSPACE_ADMIN_EMAIL="admin@yourworkspace.com"
   export VAULT_MATTER_ID="your-vault-matter-id"
   export DRIVE_FOLDER_ID="your-drive-folder-id"
   ```

## Usage

```bash
python vaultExport.py
```

## What it does

1. Authenticates with Google services using service account credentials
2. Finds the latest completed Vault export
3. Downloads the ZIP file from Google Cloud Storage
4. Extracts the ZIP file
5. Uploads all `.wav` and `.mp3` files to Google Drive with renamed filenames

## File Structure

- `vaultExport.py` - Main script
- `requirements.txt` - Python dependencies
- `temp/` - Temporary directory for downloads and extraction (auto-created)

## Environment Variables

- `GOOGLE_SERVICE_ACCOUNT_JSON` - Service account credentials as JSON string
- `WORKSPACE_ADMIN_EMAIL` - Workspace admin email for domain-wide delegation
- `VAULT_MATTER_ID` - Google Vault matter ID
- `DRIVE_FOLDER_ID` - Google Drive folder ID where files will be uploaded
