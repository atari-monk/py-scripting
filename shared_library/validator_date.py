from datetime import date, datetime

class ValidatorDate:
    @staticmethod
    def validate_date(value: str, date_format: str = "%Y-%m-%d") -> date:
        try:
            date_obj = datetime.strptime(value, date_format).date()
        except ValueError:
            raise ValueError(f"Date must be in the format {date_format}.")
        return date_obj

    @staticmethod
    def validate_relation(start_date: date, end_date: date):
        if end_date < start_date:
            raise ValueError(f"End date must be after {start_date.isoformat()}.")
