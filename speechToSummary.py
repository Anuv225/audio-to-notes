import os

import openai

openai.api_key = ""


def createTranscript(audio_file):
    audio_file = open(audio_file,"rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']

def createSummary(transcript):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content":"You are an expert on taking notes and good at creating summaries."},
            {"role": "user", "content": f"Summarize the following transcript into key bullet points:\n{transcript}"}
        ]
    )

    response = response['choices'][0]['message']['content'].split('-')
    return (response[1:])

    




