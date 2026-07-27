def __init__(self):
    load_dotenv()

    url = os.getenv("SURREAL_URL")

    print(f"Surreal URL: {url}")

    self.client = AsyncSurreal(url)