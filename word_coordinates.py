
def extract_words_coordinates(o: Any, depth=0) -> List[Dict[str, Any]]:
    """
    Extract location and text of LTItem and all its descendants into a list.
    """
    results = []

    if hasattr(o, 'bbox') and hasattr(o, 'get_text'): 
        bbox = o.bbox 
        results.append({
            "type": o.__class__.__name__,
            "x1": bbox[0],  # Extract x1
            "y1": bbox[1],  # Extract y1
            "x2": bbox[2],  # Extract x2 (optional)
            "y2": bbox[3],  # Extract y2 (optional)
            "text": o.get_text().strip()
        })

    if isinstance(o, Iterable):
        for i in o:
            results.extend(extract_words_coordinates(i, depth=depth + 1))
    return results


def get_indented_name(o: Any, depth: int) -> str:
    """Indented name of LTItem"""
    return '  ' * depth + o.__class__.__name__


def get_optional_bbox(o: Any) -> str:
    """Bounding box of LTItem if available, otherwise empty string"""
    if hasattr(o, 'bbox'):
        return ''.join(f'{i:<4.0f}' for i in o.bbox)
    return ''


def get_optional_text(o: Any) -> str:
    """Text of LTItem if available, otherwise empty string"""
    if hasattr(o, 'get_text'):
        return o.get_text().strip()
    return ''
