import httpx
from loguru import logger
from pydantic import BaseModel


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


def fetch_resource(resource_id: int, timeout: float = 5.0) -> Post | None:
    url = f"https://jsonplaceholder.typicode.com/posts/{resource_id}"

    try:
        response = httpx.get(url, timeout=timeout)

        if response.status_code == 200:
            logger.info("Ресурс {} успешно получен", resource_id)
            return Post.model_validate(response.json())

        if response.status_code == 404:
            logger.error("Ресурс {} не найден", resource_id)
            return None

        response.raise_for_status()

    except (httpx.TimeoutException, httpx.ConnectError):
        logger.warning(
            "Ошибка соединения или тайм-аут при получении ресурса {}",
            resource_id
        )
        logger.exception("Полный стек ошибки")

    except Exception:
        logger.warning(
            "Неожиданная ошибка при получении ресурса {}",
            resource_id
        )
        logger.exception("Полный стек ошибки")

    return None

fetch_resource(1)
fetch_resource(999)
fetch_resource(1, timeout=0.001)
