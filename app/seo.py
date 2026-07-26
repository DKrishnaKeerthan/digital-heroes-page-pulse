from bs4 import BeautifulSoup

def analyze_seo(soup: BeautifulSoup):
    title = soup.title.string.strip() if soup.title and soup.title.string else None

    meta = soup.find("meta", attrs={"name": "description"})
    meta_description = (
        meta.get("content").strip()
        if meta and meta.get("content")
        else None
    )

    h1_tags = soup.find_all("h1")

    images = soup.find_all("img")
    missing_alt = sum(
        1 for img in images
        if not img.get("alt") or not img.get("alt").strip()
    )

    return {
        "title": title,
        "has_title": title is not None,
        "meta_description": meta_description,
        "has_meta_description": meta_description is not None,
        "h1_count": len(h1_tags),
        "images_total": len(images),
        "images_missing_alt": missing_alt
    }