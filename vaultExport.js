const { GoogleAuth } = require('google-auth-library');
const axios = require('axios');
const fs = require('fs');

async function run() {
  const key = JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT_JSON);

  const auth = new GoogleAuth({
    credentials: key,
    scopes: [
      'https://www.googleapis.com/auth/ediscovery',
      'https://www.googleapis.com/auth/devstorage.read_only'
    ],
    clientOptions: {
      subject: process.env.WORKSPACE_ADMIN_EMAIL
    }
  });

  const client = await auth.getClient();
  const token = await client.getAccessToken();

  const matterId = process.env.VAULT_MATTER_ID;

  const res = await axios.post(
    `https://vault.googleapis.com/v1/matters/${matterId}/exports`,
    {
      name: `voice-export-${new Date().toISOString()}`,
      query: {
        corpus: 'VOICE',
        dataScope: 'ALL_DATA',
        accountInfo: {
          emails: [process.env.VOICE_USER_EMAIL]
        }
      },
      exportOptions: {
        voiceOptions: { exportFormat: 'MBOX' }
      }
    },
    {
      headers: {
        Authorization: `Bearer ${token.token}`
      }
    }
  );

  console.log('Export created:', res.data.id);
}

run().catch(err => {
  console.error(err.response?.data || err.message);
  process.exit(1);
});
