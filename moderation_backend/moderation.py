from google.cloud import vision

def moderate_image(image_bytes):
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=image_bytes)

    response = client.safe_search_detection(image=image)

    if response.error.message:
        raise RuntimeError(response.error.message)

    annotation = response.safe_search_annotation

    blocked_categories = {
        "adult": vision.Likelihood.LIKELY,
        "racy": vision.Likelihood.VERY_LIKELY,
        "violence": vision.Likelihood.VERY_LIKELY
    }

    results = {
        "adult": annotation.adult,
        "racy": annotation.racy,
        "violence": annotation.violence
    }

    for category, minimum_likelihood in blocked_categories.items():
        if results[category] >= minimum_likelihood:
            return {
                "approved": False,
                "reason": f"Image flagged for {category} content"
            }

    return {
        "approved": True,
        "reason": None
    }