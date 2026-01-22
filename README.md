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
2. Create a new export from the last export time which is stored inside last_export_time.txt file
3. Downloads the ZIP file from Google Cloud Storage using the information from the response of created export
4. Extracts the ZIP file
5. Process the mbox file and extract all call recordings
6. Checks the deduplication from google spreadsheet using message_id
7. Uploads all `.wav` and `.mp3` files to Google Drive with renamed filenames
8. Store the message_id in google spreadsheet for the new uploaded recording

## File Structure

- `vaultExport.py` - Main script
- `utils.py` - For the required utility functions
- `helpers.py` - Helper functions to get all the mbox files inside the directory and process them to extract recordings.
- `requirements.txt` - Python dependencies
- `temp/` - Temporary directory for downloads and extraction (auto-created)

## Environment Variables

- `GOOGLE_SERVICE_ACCOUNT_JSON` - Service account credentials as JSON string
- `WORKSPACE_ADMIN_EMAIL` - Workspace admin email for domain-wide delegation
- `VAULT_MATTER_ID` - Google Vault matter ID
- `DRIVE_FOLDER_ID` - Google Drive folder ID where files will be uploaded
- `GOOGLE_SPREADSHEET_ID` - Google Spreadsheet ID where all the deduplication is handled by storing the informations
- `GOOGLE_SHEET_TAB_NAME` -  Google Sheet tab name where the recordings informations are stored
