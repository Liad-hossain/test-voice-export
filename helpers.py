import os
import mailbox
import datetime
from email.utils import parsedate_to_datetime

TEMP_DIR = "./temp"
EXTRACT_DIR = "./temp/extracted"


def get_mbox_files():
    mbox_files = []
    for root, _, files in os.walk(EXTRACT_DIR):
        for file in files:
            if file.endswith('.mbox'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, EXTRACT_DIR)
                mbox_files.append(rel_path)
    return mbox_files


def process_mbox_file(mbox_path):
    audio_recordings = []
    full_mbox_path = os.path.join(EXTRACT_DIR, mbox_path)

    try:
        mbox = mailbox.mbox(full_mbox_path)
        messages = []

        for message in mbox:
            messages.append(message)

        print(f"Found {len(messages)} messages in MBOX file")

        for msg in messages:
            subject = msg.get('Subject', '')
            if 'OUTGOING_CALL' in subject or 'INCOMING_CALL' in subject or 'recording' in subject.lower():
                from_number = msg.get('From', '').strip('+')
                to_number = msg.get('To', '').strip('+')
                date_str = msg.get('Date', '')

                is_outgoing = 'OUTGOING_CALL' in subject
                phone_number = to_number if is_outgoing else from_number

                try:
                    parsed_date = parsedate_to_datetime(date_str)
                    timestamp = parsed_date.strftime('%Y%m%d_%H%M%S')
                except Exception as e:
                    print(f"Failed to parse date '{date_str}': {e}")
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == 'application/octet-stream':
                            filename = part.get_filename()
                            if filename and ('recording' in filename.lower() or filename.endswith(('.mp3', '.wav'))):
                                payload = part.get_payload(decode=True)
                                
                                if payload:
                                    audio_filename = f"call_{phone_number}_{timestamp}.mp3"
                                    audio_path = os.path.join(EXTRACT_DIR, audio_filename)

                                    try:
                                        with open(audio_path, 'wb') as audio_file:
                                            audio_file.write(payload)

                                        audio_recordings.append(audio_filename)
                                        print(f"Extracted audio recording: {audio_filename}")

                                    except Exception as e:
                                        print(f"Failed to save audio file {audio_filename}: {e}")

    except Exception as e:
        print(f"Failed to parse MBOX file {mbox_path}: {e}")

    return audio_recordings