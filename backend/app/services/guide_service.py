from typing import Dict, Optional
from app.services import guide_data
from app.schemas.guide import Guide


# For Phase 1 we just keep an in-memory dict.
# Later this becomes DB-backed.
_guides_by_slug: Dict[str, Guide] = {
    g.slug: g for g in guide_data.GUIDES
}


def get_guide_by_slug(slug: str) -> Optional[Guide]:
    return _guides_by_slug.get(slug)
