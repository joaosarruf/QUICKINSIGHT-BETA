const { AssemblyAI } = require('assemblyai');
const fs = require('fs');

const client = new AssemblyAI({
  apiKey: "66a8c7176b2c4dbc8e1ec4fd7931df63"
});

// Caminho do arquivo local
const filePath = '/root/QuickInsight/backend/Routes/audios/audio.mp3';

// Lê o conteúdo do arquivo
const audioContent = fs.readFileSync(filePath);

const config = {
  audio: audioContent, // Use 'audio' em vez de 'audio_url'
};

const run = async () => {
    const transcript = await client.transcripts.create(config);
    console.log(transcript.text);
  };

run();

