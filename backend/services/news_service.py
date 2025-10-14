from sqlmodel import Session, select
from backend.models.news import News
from backend.schema.news import NewsCreate, NewsUpdate

def get_all_news(db: Session):
    return db.exec(select(News)).all()

def get_news_by_id(db: Session, news_id: int):
    return db.get(News, news_id)

def get_news_by_category(db: Session, category_id: int):
    return db.exec(select(News).where(News.category_id == category_id)).all()

def get_news_by_author(db: Session, author_id: int):
    return db.exec(select(News).where(News.author_id == author_id)).all()

def create_news(db: Session, news_data: NewsCreate):
    news = News(**news_data.dict())
    db.add(news)
    db.commit()
    db.refresh(news)
    return news

def update_news(db: Session, news_id: int, news_data: NewsUpdate):
    news = db.get(News, news_id)
    if not news:
        return None
    for key, value in news_data.dict(exclude_unset=True).items():
        setattr(news, key, value)
    db.add(news)
    db.commit()
    db.refresh(news)
    return news

def delete_news(db: Session, news_id: int):
    news = db.get(News, news_id)
    if not news:
        return False
    db.delete(news)
    db.commit()
    return True
