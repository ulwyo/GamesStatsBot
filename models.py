from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///data.db"
Base = declarative_base()

def create_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()

class Hero(Base):
    __tablename__ = "heroes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    localized_name = Column(String)
    primary_attr = Column(String)
    attack_type = Column(String)
    roles = Column(String)
    legs = Column(Integer)

    @classmethod
    def create(cls, data: dict, session):
        hero = cls(
            name=data.get("name", ""),
            localized_name=data.get("localized_name", ""),
            primary_attr=data.get("primary_attr", ""),
            attack_type=data.get("attack_type", ""),
            roles=",".join(data.get("roles", [])),
            legs=data.get("legs", 0)
        )
        session.add(hero)

        return hero


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    personaname = Column(String)
    name = Column(String)
    plus = Column(Boolean)
    cheese = Column(Integer)
    steamid = Column(String)
    avatar = Column(String)
    avatarmedium = Column(String)
    avatarfull = Column(String)
    profileurl = Column(String)
    loccountrycode = Column(String)

    @classmethod
    def create(cls, data: dict, session):
        data = data.get("profile", {})
        player = cls(
            id=data.get("account_id", 0),
            personaname=data.get("personaname", ""),
            name=data.get("name", ""),
            plus=data.get("plus", False),
            cheese=data.get("cheese", 0),
            steamid=data.get("steamid", ""),
            avatar=data.get("avatar", ""),
            avatarmedium=data.get("avatarmedium", ""),
            avatarfull=data.get("avatarfull", ""),
            profileurl=data.get("profileurl", ""),
            loccountrycode=data.get("loccountrycode", "")
        )
        session.add(player)

        return player


class PlayerMatch(Base):
    __tablename__ = "player_matches"

    id = Column(Integer, primary_key=True)
    player_slot = Column(Integer)
    radiant_win = Column(Boolean)
    duration = Column(Integer)
    game_mode = Column(Integer)
    lobby_type = Column(Integer)
    hero_id = Column(Integer)
    version = Column(Integer)
    kills = Column(Integer)
    deaths = Column(Integer)
    assists = Column(Integer)
    average_rank = Column(Integer)
    leaver_status = Column(Integer)
    party_size = Column(Integer)
    hero_variant = Column(Integer)

    @classmethod
    def create(cls, data: dict, session):
        player_match = cls(
            id=data.get("match_id", 0),
            player_slot=data.get("player_slot", 0),
            radiant_win=data.get("radiant_win", False),
            duration=data.get("duration", 0),
            game_mode=data.get("game_mode", 0),
            lobby_type=data.get("lobby_type", 0),
            hero_id=data.get("hero_id", 0),
            version=data.get("version", 0),
            kills=data.get("kills", 0),
            deaths=data.get("deaths", 0),
            assists=data.get("assists", 0),
            average_rank=data.get("average_rank", 0),
            leaver_status=data.get("leaver_status", 0),
            party_size=data.get("party_size", 0),
            hero_variant=data.get("hero_variant", 0)
        )
        session.add(player_match)
