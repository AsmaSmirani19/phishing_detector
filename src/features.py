import re

def url_length(url):
    return len(url)

def count_dots(url):
    return url.count('.')

def count_hyphens(url):
    return url.count('-')

def count_digits(url):
    """Compte combien il y a de chiffres dans l'URL."""
    return sum(c.isdigit() for c in url)

def count_at_symbols(url):
    return url.count('@')

def has_ip_address(url):
    """Détecte si l'URL contient une adresse IP (ex: 192.168.1.1)."""
    match = re.search(r'(\d{1,3}\.){3}\d{1,3}', url)
    return 1 if match else 0

def has_https(url):
    """Retourne 1 si l'URL est en HTTPS, 0 sinon."""
    return 1 if url.startswith('https://') else 0

def count_subdomains(url):
    """Compte le nombre de sous-domaines (ex: a.b.google.com = 2 sous-domaines)."""
    # On enlève le http:// ou https://
    clean_url = url.replace('http://', '').replace('https://', '')
    # On coupe au premier slash pour ne garder que le nom de domaine
    domain = clean_url.split('/')[0]
    # On compte les points et on enlève 1 (pour le .com)
    return max(0, domain.count('.') - 1)

def has_suspicious_words(url):
    """Vérifie la présence de mots typiques du phishing."""
    suspicious = ['login', 'verify', 'secure', 'update', 'account', 'signin', 'banking', 'support']
    url_lower = url.lower()
    for word in suspicious:
        if word in url_lower:
            return 1
    return 0