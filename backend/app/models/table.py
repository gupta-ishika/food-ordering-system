from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Table(Base):
    __tablename__ = "tables"

    __table_args__ = (
        UniqueConstraint(
            "restaurant_id",
            "table_number",
            name="uq_restaurant_table_number",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    restaurant_id: Mapped[int] = mapped_column(
        ForeignKey("restaurants.id"),
        index=True,
        nullable=False,
    )

    table_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    qr_code_url: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    restaurant: Mapped["Restaurant"] = relationship(
        back_populates="tables",
    )

    orders: Mapped[list["Order"]] = relationship(
        back_populates="table",
        cascade="all, delete-orphan",
    )