from datetime import date, datetime, time, timedelta
from decimal import Decimal
from typing import TypeAlias


SheetKey: TypeAlias = int | str
CellValue: TypeAlias = int | float | Decimal | str | bytes | datetime | date | time | timedelta | None
