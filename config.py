import os

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - fallback for environments without python-dotenv
    def load_dotenv():
        return False

load_dotenv()

# Email que vai receber as vagas
EMAIL_DESTINO = "ricardottsilva@gmail.com"

# Configuração SMTP
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))

# Ficheiro onde guardamos as vagas
JSON_FILE = "vagas.json"

# Pesquisas que queremos fazer
PESQUISAS = [
    "python",
    "python junior",
    "developer junior",
    "developer estágio",
    "developer estagio",
    "programador junior",
    "programador júnior",
    "estágio python",
    "estagio python"
]
