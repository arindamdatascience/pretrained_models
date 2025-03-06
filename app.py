from fastapi import FastAPI, File, UploadFile
import soundfile as sf
from inference import VoiceCloner
from config import MODEL_PATHS

app = FastAPI()
cloner = VoiceCloner(MODEL_PATHS)

@app.post("/clone")
async def clone_voice(language: str, text: str, voice_sample: UploadFile = File(...)):
    """Clone voice with the specified language model."""
    if language not in MODEL_PATHS:
        return {"error": "Unsupported language"}

    # Read and process the voice sample
    audio, samplerate = sf.read(voice_sample.file)
    
    # Clone voice
    output_audio = cloner.clone_voice(language, text, audio)

    return {"message": "Voice cloned successfully!", "audio": output_audio}

# Run with: uvicorn app:app --host 0.0.0.0 --port 8000
