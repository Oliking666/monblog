from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
import os


def validate_file_size(value, max_size=2):
    """Valide la taille du fichier (en MB)"""
    filesize = value.size
    if filesize > max_size * 1024 * 1024:
        raise ValidationError(
            mark_safe(f"La taille maximale du fichier est de <strong>{max_size}MB</strong>")
        )

def validate_image_extension(value):
    """Valide les extensions d'image autorisées"""
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError(
            mark_safe("Format de fichier non supporté. Extensions autorisées: "
                     "<strong>JPG, JPEG, PNG, GIF, WEBP</strong>")
        )

def validate_file_extension(value, allowed_extensions):
    """Valide des extensions de fichier personnalisées"""
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in allowed_extensions:
        raise ValidationError(
            mark_safe(f"Extension non autorisée. Extensions valides: "
                     f"<strong>{', '.join(allowed_extensions)}</strong>")
        )


# validators.py
from PIL import Image
import io

def validate_image_content(value):
    """Vérifie que le fichier est bien une image valide"""
    try:
        img = Image.open(io.BytesIO(value.read()))
        img.verify()  # Vérifie que l’image n’est pas corrompue
        value.seek(0)  # Réinitialise le pointeur du fichier
    except Exception as e:
        raise ValidationError("Le fichier n’est pas une image valide")

# validators.py
import magic

def validate_pdf(value):
    """Valide que le fichier est bien un PDF"""
    file_type = magic.from_buffer(value.read(1024), mime=True)
    value.seek(0)
    if file_type != 'application/pdf':
        raise ValidationError("Seuls les fichiers PDF sont autorisés")
