def sentence_chunk(text):
    return [s.strip() for s in text.split('.') if s.strip()]
