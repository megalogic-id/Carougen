import os

import openai

openai.api_key = os.environ.get("OPENAI_API_KEY", 8080)


def generate(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt="""
        Buatkan sebuah materi untuk konten Instagram yang singkat, padat, dan jelas tentang {}
        dalam format HTML dalam bentuk list.
        Untuk setiap sub-judul dan list ditebalkan menggunakan bold,
        setiap sub-judul diberikan baris baru menggunakan <br> dia memanjang ke bawah.
        Berikan juga caption di akhir dengan 20 hashtags
        """.format(prompt),
        temperature=0.7,
        max_tokens=4000,
        n=1,
        stop=None,
        timeout=15
    )
    return response.choices[0].text.strip()
