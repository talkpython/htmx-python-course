import json
from pathlib import Path
from typing import List, Dict, Optional

from models.category_model import Category
from models.video_model import Video

__categories: Dict['str', Category] = {}
__all_videos_list: List[Video] = []


def load_data():
    global __all_videos_list, __categories

    __categories = {}
    __all_videos_list = []

    file = Path(__file__).parent.parent / 'db' / 'videos.json'
    with open(file, 'r') as fin:
        data = json.load(fin)

    categories = [
        Category(**category)
        for category in data
    ]

    for c in categories:
        __categories[c.category.lower().strip()] = c
        for v in c.videos:
            v.category = c.category

    rebuild_flat_file_list()


def rebuild_flat_file_list():
    global __all_videos_list

    flat_set = {
        v.id: v
        for cat_name, cat in __categories.items()
        for v in cat.videos
    }
    # pprint(flat_set)
    __all_videos_list = list(flat_set.values())
    __all_videos_list.sort(key=lambda vid: vid.views, reverse=True)


def category_by_name(category: str) -> Optional[Category]:
    if not category or not category.strip():
        return None

    category = category.strip().lower()
    cat = __categories.get(category)
    if not cat:
        return None

    return cat


def all_videos(page: int = 1, page_size: Optional[int] = None) -> List[Video]:
    videos = __all_videos_list
    if page_size:
        start = page_size * (page - 1)
        end = start + page_size
        videos = videos[start: end]

    return videos


def all_categories() -> List[Category]:
    categories = list(__categories.values())
    categories.sort(key=lambda c: c.category.lower().strip())

    return categories


def video_by_id(video_id: str) -> Optional[Video]:
    for video in all_videos():
        if video.id == video_id:
            return video

    return None


def search_videos(search_text: str) -> List[Video]:
    results: List[Video] = []

    if not search_text or not search_text.strip():
        return results

    search_text = search_text.lower().strip()

    for v in all_videos():
        text = f"{v.id} {v.title} {v.author}".lower()
        if search_text in text:
            results.append(v)

    return results


def add_video(cat_name: str, youtube_id: str, title: str, author: str, view_count: int):
    global __all_videos_list

    if video_by_id(youtube_id):
        return None

    cat = category_by_name(cat_name)
    if not cat:
        return None

    url = f'https://www.youtube.com/watch?v={youtube_id}'
    v = Video(id=youtube_id, title=title, url=url, author=author, views=view_count, category=cat.category)
    cat.videos.append(v)

    rebuild_flat_file_list()

    return v


def video_count() -> int:
    return len(__all_videos_list)


# Start off with some data.
load_data()
